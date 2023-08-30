import csv

orders_list = [ ]
def open_csv_orders(filename, list_name):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            order = {
                "customer_name": row['customer_name'].strip(),
                "customer_address": row['customer_address'].strip(),
                "customer_phone": row['customer_phone'].strip(),
                "courier": int(row['courier']),
                "status": row['status'].strip(),
                "items": list(row['items'].strip().replace(',','').replace(' ',''))
            }
            
            list_name.append(order)

# Example usage
open_csv_orders('orders.csv', orders_list)
print(orders_list)


# def close_csv_orders(filename,list_name):
#      with open(filename, 'w', newline='') as output_file:
#           for order in list_name:
#             for items in order:
#                 if type(order[items]) == list:
#                     order[items] = ', '.join(order[items])   
#           writer = csv.writer(output_file)
#           writer.writerow(["customer_name", "customer_address","customer_phone","courier","status","items"]) 
#           for order in list_name:
#                 order['items'] = ', '.join(order['items'])

#           for order in list_name:
#              writer.writerow([
#                  order["customer_name"],
#                  order["customer_address"],
#                  order["customer_phone"],
#                  order["courier"],
#                  order["status"],
#                  order["items"].strip().replace(' ','').replace(',,,',''),
#              ])
#      print('closing orders file')
#      return list_name
    

# close_csv_orders('orders.csv', orders_list)
# print('closed alll ')

# products_list = [{'product_name': 'Dr Pepper', 'product_price': 0.8}]

# def open_csv_products(filename, list_name):
#     with open(filename, 'r') as csv_file:
#         reader = csv.DictReader(csv_file)
#         for row in reader:
#             order = {
#                 "product_name": row['product_name'].strip(),
#                 "product_price": float(row['product_price']),
                
#             }
#             list_name.append(order)

# open_csv_products('products.csv', products_list)
# print(products_list)

# def close_csv_products(filename,list_name):
#      with open(filename, 'w', newline='') as output_file:
#           writer = csv.writer(output_file)
#           writer.writerow(["product_name", "product_price"])  # Write the header row
#           for item in list_name:
#              writer.writerow([
#                  item["product_name"],
#                  item["product_price"],
#              ])
            
#      return list_name


# close_csv_products('products.csv',products_list)


# courier_list = [{'name':'ahmed','phone_number':'07398952757'}]


# def open_csv_courier(filename, list_name):
#     with open(filename, 'r') as csv_file:
#         reader = csv.DictReader(csv_file)
#         for row in reader:
#             order = {
#                 "name": row['name'].strip(),
#                 "phone_number": row['phone_number'],
#             }
#             list_name.append(order)


# open_csv_courier('courier.csv', courier_list)

# print(courier_list)


# def close_csv_courier(filename,list_name):
#      with open(filename, 'w', newline='') as output_file:
#           writer = csv.writer(output_file)
#           writer.writerow(["name", "phone_number"])  # Write the header row
#           for item in list_name:
#              writer.writerow([
#                  item["name"],
#                  item["phone_number"],
#              ])
#      print('Closing CSV file')      
#      return list_name

# close_csv_courier('courier.csv', courier_list)

# some_list1 = [ ]
# some_list2 = [1,2,3,4,5,6]

# def item_filler(listname1,listname2):
#     item1 = '$'
#     while item1 == '$':
#         item1 = input('please insert a valid number ')
#         if item1.strip() == '':
#             break
#         elif item1.strip() != '' and item1.strip().isdigit() == False:
#             print('please insert a valid input')
#             item1 = '$'
#         elif item1.strip().isdigit() == True:
#             item1 = int(item1)
#             if item1 > len(listname2):
#                 print('your number exceed the number of items in the list. insert a vlid number')
#                 item1 = '$'
#             else:
                
#                 listname1.append(item1)
#                 item1 = '$'
    
#     return listname1

# while bool(some_list1) == False:
#     some_list1 = item_filler(some_list1,some_list2)

# print(some_list1)




# def item_filler(listname1,listname2):
#     item1 = '$'
#     while item1 == '$':
#         item1 = input('please insert a valid number ')
#         if item1.strip() == '':
#             break
#         elif item1.strip() != '' and item1.strip().isdigit() == False:
#             print('please insert a valid input')
#             item1 = '$'
#         elif item1.strip().isdigit() == True:
#             item1 = int(item1)
#             if item1 > len(listname2):
#                 print('your number exceed the number of items in the list. insert a vlid number')
#                 item1 = '$'
#             else:
#                 item1 = str(item1)
                
#                 listname1.append(item1)
#                 item1 = '$'
    
#     return listname1


