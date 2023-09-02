from useful_packages5 import * 
from sql_packages import * 

import pymysql
import os
from dotenv import load_dotenv

connection, cursor = setup_db_connection()




# LOAD orders from orders.csv
orders_list = []
open_csv_orders('orders.csv',orders_list)

# CREATE order status list
order_status_list = ['starting','preparing','completed']


# PRINT main menu options
menu_options = [' Save & Exit app', 'Products Menu', 'Couriers Menu','Orders Menu']
# GET user input for main menu option
user_input = ''
cafe_open = True
while  cafe_open == True and user_input not in ['0','1','2','3']:
    enumerated_list(menu_options)

    user_input = input('please insert a number from 0,1,2,3: ')
    print('')
# IF user input is 0:
    if user_input == '0':
        #  SAVE orders list to order.csv
         close_csv_orders('orders.csv', orders_list)
        #  EXIT app
         os.system('clear')
         cafe_open = False


# # products menu
# ELSE IF user input is 1:
    elif user_input == '1':
        open_menu = True
        #PRINT product menu options
        menu_options1 = ['Return to main menu','Print product list','Create a new product','Update existing product','Delete existing product']
        enumerated_list(menu_options)
        user_input1 = ''
        os.system('clear')
        print('welcome to the products menu')
        print('\n')
    
#     GET user input for product menu option
        while  open_menu == True and user_input1 not in ['0','1','2','3','4']:
            
            enumerated_list(menu_options1)
            user_input1 = input('please insert a choice from 0,1,2,3,4:  ')

#     IF user inputs 0:
            if user_input1 == '0':
               #RETURN to main menu
                
                user_input = ''
                open_menu = False
                os.system('clear')
                print('Going back to Main menu')

#     # WEEK 5 UPDATE
#     ELSE IF user input is 1:
            elif user_input1 == '1':
                 print('\n')
                 os.system('clear')
                 # PRINT products list
                 table_printer(table_name='products')
                 
                 user_input1 = ''


#     # WEEK 5 UPDATE
#     ELSE IF user input is 2:
            elif user_input1 == '2':
                 os.system('clear')
                 check_name = ''

                 dict1 = {"product_name": "0", "product_price": "0"}
                 table_printer(table_name='products')

                # GET user input for product name
                 while dict1["product_name"] == "0" :
                    # here user is asked for name insert
                    dict1["product_name"] = name_insert(dict1["product_name"])
                    # resets if left empty, so a name is inserted for the product
                    if dict1["product_name"].strip() == '':
                        dict1["product_name"] = "0"
                    else:
                        #  check to ensure the new product being added isnt a duplicate
                        check_name = product_name_check(dict1["product_name"], check_name)
                        #  resets if product name already exist
                        if check_name == 'yes':
                            dict1['product_name'] = '0'
                        #  doesnt reset if product name exists
                        elif check_name == 'no':
                            break
                 

                 
                # GET user input for product price
                 while dict1["product_price"] == "0" :
                    dict1["product_price"] = price_insert(dict1["product_price"])
                    # price must be a float value, so that the field is not left empty
                    if type(dict1["product_price"]) != float:
                        dict1["product_price"] = "0"
                        print('please insert a valid input for price')
                    else:
                        # once a name and a price are obtained the new product is added 
                        add_product(dict1["product_name"], dict1["product_price"])
                
                 user_input1 = ''



#     # WEEK 5 UPDATE
#     ELSE IF user input is 3:
            elif user_input1 == '3':
                os.system('clear')

                dict13 = {"product_name": "0", "product_price": "0"}
                #PRINT products with their IDs
                table_printer(table_name = 'products')
                
                id_number = '$'
                checker = ''
                name_checker = ''
                #GET user input for product ID
               
                while id_number == '$' :
                    id_number , checker = id_number_check_products_table(id_number,checker)
                    # if user id doesnt exist the loop will resets and ask for id insert
                    if checker == 'no':
                        id_number = '$'

                # if the insert is left empty the code ends as the user doesnt desire to change anything
                if checker == 'no change':
                    print('No change desired going back to main menu')
                    
                # this if stament is activated when a correct courier ID is inserted
                elif checker == 'yes':
                    print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')

                    #GET user input for product name
                    while dict13["product_name"] == "0":
                        # the user is asked for a new product name to alter existing product
                        dict13["product_name"] = name_insert(dict13["product_name"])

                        #if name insert is left empty no name taken and product name will be left the same
                        if dict13["product_name"].strip() == '':
                            print("product will not be changed")
                            break

                        #if the name insert is not left empty this elif statment is activated
                        elif dict13["product_name"].strip() != '':
                            name_checker = product_name_check(dict13["product_name"], name_checker)
                            # this checks if the product name already exists
                            if name_checker == 'yes':
                                # if the name is in the products table, name insert resets
                                dict13['product_name'] = '0'
                                # if the name doesnt exist product name is updated
                            elif name_checker == 'no':
                                product_name_change(id_number,dict13['product_name'])


                    #GET user input for product price
                    while dict13["product_price"] == "0":
                        # the users are asked for a price 
                        dict13["product_price"] = price_insert(dict13["product_price"])

                        # if the price is inserted correctly in float form the price of the product is updated
                        if type(dict13["product_price"]) == float :
                            product_price_change(id_number,dict13['product_price'])
                            break
                    #IF any inputs are empty, do not update them
                        elif dict13["product_price"].strip() == '':
                            print("product price will not be changed")
                            break
                        #IF input is incorrect sush as letters the code will reset and ask user for price
                        elif dict13["product_price"].strip() != '' and type(dict13["product_price"]) != float:
                            print('please insert a vlid input for the price ')
                            dict13["product_price"] == "0"

                user_input1 = ''
            


