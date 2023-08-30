
from useful_packages import enumerated_list 
from useful_packages import list_index_number

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

     elif user_input2 == '1':
     
        enumerated_list(orders_list)
        user_input2 = ''

     elif user_input2 == '2':
        my_dict = {"customer_name": "0","customer_address": "0","customer_phone": "0","status": "0"}

        #customer name
        while my_dict["customer_name"] == "0" or my_dict["customer_name"].strip() == '' :
            my_dict["customer_name"] = input("Please insert the name of the order ")

        # customer address
        while my_dict["customer_address"] == "0" or my_dict["customer_name"].strip() == '':
    
            unit_number = 0
            address_street = 0
            address_city = 0
            address_postcode1 = 0
            address_postcode2 = 0
    
    
        
            while unit_number == 0 or unit_number.strip() == '':
                
                unit_number = input('please give me your Unit Number ').title().strip()
                    
            while address_street == 0 or address_street.strip() == '':
                address_street = input('Please insert your street address ').title().strip()
                
            while address_city == 0 or address_city.strip() == '':
                address_city = input('please insert your city ').capitalize().strip()
                
            while address_postcode1 == 0:
                
                address_postcode1 = input('please insert your 1STpostcode ').capitalize().strip()
                if len(address_postcode1) < 2 or len(address_postcode1) > 4:
                    address_postcode1 = 0
                    
            while address_postcode2 == 0:
                address_postcode2 = input('please insert your 2NDpostcode ').capitalize().strip()
                if len(address_postcode2) != 3:
                    address_postcode2 = 0
            
            
            my_dict["customer_address"]= f'{unit_number}, {address_street}, {address_city}, {address_postcode1} {address_postcode2}'
            
        while my_dict["customer_phone"] ==  "0" or my_dict["customer_phone"].strip() == '':
            print('please insert a phone number with 11 digits')
        
            my_dict["customer_phone"] = input('please insert your phone number  ')
            
            if my_dict["customer_phone"].isdigit == False or len(my_dict["customer_phone"]) < 11 :
                print('invalid input, please ensure you insert the right phone number')
                my_dict["customer_phone"] = "0"

        

        my_dict["status"] = "preparing"
        user_input2 = ''

        orders_list.append(my_dict)
        print(orders_list)
    
     elif user_input2 == '3':

        enumerated_list(orders_list)
        switch_number = ''
        switch_number = list_index_number(switch_number,orders_list)
        change_status = ''
        while change_status not in ['starting','preparing','completed']:
            change_status = input('please input from the following conditions: starting, preparing, completed: ').lower()
    
        orders_list[switch_number]['order_status'] = change_status
        enumerated_list(orders_list)
        user_input2 = ''

     elif user_input2 == '4':

         enumerated_list(orders_list)

         change_number = ''

         print('please insert the number of the order u wish to change')

         change_number = list_index_number(change_number,orders_list)

         my_dict2 = {"customer_name": "0","customer_address": "0","customer_phone": "0"}

          

        #customer name
         while my_dict2["customer_name"] == "0":
            print("if you insert a number it will not be taken")
            my_dict2["customer_name"] = input("Please insert the name of the order or leave empty ")
            if my_dict2["customer_name"].isalpha() == True:
                orders_list[change_number]["customer_name"] = my_dict2["customer_name"]
            else:
                print("name was not changed")

            

        # customer address
         while my_dict2["customer_address"] == "0" :
    
            unit_number = 0
            address_street = 0
            address_city = 0
            address_postcode1 = 0
            address_postcode2 = 0
    
    
        
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
            
            emptyy = ''

            if unit_number.strip() != emptyy and address_street.strip() != emptyy and address_city.strip() != emptyy and address_postcode1.strip() != emptyy and  address_postcode2.strip() != emptyy:
                 print("address will be changed")
                 my_dict2["customer_address"]= f'{unit_number}, {address_street}, {address_city}, {address_postcode1} {address_postcode2}'
                 orders_list[change_number]["customer_address"] = my_dict2["customer_address"]

                 
                 
            
            elif unit_number.strip() == emptyy and address_street.strip() == emptyy and address_city.strip() == emptyy and address_postcode1.strip() == emptyy and address_postcode2.strip() == emptyy:
                print("nothing will be changed")
                break
            
            else:
                unit_number = 0
                address_street = 0
                address_city = 0
                address_postcode1 = 0
                address_postcode2 = 0

                
            
            

           

            
            
            
            
         while my_dict2["customer_phone"] ==  '0' :
            my_dict2["customer_phone"] = input('please insert a phone number with 11 digits or leave blank by pressing enter')
            if len(my_dict2["customer_phone"]) != 0:
                 if my_dict2["customer_phone"].isdigit == False or len(my_dict2["customer_phone"]) < 11 :
                    print('invalid input, please ensure you insert the right phone number')
                    my_dict2["customer_phone"] = 0
                 else:
                     print('phone number changed')
                     orders_list[change_number]["customer_phone"] = my_dict2["customer_phone"]
        

         enumerated_list(orders_list)
         user_input2 = ''
            
        
            
        

        


         
         

            
     
        
         
        
        
         
        
       
    
     elif user_input2 == '5':

        enumerated_list(orders_list)
        del_choice = ''
        del_choice = list_index_number(del_choice, orders_list)

        orders_list.pop(del_choice)

        enumerated_list(orders_list)
        user_input2 = ''


# print
            
        


            
        
       



        
        

        

    
        

        

            
     
        


#         # STRETCH GOAL - DELETE order
                    
#         PRINT orders list
#         GET user input for order index value
#         DELETE order at index in order list
