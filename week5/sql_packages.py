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

def id_number_check_products_table(id_number, checker):
    while id_number == '$':
        id_number = input('please insert a the ID number of the item you wish to change: ')

        if id_number.strip() == '':
            print('ID number was not inserted, leaving menu')
            checker = 'no change'
         # to print what you want 
        else:
            if id_number.isdigit() == False:
                id_number = '$'
                ('NOT A number, please insert a number')
            elif id_number.isdigit() == True:
                query = "select product_ID from products"
                cursor.execute(query)
    # Fetch all rows from the result set
                result = cursor.fetchall()
                checker = 'no'
                for row in result:
                    if row[0] == int(id_number):
                        print('product ID exist')
                        checker = 'yes'
                        break
                if checker == 'no':
                    print("product ID doesn't exist")
                    checker = 'no'
                    


        
    return id_number,checker

def product_name_check(product_name, checker):
    query = "select product_Name from products "
    cursor.execute(query)
    # Fetch all rows from the result set
    result = cursor.fetchall()
    checker = 'no'
    for row in result:
    
        if row[0].replace(' ','').lower() == product_name.replace(' ','').lower():
            print('product Name already  exist')
            checker = 'yes'
            break
    if checker == 'no':
            print("product Name doesn't exist")
    
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
    connection.commit()


def add_products_to_orders(some_list):
    basket = []
    checker = ''
    product_id = '$'
    while product_id == '$':
        product_id, checker = id_number_check_products_table(product_id, checker)
        if checker == 'no':
            print('Product doesnt exist')
            product_id = '$'
        elif checker == 'no change':
            print('No Id was inserted')
            some_list = basket
            product_id = 'done'
            break
        elif checker == 'yes':
            print('product will be added to basket')
            basket.append(product_id)
            product_id = '$'
    
    return some_list
# #############
########333####
##### Courier SQL commands





def courier_printer(something):
    products_dict = {'product_id':'','product_name':'', 'product_price':''}
    for row in something:
        products_dict['product_id'] = row[0]
        products_dict['product_name'] = row[1]
        products_dict['product_price'] = row[2]
        print(products_dict)



def add_courier(name,phone_number):
    print('Inserting new record...')
    # Insert a new record
    sql = """
        INSERT INTO couriers (courier_Name, phone_number) 
        VALUES (%s, %s)
        """
    data_values = (name, phone_number)
    cursor.execute(sql, data_values)
    # Commit the record
    connection.commit()

def id_number_check_couriers_table(id_number, checker):
    while id_number == '$':
        id_number = input('please insert a the ID number of the Courier you wish to change: ')

        if id_number.strip() == '':
            print('ID number was not inserted, leaving menu')
            checker = 'no change'
         # to print what you want 
        else:
            if id_number.isdigit() == False:
                id_number = '$'
                ('NOT A number, please insert a number')
            elif id_number.isdigit() == True:
                query = "select courier_ID from couriers"
                cursor.execute(query)
    # Fetch all rows from the result set
                result = cursor.fetchall()
                checker = 'no'
                for row in result:
                    if row[0] == int(id_number):
                        print('Courier ID exist')
                        checker = 'yes'
                        break
                if checker == 'no':
                    print("Courier ID doesn't exist")
                    checker = 'no'
                           
    return id_number,checker

def courier_phone_check(phone_number, checker):
    query = "select phone_number from couriers "
    cursor.execute(query)
    # Fetch all rows from the result set
    result = cursor.fetchall()
    checker = 'no'
    for row in result:
    
        if row[0].replace(' ','') == phone_number.replace(' ',''):
            print('phone number already  exist')
            checker = 'yes'
            break
    if checker == 'no':
            print("phone number doesn't exist")
    
    return checker

def courier_name_change(courier_id, courier_name):
    query = "UPDATE couriers SET courier_Name = %s WHERE courier_ID = %s"
    cursor.execute(query, (courier_name, courier_id))
    connection.commit()

def phone_number_change(courier_id, new_phone_number):
    query = "UPDATE couriers SET phone_number = %s WHERE courier_ID = %s"
    data_values = (new_phone_number, courier_id)
    cursor.execute(query, data_values)
    connection.commit()

def delete_courier(courier_id):
    query = f"DELETE FROM couriers WHERE courier_ID = {courier_id}"
    cursor.execute(query)
    connection.commit()