#     # WEEK 5 UPDATE
#     ELSE IF user input is 4:
            elif user_input1 == '4':
                os.system('clear')
                #PRINT products with their IDs
                table_printer(table_name='products')
                id_number = '$'
                checker = ''
                #GET user input for product ID
                while id_number == '$' :
                    id_number , checker = id_number_check_products_table(id_number,checker)
                    if checker == 'no':
                        id_number = '$'

                # If no Id is inserted no product is deleted 
                if checker == 'no change':
                    print('NO ENTRY WAS TAKEN GOING BACK TO MAIN MENU')
                    
                elif checker == 'yes':
                    # DELETE product in products table
                    delete_product(id_number)               
                user_input1 = ''
#         # STRETCH GOAL - DELETE product
        





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
                #GET all couriers from couriers table
                #PRINT couriers
                print('\n')
                os.system('clear')
                table_printer(table_name='couriers')
                
                user_input2 = ''

            # CREATE new courier
            elif user_input2 == '2':
                os.system('clear')
                dict22 = {"name": "0","phone_number":"0"}
                checker = ''

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
                        checker = courier_phone_check(dict22['phone_number'],checker)
                        if checker == 'yes':
                            dict22['phone_number'] = '0'
                        elif checker == 'no':
                            #INSERT courier into couriers table  
                            add_courier(dict22['name'],dict22['phone_number'])
                            break
                 
                user_input2 = ''  

            elif user_input2 == '3':
                dict23 = {"name": "0","phone_number":"0"}
                os.system('clear')
                id_number = '$'
                checker = ''
                phone_number_checker = '' 

                table_printer(table_name='couriers')

                #GET user input for courier ID
                # retrieve courier Id then check if the ID number exists
                while id_number == '$' :
                    id_number , checker = id_number_check_couriers_table(id_number,checker)
                    #  if the Id inserted doesnt exist loop resets and ask for a another insert
                    if checker == 'no':
                        id_number = '$'
                # if no insert is added code breaks and goes back to main menu
                if checker == 'no change':
                    print('No change desired going back to main menu')
                    

                elif checker == 'yes':
                    print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')
                    
                    #GET user input for courier name
                    while dict23['name'] == "0":
                        dict23["name"] = name_insert(dict23["product_name"])
                        # if the user left the insert empty name doesnt change
                        if dict23["name"].strip() == '':
                            print("product will not be changed")
                            break
                        elif dict23["name"].strip() != '':
                            # ensures names are inserted in the correct format
                            if dict23['name'].replace(' ','').isalpha() == False:
                                print('Please insert a valid name with just letters')
                                # resets if incorrect input is added
                                dict23['name'] = '0'
                            else: 
                                print('Name will be changed')
                                #Courier name update
                                courier_name_change(id_number,dict23['name'])

                    
                    #GET user input for courier phone number
                    while dict23['phone_number'] == "0":
                        dict23['phone_number'] = phone_number_insert(dict23['phone_number'])
                        if dict23["phone_number"].strip() == '':
                            print("Phone Number will not be changed")
                            break
                        elif dict23["phone_number"].strip() != '':
                            # function checks if the phone number exists
                            phone_number_checker = courier_phone_check(dict23['phone_number'], phone_number_checker)
                            if phone_number_checker == 'yes':
                                # this ensures users don't insert a phone number already in the database
                                dict23["phone_number"] = '0'
                            elif phone_number_checker == 'no':
                                # command that alters the phone number
                                phone_number_change(id_number, dict23['phone_number'])

                
                user_input2 = ''       

                
                






            elif user_input2 == '4':
                os.system('clear')
                #PRINT products with their IDs
                table_printer(table_name='couriers')
                id_number = '$'
                checker = ''
                #GET user input for product ID
                while id_number == '$' :
                    # if id number inserted doesnt exist or input is incorrect the insert resets
                    id_number , checker = id_number_check_products_table(id_number,checker)
                    if checker == 'no':
                        id_number = '$'
                
                # if no id inserted, code breaks .
                if checker == 'no change':
                    print('NO ENTRY WAS TAKEN GOING BACK TO MAIN MENU')
                    
                elif checker == 'yes':
                    # DELETE courier with the id 
                    delete_courier(id_number)               
                

                user_input2 = ''   








# # orders menu
# ELSE IF user input is 3:
#     PRINT order menu options
#     GET user input for order menu option

#     IF user input is 0:
#         RETURN to main menu

#     ELSE IF user input is 1:
#         PRINT orders dictionary

#     ELSE IF user input is 2:
#         GET user input for customer name
#         GET user input for customer address
#         GET user input for customer phone number

#         # WEEK 5 UPDATE
#         GET all products from products table
#         PRINT products
#         GET user inputs for comma-separated list of product IDs
#         CONVERT above user input to a string e.g. "2,1,3"

#         # WEEK 5 UPDATE
#         GET all couriers from couriers table
#         PRINT couriers
#         GET user input for courier ID

#         SET order status to be 'PREPARING'

#         CREATE new order dictionary with above properties
#         APPEND order to orders list

#     ELSE IF user input is 3:
#         # UPDATE existing order status

#         PRINT orders list with its index values
#         GET user input for order index value

#         PRINT order status list with index values
#         GET user input for order status index value
#         UPDATE status for order

#     ELSE IF user input is 4:
#         # STRETCH - UPDATE existing order

#         PRINT orders list with its index values
#         GET user input for order index value

#         FOR EACH key-value pair in selected order dictionary:
#             GET user input for updated property
#             IF user input is blank:
#                 do not update this property
#             ELSE:
#                 update the property value with user input

#     ELSE IF user input is 5:
#         # STRETCH GOAL - DELETE order
                    
#         PRINT orders list
#         GET user input for order index value
#         DELETE order at index in order list
# ```















































