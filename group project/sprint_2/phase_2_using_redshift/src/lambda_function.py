import json
# import boto3 # library used to access AWS API
import csv
import psycopg2 as psy
from datetime import datetime
from data_utils import *
from sql_utils import *


param_name = 'where_have_you_bean_redshift_settings'

s3 = boto3.client('s3')
# (https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html)


def lambda_handler(event, context): #To extract data from CSV and create a list from it.
    try:
        print(f'lambda_handler: started: event=${event}')
       
        bucket = event["Records"][0]['s3']['bucket']['name'] 
        #code to find bucket the event took place in
        print("Bucket located")
        s3file= event["Records"][0]['s3']['object']['key']
        #code to find file the event that triggered event
        
        print(f'lambda_handler: bucket={bucket}, key={s3file}')
        #code to print file/bucket that triggered event
    
        response = s3.get_object(Bucket=bucket, Key=s3file)
        #code to get this file from bucket
        
        #Next step is to actually extract data from file
        file = response['Body'].read().decode('utf-8').split('\n')
        #this will read the file and decode so is in correct format
        
        print("Data extracted!")
        source_file =csv.DictReader(file, fieldnames=['purchase_date', 'branch', 'customer_name', 'items', 'total', 'mode_of_payment', 'cardnumber'], delimiter=',')
        data = []
        
        for row in source_file: #the following lines correct the date format so it can be uploaded to a database later
                date_str = row["purchase_date"]
                datetime_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
                row["purchase_date"] = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
                data.append(row)
        print("Data placed into a list.")
        
    except Exception as error:
        print("An error occurred: " + str(error))
    print(f'We are verifying the data was extracted correctly by printing the first entry:{data[0]}')
    #Now need to run code on data list
    # ========================================================================================== Making lists==========================================
    redshift_details = get_ssm_param(param_name)
    print("")
    connection, cursor  = open_sql_database_connection_and_cursor(redshift_details)
    print("Processed complete! Setup connection with redshift")    
    print("")
    create_db_tables(connection, cursor)
    print("")
    print("Now will form lists to fill database with")
    reformatted_data = separate_items_into_list_within_a_list(data,'items') #data extracted is now in form A list of dictionaries with the items field as a list aswell
    reformatted_cleaned_data = coloumn_deleter(reformatted_data,'cardnumber') #removes card number field from data
    reformatted_cleaned_data = coloumn_deleter(reformatted_cleaned_data,'customer_name') #removes customer name field from data
    branches_list = branch_list(reformatted_cleaned_data,cursor)
    initial_products_table = form_initial_products_list(reformatted_cleaned_data,) #fill empty products table with just the product: name, price, id and soon number ordered 
    new_products_table = drop_duplicate(initial_products_table,initial_products_table,'product_name') #removes all duplicate products 
    final_products_table = create_final_products_list(reformatted_cleaned_data,new_products_table)
    final_products_table = product_id_checker_and_reassigner(final_products_table, cursor)
    final_products_table_with_branches_reassigned = branch_id_reassigner(final_products_table, branches_list) # Verify if used!
    sorted_final_products_table = sorting_alphabetically(final_products_table, "product_name") # Full list of unique products final_products_table in alphabetical order
    sorted_final_products_table_with_branches_reassigned = branch_id_reassigner(sorted_final_products_table, branches_list) # this is the final products table used to fill products table with branch names reassgined to their respective product_ids
    payment_table = [{'payment_id':1, 'payment_method': 'CASH'},{'payment_id':2, 'payment_method': 'CARD'}] #creating payment table list
    payment_table = payment_id_checker_and_reassigner(payment_table,cursor)
    big_table = create_main_table_list(reformatted_cleaned_data,final_products_table) #list of information needed for main table
    orders_table_list = orders_table_func(big_table) #list i will use to create orders table
    big_table_with_branch_id= branch_id_reassigner(big_table,branches_list)
    big_table_with_branch_id= payment_id_reassigner(big_table_with_branch_id,payment_table) #list i will use to create main table (now has payment id and branch id reassigned)
    print("Processed complete! All required data for SQL tables have been extracted and sorted.")
    print("") 
    load_branch_tables(connection, cursor, branches_list)
    load_products_tables(connection, cursor, sorted_final_products_table_with_branches_reassigned)
    load_payments_tables(connection, cursor, payment_table)
    load_Transactions_tables(connection, cursor, big_table_with_branch_id)
    load_orders_tables(connection, cursor, orders_table_list)
    print("All Data loaded succesfully!")
    print("---------------------------------------------------------------------------------------------")
    print("")
    print("Operation completed succesfully! Please verify in Redshift database)")
    cursor.close()
    connection.close()
  
    