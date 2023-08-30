from useful_packages5 import * 

import os

orders_list = []
products_list = []
couriers_list = []

# LOAD orders from orders.csv
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
        os.system('clear')
        print('welcome to the products menu')
        open_menu = True
        #PRINT product menu options
        menu_options1 = ['Return to main menu','Print product list','Create a new product','Update existing product','Delete existing product']
        enumerated_list(menu_options)
        user_input1 = ''
    
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
                 os.system('clear')
                 # PRINT products list
                 print('1 ,1')
                 print('\n')
               
            
                 user_input1 = ''
#         GET all products from products table
#         PRINT products

#     # WEEK 5 UPDATE
#     ELSE IF user input is 2:
            elif user_input1 == '2':
                os.system('clear')
                print('1,2')                
                user_input1 = ''
#         # CREATE new product

#         GET user input for product name
#         GET user input for product price
#         INSERT product into products table

#     # WEEK 5 UPDATE
#     ELSE IF user input is 3:
            elif user_input1 == '3':
                os.system('clear')
                print('1,3')                
                user_input1 = ''


#         # STRETCH GOAL - UPDATE existing product
            

#         GET all products from products table
#         PRINT products with their IDs
#         GET user input for product ID

#         GET user input for product name
#         GET user input for product price

#         IF any inputs are empty, do not update them
#         UPDATE properties for product in product table

#     # WEEK 5 UPDATE
#     ELSE IF user input is 4:
            elif user_input1 == '4':
                os.system('clear')
                print('1,4')                
                user_input1 = ''
#         # STRETCH GOAL - DELETE product
        
#         GET all products from products table
#         PRINT products with their IDs

#         GET user input for product ID
#         DELETE product in products table
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
                print('2,1')  
                user_input2 = ''
                #     ELIF user inputs 1:
#         GET all couriers from couriers table
#         PRINT couriers

            elif user_input2 == '2':
                os.system('clear')
                print('2,1')  
                user_input2 = ''  
#     ELSE IF user input is 2:
#         # CREATE new courier

#         GET user input for courier name
#         GET user input for courier phone number
#         INSERT courier into couriers table   

            elif user_input2 == '3':
                os.system('clear')
                print('2,3')
                user_input2 = ''       
#     ELSE IF user input is 3: 
#         # STRETCH GOAL - UPDATE existing courier

#         GET all couriers from couriers table
#         PRINT couriers with their IDs
#         GET user input for courier ID

#         GET user input for courier name
#         GET user input for courier phone number

#         IF an input is empty, do not update its respective table property
#         UPDATE properties for courier in courier table

            elif user_input2 == '4':
                os.system('clear')
                print('2,4')
                user_input2 = ''   
#     ELSE IF user input is 4:
#         # STRETCH GOAL - DELETE courier
                
#         GET all couriers from couriers table
#         PRINT courier with their IDs

#         GET user input for courier ID
#         DELETE courier in couriers table







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















































