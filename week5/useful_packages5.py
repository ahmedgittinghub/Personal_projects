import csv


def name_insert(name):
    while name == '0':
         name = input("Please insert the name of the order: ")
    return name

def phone_number_insert(phone):
         
         
         while phone ==  '0' :
            phone = input('please insert a phone number with 11 digits or leave blank by pressing enter ')
            if len(phone.strip()) != 0:
                if phone.isdigit() == False or len(phone.strip()) != 11 :
                    print('invalid input, please ensure you insert the right phone number')
                    phone = '0'
                else:
                    break
            else:
                break
    
         return phone           



def file_closer(filename, list_of_data):
    print('appending changes to list ')
    try:
        f = open(filename, 'w')
    except FileNotFoundError as fnfe:
        print('file not found' + fnfe)
    finally:
        f.write('\n'.join(list_of_data))
        f.close()
        print('file closed')
        return list_of_data




def file_opener(filename, list_of_data):
    print('opening file ')
    try:
        f = open(filename,'r')
        lines = f.readlines()
    except FileNotFoundError as fnfe:
        print('file not found' + fnfe)
        
    finally:
        print(' all good, executing right now')
        for line in lines:
            list_of_data.append(line.rstrip())
        for items in list_of_data:
            if items == '':
                list_of_data.remove(items)
                print('all done dont worry')
    f.close()
    return list_of_data
        
def enumerated_list(listname):
    for index,items in enumerate(listname):
        print(index,items)



def list_index_number(k, listname):
    while type(k) != int :
        try:
            k = int(input('Please insert a number of the item you wish to change/delete: '))
        except ValueError:
            print('Please insert a valid input.')
            
        else:
            print('Well done, that\'s great!')

        if type(k) == int and k > len(listname):
            print('please insert a lower number ')
            k = ''
        elif type(k) == int and k == len(listname):
            print('please insert a lower number ')
            k = ''
    return k



def delete_function(k, listname):

    listname.pop(k)
    return listname



def ady_getter(something):
    while something == '0':
         unit_number = 0
         address_street = 0
         address_city = 0
         address_postcode1 = 0
         address_postcode2 = 0
         emptyy = ''
    
    
        
         while unit_number == 0 :
            unit_number = input('please give me your Unit Number ').title().strip()
         while address_street == 0 :
                address_street = input('Please insert your street address ').title().strip()
         while address_city == 0  :
                address_city = input('please insert your city ').capitalize().strip()
         while address_postcode1 == 0:
             address_postcode1 = input('please insert your 1STpostcode ').capitalize().strip()
             if address_postcode1.strip() != '':
                    if len(address_postcode1) < 2 or len(address_postcode1) > 4:
                        print('please input the correct characters')
                        address_postcode1 = 0
                    else:
                        print('thankyou for your input')
         
         while address_postcode2 == 0:
                address_postcode2 = input('please insert your 2NDpostcode ').capitalize().strip()
                if address_postcode2 != '':
                    if len(address_postcode2) != 3:
                        print('please input a potcode of 3 character')
                        address_postcode2 = 0
                    else:
                        print('thank you for your input')
         if unit_number.strip() != emptyy and address_street.strip() != emptyy and address_city.strip() != emptyy and address_postcode1.strip() != emptyy and  address_postcode2.strip() != emptyy:
                 print("address will be changed")
                 something = f'{unit_number}, {address_street}, {address_city}, {address_postcode1} {address_postcode2}'
                 

                 
                 
            
         elif unit_number.strip() == emptyy and address_street.strip() == emptyy and address_city.strip() == emptyy and address_postcode1.strip() == emptyy and address_postcode2.strip() == emptyy:
                print("Address was not insurted")
                something = '£'
                
            
         else:  
                print(' ')
                print('please insurt a valid input')
                unit_number = 0
                address_street = 0
                address_city = 0
                address_postcode1 = 0
                address_postcode2 = 0
        
    return something


