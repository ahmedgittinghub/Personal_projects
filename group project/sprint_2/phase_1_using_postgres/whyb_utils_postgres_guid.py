from whyb_code_postgres_guid import *
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE= os.environ.get("postgres_db")
HOST=os.environ.get("postgres_host")
USER=os.environ.get("postgres_user")
PASSWORD=os.environ.get("postgres_pass")
# PORT= os.environ.get("postgres_port")

def setup_db_connection(database=DATABASE,host= HOST,user= USER,password= PASSWORD):
    connection = psycopg2.connect(database=database,host=host,user=user,password=password)
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
            branch_id VARCHAR(36) NOT NULL,
            branch_name varchar(70),
            PRIMARY KEY (branch_id)
        );
    """
    #SUB TABLE 3 - Payments
    create_payment_table = \
    """
         CREATE TABLE IF NOT EXISTS payments(
             payment_id VARCHAR(36) NOT NULL,
             payment_method varchar(70),
             PRIMARY KEY (payment_id)
        );
    """
    #SUB TABLE 5 - Products
    create_product_table ="""
        CREATE TABLE IF NOT EXISTS products(
            product_id VARCHAR(36) NOT NULL,
            product_name VARCHAR(255),
            product_price decimal(19,2),
            branch_id VARCHAR(36) NOT NULL,
            PRIMARY KEY (product_id),
            FOREIGN KEY(branch_id) REFERENCES branches(branch_id)
  
        );
    """
    #MAIN TABLE - Transactions
    create_transactions_table = \
    """
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id VARCHAR(36) NOT NULL,
            date_and_time_id TIMESTAMP,
            branch_id VARCHAR(36) NOT NULL,
            total_price decimal(19,2),
            payment_id VARCHAR(36) NOT NULL,
            PRIMARY KEY (transaction_id),
            FOREIGN KEY(branch_id) REFERENCES branches(branch_id),
            FOREIGN KEY(payment_id) REFERENCES payments(payment_id)
        );

    """
    #SUB TABLE 1 - Order_data 
    create_orders_table = \
    """
        CREATE TABLE IF NOT EXISTS order_data(
            transaction_id VARCHAR(36) NOT NULL,
            product_id VARCHAR(36) NOT NULL,
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
    # #1 to fill branch table
    # for data_row in branches_list:
    #     insert_row_sql = f"""INSERT INTO branches(branch_id,branch_name)
    #             VALUES('{data_row["branch_id"]}', '{data_row['branch']}')"""    
    #     cursor.execute(insert_row_sql)
    #     print("Branch table loaded succesfully!")
    for data_row in branches_list:
            branch_id = data_row["branch_id"]
            branch_name = data_row["branch"]

            # Check if the branch_id already exists in the table
            select_sql = f"SELECT branch_name FROM branches WHERE branch_name = '{branch_name}'"
            cursor.execute(select_sql)
            existing_branch = cursor.fetchone()

            if existing_branch:
                print(f"Branch with branch_name '{branch_name}' already exists. Skipping insertion.")
            else:
                # Insert the new row if the branch_id doesn't exist
                insert_row_sql = f"""INSERT INTO branches(branch_id, branch_name)
                                    VALUES('{branch_id}', '{branch_name}')"""
                cursor.execute(insert_row_sql)
                print(f"Inserted new branch with branch_name '{branch_name}'.")
    print("Branch table loaded succesfully!")

    connection.commit()

     #2 to fill products table
    for data_row in sorted_final_products_table_with_branches_reassigned:
        # insert_row_sql = f"""INSERT INTO products(product_id,product_name,product_price,branch_id)
        #         VALUES('{data_row["product_id"]}', '{data_row['product_name']}', 
        #         '{data_row['product_price']}', '{data_row['branch_id']}')"""    
        product_id = data_row["product_id"]
        product_name = data_row["product_name"]
        product_price = data_row['product_price']
        branch_id = data_row['branch_id']

        # Check if the branch_id already exists in the table
        select_sql = f"SELECT product_name FROM products WHERE product_name = '{product_name}'"
        cursor.execute(select_sql)
        existing_product = cursor.fetchone()

        if existing_product:
            print(f"Product with product_name '{product_name}' already exists. Skipping insertion.")
        else:
            # Insert the new row if the branch_id doesn't exist
            insert_row_sql =f"""INSERT INTO products(product_id,product_name,product_price,branch_id)
                    VALUES('{product_id}', '{product_name}','{product_price}', '{branch_id}')"""
            cursor.execute(insert_row_sql)
            print(f"Inserted new product with product name '{product_name}'.")
    # cursor.execute(insert_row_sql)
    print("Products table loaded succesfully!")

    connection.commit()


    #3 to fill payments table
    for data_row in payment_table:
    #     insert_row_sql = f"""INSERT INTO payments(payment_id,payment_method)
    #             VALUES('{data_row['payment_id']}', '{data_row['payment_method']}')"""    
    #     cursor.execute(insert_row_sql)
        payment_id = data_row["payment_id"]
        payment_method = data_row["payment_method"]

        # Check if the branch_id already exists in the table
        select_sql = f"SELECT payment_method FROM payments WHERE payment_method = '{payment_method}'"
        cursor.execute(select_sql)
        existing_payment = cursor.fetchone()

        if existing_payment:
            print(f"Payment method '{payment_method}' already exists. Skipping insertion.")
        else:
            # Insert the new row if the branch_id doesn't exist
            insert_row_sql =f"""INSERT INTO payments(payment_id,payment_method)
                    VALUES('{payment_id}', '{payment_method}')""" 
            cursor.execute(insert_row_sql)
            print(f"Inserted new Payment method '{payment_method}'.")
    print("Payments table loaded succesfully!")
    connection.commit()
    
    print(big_table_with_branch_id[1])
    #4 to fill main table - Transactions
    for data_row in big_table_with_branch_id:
        insert_row_sql = f"""INSERT INTO transactions(transaction_id,date_and_time_id,branch_id,total_price,payment_id)
                VALUES('{data_row['Transaction_id']}', '{data_row['Transaction_date_and_time']}', '{data_row['branch_id']}','{data_row['order_sum']}','{data_row['method_of_payment']}')"""    
        cursor.execute(insert_row_sql)
    print("Transactions table loaded succesfully!")

    connection.commit()

    #5 to fill orders table
    for data_row in orders_table_list:
        insert_row_sql = f"""INSERT INTO order_data(transaction_id,product_id,quantity)
                VALUES('{data_row['transaction_id']}', '{data_row['product_id']}', '{data_row['quantity']}')"""    
        cursor.execute(insert_row_sql)
    print("Orders table loaded succesfully!")

    connection.commit()
    print("All Data loaded succesfully!")


create_db_tables(connection, cursor)
load_db_tables(connection, cursor)
print("---------------------------------------------------------------------------------------------")
print("")
print("Operation completed succesfully! Please login via link http://localhost:8080/ to verify =)")

cursor.close()
connection.close()

