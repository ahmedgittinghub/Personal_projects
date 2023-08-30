import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")






# print('Selecting all records...')
#           # TODO Add code here to select all the records
# cursor1.execute('SELECT * FROM products')
# rows = cursor1.fetchall()







def setup_db_connection(host = host_name, user = user_name, password = user_password , database = database_name):
    try:
        connection = pymysql.connect(host = host_name, user = user_name, password = user_password , database = database_name)
        cursor = connection.cursor()
        print("We connected!")

    except Exception as ex:
        print('Failed to:' , ex)

    return connection, cursor

connection, cursor = setup_db_connection()


print('Selecting all records...')
# TODO Add code here to select all the records
cursor.execute('SELECT * FROM products')
rows = cursor.fetchall()

products_dict = {'product_id':'','product_name':'', 'product_price':''}

check_dict = {'product_name':'', 'product_price':''}




# print('Inserting new record...')
#     # Insert a new record
# sql = """
#     INSERT INTO products (product_Name, product_price) 
#     VALUES (%s, %s)
#     """
# data_values = ('Dr pepper', 0.9)
# cursor.execute(sql, data_values)
# # Commit the record
# connection.commit()

product_add = {'product_name':'Dr pepper', 'product_price':'0.8'}

query="select * from products where product_Name = 'Dr pepper'"

print(cursor.execute(query))


print('Displaying all records...')
# TODO Add code here to print out all the records
for row in rows:
    products_dict['product_id'] = row[0]
    products_dict['product_name'] = row[1]
    products_dict['product_price'] = row[2]

    if products_dict['product_name'] == product_add['product_name']:
        print('no')
    else:
        print('yes')
    print(products_dict)


# to print what you want 
query = "select * from products where product_Name = 'Dr pepper'"
cursor.execute(query)

# Fetch all rows from the result set
result = cursor.fetchall()

# Print the fetched rows
for row in result:
    print(row)

# You can also print specific columns from the rows if needed
# For example: print(row['column_name'])
