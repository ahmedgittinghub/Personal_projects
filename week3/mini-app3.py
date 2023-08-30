from useful_packages3 import enumerated_list

from useful_packages3 import list_index_number
from useful_packages3 import name_insert
from useful_packages3 import delete_function
from useful_packages3 import file_closer
from useful_packages3 import file_opener
from useful_packages3 import ady_getter
import os
from useful_packages3 import phone_number_insert
from useful_packages3 import list_index_number2



products_list = []

couries_list = []
# ```txt
# LOAD products list from products.txt
file_opener("products.txt", products_list)
# LOAD couriers list from couriers.txt
file_opener("couries.txt", couries_list)




# CREATE orders list of dictionaries  
orders_list = [{
   "customer_name": "John",
   "customer_address": "Unit 1, 11 Main Street, LONDON, WH1 1ER",
   "customer_phone": "0789887331",
   "Courie": 7,
   "status": "preparing"
},
{
   "customer_name": "Erica",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH2 2ER",
   "customer_phone": "0789887332",
   "Courie": 6,
   "status": "starting"
},
{
   "customer_name": "Corrin",
   "customer_address": "Unit 3, 13 Main Street, LONDON, WH3 3ER",
   "customer_phone": "0789887333",
   "Courie": 5,
   "status": "preparing"
},
{
   "customer_name": "Ahmed",
   "customer_address": "Unit 4, 14 Main Street, LONDON, WH4 4ER",
   "customer_phone": "0789887334",
   "Courie": 4,
   "status": "completed"
},
{
   "customer_name": "Eugene",
   "customer_address": "Unit 5, 15 Main Street, LONDON, WH5 5ER",
   "customer_phone": "0789887335",
   "Courie": 7,
   "status": "preparing"}]

# CREATE order status list                
menu_options = [' Save & Exit app', 'Products Menu', 'Couriers Menu','Orders Menu']
order_status_list = ['starting','preparing','completed']




