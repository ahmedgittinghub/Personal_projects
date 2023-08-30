from useful_packages2 import ady_getter
from useful_packages2 import name_insert
from useful_packages2 import phone_number_insert
from useful_packages2 import enumerated_list
from useful_packages2 import list_index_number
import os



menu2_options = ['Main Menu',' View Orders Dictionary','New order Input',' Update existing order status','update existing order details',' delete product']








orders_list = [{
   "customer_name": "John",
   "customer_address": "Unit 1, 11 Main Street, LONDON, WH1 1ER",
   "customer_phone": "0789887331",
   "status": "preparing"
},
{
   "customer_name": "Erica",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH2 2ER",
   "customer_phone": "0789887332",
   "status": "starting"
},
{
   "customer_name": "Corrin",
   "customer_address": "Unit 3, 13 Main Street, LONDON, WH3 3ER",
   "customer_phone": "0789887333",
   "status": "preparing"
},
{
   "customer_name": "Ahmed",
   "customer_address": "Unit 4, 14 Main Street, LONDON, WH4 4ER",
   "customer_phone": "0789887334",
   "status": "completed"
},
{
   "customer_name": "Eugene",
   "customer_address": "Unit 5, 15 Main Street, LONDON, WH5 5ER",
   "customer_phone": "0789887335",
   "status": "preparing"
}]

orders_menu_status = True

user_input2 = ''

while  orders_menu_status == True and user_input2 not in ['0','1','2','3','4','5']:
     
     
     
     print(enumerated_list(menu2_options))
    
     user_input2 = input('please give me a number from 0-5: ')
     if user_input2 == '0':
           orders_menu_status == False
           os.system('clear')

     elif user_input2 == '1':
     
        enumerated_list(orders_list)
        print('')
        user_input2 = ''

     elif user_input2 == '2':
        os.system('clear')
        my_dict = {"customer_name": "0","customer_address": "0","customer_phone": "0","status": "0"}
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
        
           
        my_dict["status"] = "preparing"

        orders_list.append(my_dict)
        enumerated_list(orders_list)
        user_input2 = ''

    
     elif user_input2 == '3':
        os.system('clear')

        enumerated_list(orders_list)
        switch_number = ''
        switch_number = list_index_number(switch_number,orders_list)
        change_status = ''
        while change_status not in ['starting','preparing','completed']:
            change_status = input('please input from the following conditions: starting, preparing, completed ').lower()
    
        orders_list[switch_number]['order_status'] = change_status
        enumerated_list(orders_list)

        user_input2 = ''


     elif user_input2 == '4':
         os.system('clear')
         enumerated_list(orders_list)

         change_number = ''

         print('please insert the number of the order u wish to change')

         change_number = list_index_number(change_number,orders_list)

         my_dict2 = {"customer_name": "0","customer_address": "0","customer_phone": "0"}

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
                   
        
        
         enumerated_list(orders_list)
         print("")
         user_input2 = ''

            
     elif user_input2 == '5':
        os.system('clear')

        enumerated_list(orders_list)

        del_choice = ''

        del_choice = list_index_number(del_choice, orders_list)

        orders_list.pop(del_choice)

        enumerated_list(orders_list)

        print('')

        user_input2 = ''