def list_index_number2(k, listname):
    while k == '£':
        k = input('Please input the number you wish to choose or leave the field blank: ')
        if k.replace(' ', '') == '':
            print('Field was left empty')
            break
        elif k.replace(' ', '') != '':
            try:
                k = int(k)
            except ValueError:
                print("That's not a number! Insert a number or leave the field blank")
                k = '£'
            else:
                print('Number inserted')
                if k > len(listname):
                    print('number inserted is invalid')
                    k = '£'
                elif k == len(listname):
                    print('number inserted is invalid')
                    k = '£'
                else:
                    print('number inserted is valid')
                    break
    
    return k  


def open_csv_courier(filename, list_name):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            order = {
                "name": row['name'].strip(),
                "phone_number": row['phone_number'],
            }
            list_name.append(order)
    print('Opening Courier folder')
    return list_name

def close_csv_courier(filename,list_name):
     with open(filename, 'w', newline='') as output_file:
          writer = csv.writer(output_file)
          writer.writerow(["name", "phone_number"])  # Write the header row
          for item in list_name:
             writer.writerow([
                 item["name"],
                 item["phone_number"],
             ])
     print('Closing Courier folder')
     return list_name



def open_csv_products(filename, list_name):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            order = {
                "product_name": row['product_name'].strip(),
                "product_price": float(row['product_price']),
                
            }
            list_name.append(order)
    print('opening products file ')
    return list_name


def close_csv_products(filename,list_name):
     with open(filename, 'w', newline='') as output_file:
          writer = csv.writer(output_file)
          writer.writerow(["product_name", "product_price"])  # Write the header row
          for item in list_name:
             writer.writerow([
                 item["product_name"],
                 item["product_price"],
             ])
     print('closing products file')       
     return list_name


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
    print('opening orders file')
    return list_name



def close_csv_orders(filename,list_name):
     with open(filename, 'w', newline='') as output_file:
          for order in list_name:
            for items in order:
                if type(order[items]) == list:
                    order[items] = ','.join(order[items])   
          writer = csv.writer(output_file)
          writer.writerow(["customer_name", "customer_address","customer_phone","courier","status","items"]) 
          for order in list_name:
                order['items'] = ', '.join(order['items'])

          for order in list_name:
             writer.writerow([
                 order["customer_name"],
                 order["customer_address"],
                 order["customer_phone"],
                 order["courier"],
                 order["status"],
                 order["items"].strip().replace(' ','').replace(',,',''),
             ])
     print('closing orders file')
     return list_name
    


def price_insert(price):
    while price ==  '0' :
        
        price = input('please insert a number to update the price you want ')
        if len(price.strip()) != 0:
            try:
                price = float(price)
            except ValueError:
                
                print('invalid input, please ensure you insert the right phone number')
                price = '0'
            else:
                print('Input is valid')      
        else:
            break
    
    return price       

def item_filler(listname1,listname2):
    item1 = '$'
    while item1 == '$':
        item1 = input('please insert a valid number ')
        if item1.strip() == '':
            break
        elif item1.strip() != '' and item1.strip().isdigit() == False:
            print('please insert a valid input')
            item1 = '$'
        elif item1.strip().isdigit() == True:
            item1 = int(item1)
            if item1 > len(listname2):
                print('your number exceed the number of items in the list. insert a vlid number')
                item1 = '$'
            elif item1 == len(listname2):
                print('your number exceed the number of items in the list. insert a vlid number')
                item1 = '$'
                
            else:
                item1 = str(item1)
                listname1.append(item1)
                item1 = '$'
    
    return listname1


def id_number_insert(phone):
         
         
         while phone ==  '' :
            phone = input('please insert a suitable id number ')
            if len(phone.strip()) != 0:
                if phone.isdigit() == False or len(phone.strip()) != 11 :
                    print('invalid input, please ensure you insert the right phone number')
                    phone = '0'
                else:
                    break
            else:
                break
    
         return phone           