# GET user input for main menu option
user_input = ''
cafe_open = True
while  cafe_open == True and user_input not in ['0','1','2','3']:
    os.system('clear')
    enumerated_list(menu_options)

    user_input = input('please insert a number from 0,1,2,3: ')
    print('')

    if user_input == '0':
         #SAVE products list to products.txt
         #SAVE couriers list to couriers.txt
         #EXIT app
        file_closer("products.txt", products_list)
        file_closer("couries.txt", couries_list)
        cafe_open = False


    # ELSE IF user input is 1:
    elif user_input == '1':
        
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
                print('Going back to Main menu')
                open_menu = False
                user_input = ''
            #     ELSE IF user input is 1:

            elif user_input1 == '1':
                
                 # PRINT products list
                enumerated_list(products_list)
                
                user_input1 = ''
            
            elif user_input1 == '2':
                os.system('clear')
                
                new_product = '0'

                #GET user input for product name

                new_product = name_insert(new_product)

                #APPEND product name to products list
        
                products_list.append(new_product)
                enumerated_list(products_list)

                
                user_input1 = ''



            elif user_input1 == '3':
                #STRETCH GOAL - UPDATE existing produc

                os.system('clear')
                
                #PRINT product names with its index value
                enumerated_list(products_list)
                #GET user input for product index value
                product_index  = ''
                #GET user input for new product name
                switch_product = '0'

                product_index = list_index_number(product_index,products_list)


                switch_product = name_insert(switch_product)



                #UPDATE product name at index in products list
                products_list[product_index] = switch_product
                enumerated_list(products_list)
                user_input = '' 

                user_input1 = ''
                
            



            elif user_input1 == '4':
                os.system('clear')
                delete_product = ''
                #STRETCH GOAL - DELETE product
        
                #PRINT products list
                enumerated_list(products_list)

               #GET user input for product index value
                delete_product = list_index_number(delete_product,products_list)

                #DELETE product at index in products list
                delete_function(delete_product,products_list)

                enumerated_list(products_list)
                print(' ')
                print(' ')
               
                user_input1 = ''
            


    elif user_input == '2':
        
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
               
               open_couries_menu = False
            


            elif user_input2 == '1':
                #PRINT couriers list
                enumerated_list(couries_list)

                print(' ')
                print(' ')

                user_input2 = ''
            


            elif user_input2 == '2':
                 os.system('clear')
                 new_courie = '0'

                #GET user input for courie name

                 new_courie = name_insert(new_courie)

                #APPEND courie name to couries list
        
                 couries_list.append(new_courie)
                 enumerated_list(couries_list)

                 print(' ')
                 print(' ')

                 user_input2 = ''
                
            
            elif user_input2 == '3':
                os.system('clear')
                switch_courie_number = ''
                switch_courie = '0'
                
                #STRETCH GOAL - UPDATE existing couries
                
                #PRINT couries names with its index value
                enumerated_list(couries_list)
               #GET user input for couries index value
                switch_courie_number = list_index_number(switch_courie_number,couries_list)
                
                 
               #GET user input for new courie name
                switch_courie = name_insert(switch_courie)
               #UPDATE couries name at index in couries list
                couries_list[switch_courie_number] = switch_courie

                enumerated_list(couries_list)

                print(' ')
                print(' ')
                user_input2 = ''
                
            
            elif user_input2 == '4':
                os.system('clear')
                delete_courie_number = ''
                #STRETCH GOAL - DELETE courie
        
                #PRINT products courie
                enumerated_list(couries_list)

               #GET user input for product index value
                delete_courie_number = list_index_number(delete_courie_number,couries_list)

                #DELETE product at index in products list
                delete_function(delete_courie_number,couries_list)

                enumerated_list(couries_list)

                print(' ')
                print(' ')
               
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


             # ELSE IF user input is 1:
            elif user_input3 == '1':
                 #  PRINT orders dictionary
                enumerated_list(orders_list)

                print(' ')
                print(' ')

                user_input3 = ''



            # ELSE IF user input is 2:
            elif user_input3 == '2':
               os.system('clear')
               my_dict = {"customer_name": "0","customer_address": "0","customer_phone": "0","Courie": '' ,"status": "0"}

            # Customer_name
               while my_dict["customer_name"] == '0':
                 my_dict["customer_name"] = name_insert(my_dict["customer_name"])
                 if my_dict["customer_name"].replace(' ','').isalpha() == False:
                      my_dict["customer_name"] = '0'
                 else:
                     break
            
             # Customer address
        

               while my_dict["customer_address"] == '0':
                    my_dict["customer_address"] = ady_getter(my_dict["customer_address"])
                    if my_dict["customer_address"] == '£':
                        print("Please insert a valid input for the address.")
                        my_dict["customer_address"] = '0'
                    else:
                        print('thank you address inserted correctly')
                        break

            #Customer Phone Number 
               while my_dict["customer_phone"] == '0':
                my_dict["customer_phone"] = phone_number_insert(my_dict["customer_phone"])
                if my_dict["customer_phone"].replace(' ','').isdigit() == False:
                    my_dict["customer_phone"] = '0'
                else:
                    break
                       
             #GET user input for courier index to select courier
               print('now please choose a couries from the list below by typing in a index number')
               #PRINT couriers list with index value for each courier
               enumerated_list(couries_list)
                #GET user input for courier index to select courier
               cory_num = ''
               cory_num = list_index_number(cory_num,couries_list)
               my_dict['Courie'] = couries_list[cory_num]


               #SET order status to be 'PREPARING'         
               my_dict["status"] = "preparing"
                #APPEND order to orders list
               orders_list.append(my_dict)
               enumerated_list(orders_list)
               user_input3 = ''

            # ELSE IF user input is 3:
            elif user_input3 == '3':
                os.system('clear')

                 #     PRINT orders list with its index values
                
                enumerated_list(orders_list)
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

                user_input3 = ''
            

            elif user_input3 == '4':
                os.system('clear')
                
                enumerated_list(orders_list)

                change_number = ''
 
                print('please insert the number of the order u wish to change')

                change_number = list_index_number(change_number,orders_list)

                my_dict2 = {"customer_name": "0","customer_address": "0","customer_phone": "0","courie": ""}

                print(" ")

          

                #customer name
                while my_dict2["customer_name"] == '0':
                    my_dict2["customer_name"] = name_insert(my_dict2["customer_name"])
                if my_dict2["customer_name"].strip() == '' :
                    print('no name was inserted, name wont be changed')
                elif my_dict2["customer_name"].replace(' ','').isalpha() == True:
                    orders_list[change_number]["customer_name"] = my_dict2["customer_name"]
                else:
                    print('insert a valid input or leaveit empty ')
               
                # customer address
                while my_dict2["customer_address"] == "0":
                    my_dict2["customer_address"] = ady_getter(my_dict2["customer_address"])

                if my_dict2["customer_address"] == "£":
                    print('address wont be changed')
                else:
                    print('address was changed')
                    orders_list[change_number]["customer_address"] = my_dict2["customer_address"]
        
                # customer phone 
                while my_dict2["customer_phone"] == '0':
                    my_dict2["customer_phone"] = phone_number_insert(my_dict2["customer_phone"])
                    if my_dict2["customer_phone"].replace(' ','') != '' and my_dict2["customer_phone"].replace(' ','').isdigit() == False:
                        print("please leave the field empty or insert 11 digits phone number")
                        my_dict2["customer_phone"] = '0'
             
                    elif my_dict2["customer_phone"].replace(' ','').isdigit() == True:
                        orders_list[change_number]["customer_phone"] = my_dict2["customer_phone"]
                    else:
                        print("phone number won't be changed")
                        break


                #courie
                enumerated_list(couries_list)
                cory_switch = "£"

                while cory_switch == "£":
                    cory_switch = list_index_number2(cory_switch,couries_list)
                    if type(cory_switch) != int:
                        print('courie wont be changed')
                        break
                    else:
                        orders_list[change_number]["Courie"] = cory_switch
                   
        
        
                enumerated_list(orders_list)
                print("")
                user_input3 = ''
            
            elif user_input3 == '5':
                os.system('clear')
                #PRINT orders list
                enumerated_list(orders_list)
                #GET user input for order index value
                del_choice = ''

                del_choice = list_index_number(del_choice, orders_list)

                 #DELETE order at index in order list
                orders_list.pop(del_choice)
                 
                enumerated_list(orders_list)

                print('')

                user_input3 = ''



                

        
    
        

        
    
   
   



   
                    
    
    
   
    
            
            

         
        
      
      

        

        


                
                

           
            
            
            
            


        
        

        
        














    





