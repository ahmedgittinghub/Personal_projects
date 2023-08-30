from packages4 import enumerated_list

from packages4 import list_index_number
from packages4 import name_insert
from packages4 import delete_function
from packages4 import file_closer
from packages4 import file_opener
from packages4 import ady_getter
import os
from packages4 import phone_number_insert
from packages4 import list_index_number2
import csv
from packages4 import open_csv_orders
from packages4 import close_csv_orders
from packages4 import open_csv_products
from packages4 import close_csv_products
from packages4 import close_csv_courier
from packages4 import open_csv_courier
from packages4 import price_insert
from packages4 import item_filler

orders_list = []
products_list = []
couriers_list = []

# LOAD products from products.csv
open_csv_products('products.csv',products_list)    
# LOAD couriers from couriers.csv    
open_csv_courier('courier.csv',couriers_list)
# LOAD orders from orders.csv
open_csv_orders('orders.csv',orders_list)

# CREATE order status list
order_status_list = ['starting','preparing','completed']



# CREATE orders list of dictionaries  

# CREATE order status list                
menu_options = [' Save & Exit app', 'Products Menu', 'Couriers Menu','Orders Menu']



# GET user input for main menu option
user_input = ''
cafe_open = True
while  cafe_open == True and user_input not in ['0','1','2','3']:
    enumerated_list(menu_options)

    user_input = input('please insert a number from 0,1,2,3: ')
    print('')

    if user_input == '0':
        #  SAVE products list to products.csv
         close_csv_products('products.csv',products_list)
        #  SAVE couriers list to couriers.csv
         close_csv_courier('courier.csv', couriers_list)
        #  SAVE orders list to order.csv
         close_csv_orders('orders.csv', orders_list)
        #  EXIT app
         os.system('clear')
         cafe_open = False


    # ELSE IF user input is 1:
    elif user_input == '1':
        os.system('clear')
        
        print('welcome to the products menu')
        open_menu = True
        #PRINT product menu options
        menu_options1 = ['Return to main menu','Print product list','Create a new product','Update existing product','Delete existing product']
        

        user_input1 = ''

        #GET user input for product menu option
        while  open_menu == True and user_input1 not in ['0','1','2','3','4']:
            enumerated_list(menu_options1)
            user_input1 = input('please insert a choice from 0,1,2,3,4:  ')

            
            #IF user inputs 0:

            if user_input1 == '0':
               #RETURN to main menu
                
                user_input = ''
                open_menu = False
                os.system('clear')
                print('Going back to Main menu')


            #     ELSE IF user input is 1:
            elif user_input1 == '1':
                 os.system('clear')
                 # PRINT products list
                 enumerated_list(products_list)
                 print('\n')
               
            
                 user_input1 = ''
            
            elif user_input1 == '2':
                os.system('clear')

                dict1 = {"product_name": "0", "product_price": "0"}

                # GET user input for product name
                while dict1["product_name"] == "0":
                    dict1["product_name"] = name_insert(dict1["product_name"])
                    if dict1["product_name"].strip() == '':
                        dict1["product_name"] = "0"
                    else:
                        break
                # GET user input for product price
                while dict1["product_price"] == "0":
                    dict1["product_price"] = price_insert(dict1["product_price"])
                    if type(dict1["product_price"]) != float:
                        dict1["product_price"] = "0"
                        print('please insert a valid input for price')
                    else:
                        break

                # APPEND product dictionary to products list 
                products_list.append(dict1)
                print('\n')
                enumerated_list(products_list)

                
                user_input1 = ''

                

            elif user_input1 == '3':
                os.system('clear')
                update_number = ''

                dict13 = {"product_name": "0", "product_price": "0"}
                
                # PRINT products with their index values
                enumerated_list(products_list)

                # GET user input for product index value
                update_number = list_index_number(update_number,products_list)

                # GET user input for updated property
                while dict13["product_name"] == "0":
                    dict13["product_name"] = name_insert(dict13["product_name"])
                    if dict13["product_name"].strip() == '':
                        print("product will not be changed")
                        break
                    elif dict13["product_name"].strip() != '':
                        products_list[update_number]["product_name"] = dict13["product_name"]
                        break
                
                while dict13["product_price"] == "0":
                    dict13["product_price"] = price_insert(dict13["product_price"])
                    if type(dict13["product_price"]) == float :
                            products_list[update_number]["product_price"] = dict13["product_price"]
                            break
                    elif dict13["product_price"].strip() == '':
                        print("product price will not be changed")
                        break
                    elif dict13["product_price"].strip() != '' and type(dict13["product_price"]) != float:
                            print('please insert a vlid input for the price ')
                            dict13["product_price"] == "0"
                    
                print('\n')
                os.system('clear')

                enumerated_list(products_list)
                print('\n')
                
                user_input1 = ''
                
            elif user_input1 == '4':
                os.system('clear')

                enumerated_list(products_list)

                del_choice = ''

                del_choice = list_index_number(del_choice, products_list)

                products_list.pop(del_choice)

                enumerated_list(products_list)
             
                user_input1 = ''
            


    elif user_input == '2':
        os.system('clear')
        
        print('welcome to couries menu')
        
        #   open_couries_menu = True
        open_couries_menu = True

        #PRINT couries menu options
        menu_options2 = ['Return to main menu','Print courie list','Create a new courie','Update existing courie','Delete existing courie']
        

        user_input2 = ''

        #GET user input for product menu option
        while  open_couries_menu == True and user_input2 not in ['0','1','2','3','4']:
            enumerated_list(menu_options2)
            user_input2 = input('please insert a choice from 0,1,2,3,4:  ')


            if user_input2 == '0' :
                
               #RETURN to main menu
               print('returning to main menu')

               
               user_input = ''

               os.system('clear')
               open_couries_menu = False
            


            elif user_input2 == '1':
                os.system('clear')
                
                #  PRINT couriers list
                enumerated_list(couriers_list)
                print('\n')

                user_input2 = ''
            

            # CREATE new courier
            elif user_input2 == '2':
                 # CREATE new courier dictionary with above properties
                 dict22 = {"name": "0","phone_number":"0"}
                 os.system('clear')

                  # GET user input for courier name
                 while dict22["name"] == "0":
                    dict22["name"] = name_insert(dict22["name"])
                    if dict22["name"].strip() == '':
                        dict22["name"] = "0"
                    else:
                        break

                # GET user input for courier phone number
                 while dict22["phone_number"] == '0':
                    dict22["phone_number"] = phone_number_insert(dict22["phone_number"])
                    if dict22["phone_number"].replace(' ','').isdigit() == False:
                         dict22["phone_number"] = '0'
                    else:
                        break

                  # APPEND courier dictionary to courier list
                 couriers_list.append(dict22)
                 enumerated_list(couriers_list)

                     
                 

                 user_input2 = ''
                 

       
        
        
       
                
            
            elif user_input2 == '3':

                dict23 = {"name": "0","phone_number":"0"}
                os.system('clear')
                update_number2 = ''
                # STRETCH GOAL - UPDATE existing courier
                
                # PRINT courier with their index values
                enumerated_list(couriers_list)
                print('\n')

                # GET user input for courier index value
                update_number2 = list_index_number(update_number2,couriers_list)

                print('\n')

                #Couriers Name
                while dict23["name"] == '0':
                    dict23["name"] = name_insert(dict23["name"])
                    if dict23["name"].strip() == '' :
                        print('no name for the courier  was inserted, name wont be changed')
                    elif dict23["name"].strip != '':
                        couriers_list[update_number2]["name"] = dict23["name"]
                 
                 #Couriers phonenuber
                while dict23["phone_number"] == '0':
                    dict23["phone_number"] = phone_number_insert(dict23["phone_number"])
                if dict23["phone_number"].replace(' ','') != '' and dict23["phone_number"].replace(' ','').isdigit() == False:
                    print("please leave the field empty or insert 11 digits phone number")
                    dict23["phone_number"] = '0'
             
                elif dict23["phone_number"].replace(' ','').isdigit() == True:
                    couriers_list[update_number2]["phone_number"] = dict23["phone_number"]
                else:
                    print("phone number won't be changed")
                
                print('\n')

                enumerated_list(couriers_list)

                print('\n')

                user_input2 = ''       


            elif user_input2 == '4':
                os.system('clear')

                enumerated_list(couriers_list)

                del_choice2 = ''

                del_choice2 = list_index_number(del_choice2, couriers_list)

                couriers_list.pop(del_choice2)
                print('\n')

                enumerated_list(couriers_list)
               
                user_input2 = ''
    
    # ELSE IF user input is 3:
    elif user_input == '3':
        
        print('welcome to orders menue')

        open_orders_menu = True
        menu_options3 = ['Main Menu',' View Orders Dictionary','New order Input',' Update existing order status','update existing order details',' delete product']

        user_input3 = ''

        while  open_orders_menu == True and user_input3 not in ['0','1','2','3','4','5']:
            enumerated_list(menu_options3)
            user_input3 = input('please insert a choice from 0,1,2,3,4,5:  ')

            
            # IF user input is 0:
            if user_input3 == '0' :
               
                
               #RETURN to main menu
               print('returning to main menu')

               
               user_input = ''
               
               open_couries_menu = False
               os.system('clear')


             # ELSE IF user input is 1:
            elif user_input3 == '1':
                 os.system('clear')
                 #  PRINT orders dictionary
                 
                 enumerated_list(orders_list)

                 print('\n')


                 user_input3 = ''



            # ELSE IF user input is 2:
            elif user_input3 == '2':
               os.system('clear')

               dict32 = {'customer_name': '0', 'customer_address': '0', 'customer_phone': '0', 'courier': '', 'status': '0', 'items': [ ]}
               
               # Customer_name
               while dict32["customer_name"] == '0':
                dict32["customer_name"] = name_insert(dict32["customer_name"])
                if dict32["customer_name"].replace(' ','').isalpha() == False: 
                    dict32["customer_name"] = '0'
                else:
                    break

                
              # Customer address
               while dict32["customer_address"] == '0':
                dict32["customer_address"] = ady_getter(dict32["customer_address"])
                if dict32["customer_address"] == '£':
                    print("Please insert a valid input for the address.")
                    dict32["customer_address"] = '0'
                else:
                    print('thank you address inserted correctly')
                    break
    
                

                #Customer Phone Number 
               while dict32["customer_phone"] == '0':
                    dict32["customer_phone"]  = phone_number_insert(dict32["customer_phone"])
                    if dict32["customer_phone"] .replace(' ','').isdigit() == False:
                        dict32["customer_phone"]  = '0'
                    else:
                        break
                        os.system('clear')
                
                #GET user input for courier index to select courier
               print('now please choose a couries from the list below by typing in a index number')
               #PRINT couriers list with index value for each courier
               enumerated_list(couriers_list)
                #GET user input for courier index to select courier
               cory_num = ''
               cory_num = list_index_number(cory_num,couriers_list)
               dict32['courier'] = cory_num

                 
               #Customer Items
               print('Now taking items')
               while bool(dict32['items']) == False:
                 enumerated_list(products_list)
                 dict32['items'] = item_filler(dict32['items'],products_list)

               
                
               dict32["status"] = "preparing"

               orders_list.append(dict32)
               enumerated_list(orders_list)

               
               os.system('clear')
               
               user_input3 = ''

            # ELSE IF user input is 3:
            elif user_input3 == '3':
                 os.system('clear')

                 #     PRINT orders list with its index values
                
                 enumerated_list(orders_list)
                 print('\n')

                 switch_number = ''
                #     GET user input for order index value
                 switch_number = list_index_number(switch_number,orders_list)

                #PRINT order status list with index values
                 enumerated_list(order_status_list)
                 change_status_number = ''
                 print('please select an approprite number that macthes the status you wish to change your order to')
                # GET user input for order status index value
                 change_status_number = list_index_number(change_status_number,order_status_list)
                 #UPDATE status for order
                 orders_list[switch_number]['status'] = order_status_list[change_status_number]

                 enumerated_list(orders_list)

                 print('\n')

                 user_input3 = ''
            
               
            

            elif user_input3 == '4':
                dict34 = {'customer_name': '0', 'customer_address': '0', 'customer_phone': '0', 'courier': '', 'status': '0', 'items': [ ]}

                os.system('clear')
                enumerated_list(orders_list)

                change_number = ''

                print('please insert the number of the order u wish to change')

                change_number = list_index_number(change_number,orders_list)

                 #customer name
                while dict34["customer_name"] == '0':
                    dict34["customer_name"] = name_insert(dict34["customer_name"])
                    if dict34["customer_name"].strip() == '' :
                        print('no name was inserted, name wont be changed')
                    elif dict34["customer_name"].replace(' ','').isalpha() == True:
                        orders_list[change_number]["customer_name"] = dict34["customer_name"]
                    else:
                        print('insert a valid input or leaveit empty ')
               
                 # customer address
                while dict34["customer_address"] == "0":
                    dict34["customer_address"] = ady_getter(dict34["customer_address"])

                    if dict34["customer_address"] == "£":
                        print('address wont be changed')
                    else:
                        print('address was changed')
                        orders_list[change_number]["customer_address"] = dict34["customer_address"]
        
                # customer phone 
                while dict34["customer_phone"] == '0':
                    dict34["customer_phone"] = phone_number_insert(dict34["customer_phone"])
                    if dict34["customer_phone"].replace(' ','') != '' and dict34["customer_phone"].replace(' ','').isdigit() == False:
                        print("please leave the field empty or insert 11 digits phone number")
                        dict34["customer_phone"] = '0'
             
                    elif dict34["customer_phone"].replace(' ','').isdigit() == True:
                        orders_list[change_number]["customer_phone"] = dict34["customer_phone"]
                    else:
                        print("phone number won't be changed")
                        break
                
                #courie
                enumerated_list(couriers_list)
                cory_switch = "£"

                while cory_switch == "£":
                    cory_switch = list_index_number2(cory_switch,couriers_list)
                    if type(cory_switch) != int:
                        print('courie wont be changed')
                        break
                    else:
                        orders_list[change_number]["courier"] = cory_switch
                        
                
                print('\n')
                print('please select from the following options')

                item_options = ['no change','add to items list','delete existing items list and start new one']


                item_change_choice = ''

                while item_change_choice not in ['0','1','3']:
                    print('please select from the following options')
                    print('\n')
                    enumerated_list(item_options)
                    print('\n')
                    print(orders_list[change_number])
                    item_change_choice = input('so whats your choice in regards to the items list?  ')

                    if item_change_choice == '0':
                        print('no change was added to the items list')
                        break

                        
                    elif item_change_choice == '1':
                        enumerated_list(products_list)
                        while bool(dict34['items']) == False:
                            dict34['items'] = item_filler(dict34['items'],products_list)
                            for items in dict34['items'] :
                                orders_list[change_number]['items'].append(items)
                        

                    elif item_change_choice == '2':
                        enumerated_list(products_list)
                        orders_list[change_number]['items'] = []
                        orders_list[change_number]['items'] = item_filler(dict34['items'],products_list)
                        print('items list deleted and new items list inserted')
                        break
                

                print("")
                user_input3 = ''
            
            
            elif user_input3 == '5':
                os.system('clear')
                enumerated_list(orders_list)

                del_choice = ''

                del_choice = list_index_number(del_choice, orders_list)

                orders_list.pop(del_choice)

                enumerated_list(orders_list)

                print('\n')

                user_input3 = ''

            
            
                


