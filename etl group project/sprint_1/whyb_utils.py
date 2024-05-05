from whyb_code import *
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.environ.get("mysql_host")
USER = os.environ.get("mysql_user")
PASSWORD = os.environ.get("mysql_pass")
WAREHOUSE_DB_NAME = os.environ.get("mysql_db")

# def create_database(cursor, db_name): #could be used to create database but NOT NEEDED
#     cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
#     cursor.execute(f'USE {db_name};')
#     connection.commit()




def setup_db_connection(host=HOST, user=USER, password=PASSWORD, warehouse_db_name=WAREHOUSE_DB_NAME):
    connection = pymysql.connect(host=host, user=user, password=password, database=warehouse_db_name)
    cursor = connection.cursor()
    print("We connected!")
    return connection, cursor


connection, cursor = setup_db_connection()


def create_db_tables(connection, cursor): #this will create all our data tables
    print("Creating tables....")
    #SUB TABLE 2 - Branches
    create_branches_data_table = \
    """
        CREATE TABLE IF NOT EXISTS branches(
            branch_id int NOT NULL AUTO_INCREMENT,
            branch_name varchar(70),
            PRIMARY KEY (branch_id)
        );
    """
    #SUB TABLE 3 - Payments
    create_payment_table = \
    """
         CREATE TABLE IF NOT EXISTS payments(
             payment_id int NOT NULL AUTO_INCREMENT,
             payment_method varchar(70),
             PRIMARY KEY (payment_id)
        );
    """
    #SUB TABLE 5 - Products
    create_product_table ="""
        CREATE TABLE IF NOT EXISTS products(
            product_id int NOT NULL AUTO_INCREMENT,
            product_name VARCHAR(255),
            product_price decimal(19,2),
            branch_id int,
            PRIMARY KEY (product_id),
            FOREIGN KEY(branch_id) REFERENCES branches(branch_id)
  
        );
    """
    #MAIN TABLE - Transactions
    create_transactions_table = \
    """
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id int NOT NULL AUTO_INCREMENT,
            date_and_time_id DATETIME,
            branch_id int,
            total_price decimal(19,2),
            payment_id int,
            PRIMARY KEY (transaction_id),
            FOREIGN KEY(branch_id) REFERENCES branches(branch_id),
            FOREIGN KEY(payment_id) REFERENCES payments(payment_id)
        );

    """
    #SUB TABLE 1 - Order_data 
    create_orders_table = \
    """
        CREATE TABLE IF NOT EXISTS order_data(
            transaction_id int NOT NULL,
            product_id int,
            quantity int,
            PRIMARY KEY(product_id, transaction_id),
            FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
                );
    """
    cursor.execute(create_branches_data_table)
    cursor.execute(create_payment_table)
    cursor.execute(create_product_table)
    cursor.execute(create_transactions_table)
    cursor.execute(create_orders_table)
    connection.commit()
    print("Tables created succesfully!")
    

def load_db_tables(connection, cursor): #this will fill all our data tables with the data required
    print("Now loading data into tables....")
    #1 to fill branch table
    for data_row in branches_list:
        insert_row_sql = f"""INSERT INTO branches(branch_id,branch_name)
                VALUES('{data_row['branch_id']}', '{data_row['branch']}')"""    
        cursor.execute(insert_row_sql)
        print("branch table created succesfully!")

    connection.commit()

     #2 to fill products table
    for data_row in sorted_final_products_table_with_branches_reassigned:
        insert_row_sql = f"""INSERT INTO products(product_id,product_name,product_price,branch_id)
                VALUES('{data_row['product_id']}', '{data_row['product_name']}', 
                '{data_row['product_price']}', '{data_row['branch_id']}')"""    
        cursor.execute(insert_row_sql)
    print("products table created succesfully!")

    connection.commit()


    #3 to fill payments table
    for data_row in payment_table:
        insert_row_sql = f"""INSERT INTO payments(payment_id,payment_method)
                VALUES('{data_row['payment_id']}', '{data_row['payment_method']}')"""    
        cursor.execute(insert_row_sql)
    connection.commit()

    #4 to fill main table - Transactions
    for data_row in big_table_with_branch_id:
        insert_row_sql = f"""INSERT INTO transactions(transaction_id,date_and_time_id,branch_id,total_price,payment_id)
                VALUES('{data_row['Transaction_id']}', '{data_row['Transaction_date_and_time']}', '{data_row['branch_id']}','{data_row['order_sum']}','{data_row['method_of_payment']}')"""    
        cursor.execute(insert_row_sql)
    connection.commit()

    #5 to fill orders table
    for data_row in orders_table_list:
        insert_row_sql = f"""INSERT INTO order_data(transaction_id,product_id,quantity)
                VALUES('{data_row['transaction_id']}', '{data_row['product_id']}', '{data_row['quantity']}')"""    
        cursor.execute(insert_row_sql)
    connection.commit()
    print("Data loaded succesfully!")


create_db_tables(connection, cursor)
load_db_tables(connection, cursor)
print("---------------------------------------------------------------------------------------------")
print("")
print("Operation completed succesfully! Please login via link http://localhost:8080/ to verify =)")

cursor.close()
connection.close()

