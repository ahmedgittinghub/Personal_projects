import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

def setup_db_connection(host = host_name, user = user_name, password = user_password , database = database_name):
    try:
        connection = pymysql.connect(host = host_name, user = user_name, password = user_password , database = database_name)
        cursor = connection.cursor()
        print("We connected!")

    except Exception as ex:
        print('Failed to:' , ex)

    return connection, cursor

def table_printer(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    print('\n')


def product_printer(something):
    products_dict = {'product_id':'','product_name':'', 'product_price':''}
    for row in something:
        products_dict['product_id'] = row[0]
        products_dict['product_name'] = row[1]
        products_dict['product_price'] = row[2]
        print(products_dict)


connection, cursor = setup_db_connection()

def check_product(something,checker):
    products_dict = {'product_id':'','product_name':'', 'product_price':''}
    # to print what you want 
    query = "select * from products "
    cursor.execute(query)
    # Fetch all rows from the result set
    result = cursor.fetchall()

    for row in result:
        products_dict['product_id'] = row[0]
        products_dict['product_name'] = row[1]
        products_dict['product_price'] = row[2]
    
        if products_dict['product_name'].replace(' ','').lower() == something.replace(' ','').lower():
            
            checker = 'no'
            break
        else:
            checker = 'yes'
            
    
    return checker

def add_product(name,price):
    print('Inserting new record...')
    # Insert a new record
    sql = """
        INSERT INTO products (product_Name, product_price) 
        VALUES (%s, %s)
        """
    data_values = (name, price)
    cursor.execute(sql, data_values)
    # Commit the record
    connection.commit()

def id_number_check_products_table(table_name,id_number, checker):
    while id_number.isdigit() == False:
        id_number = input('please insert a the ID number of the item you wish to change: ')
         # to print what you want 
        query = f"select product_ID from {table_name} "
        cursor.execute(query)
    # Fetch all rows from the result set
        result = cursor.fetchall()
        for row in result:
            if row == int(id_number):
                print('product ID exist')
                checker = 'yes'
                break
            else:
                print("product ID doesn't exist")
                checker = 'no'




def product_name_check(product_name, checker):
    query = "select product_Name from products "
    cursor.execute(query)
    # Fetch all rows from the result set
    result = cursor.fetchall()

    for row in result:
    
        if row == product_name:
            print('product Name already  exist')
            checker = 'yes'
            break
        else:
            print("product Name doesn't exist")
            checker = 'no'
    
    return checker

def product_name_change(product_id, new_name):
    query = "UPDATE products SET product_Name = %s WHERE product_ID = %s"
    cursor.execute(query, (new_name, product_id))
    connection.commit()

def product_price_change(product_id, new_price):
    query = "UPDATE products SET product_price = %s WHERE product_ID = %s"
    data_values = (new_price, product_id)
    cursor.execute(query, data_values)
    connection.commit()

def delete_product(product_id):
    query = f"DELETE FROM products WHERE product_ID = {product_id}"
    cursor.execute(query)
    connection.commit
