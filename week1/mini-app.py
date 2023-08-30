from useful_packages import list_index_number
from useful_packages import enumerated_list
from useful_packages import delete_function
from useful_packages import name_insert




# add some product names
#CREATE products list
product_list = ['pepsi','coke','fanta']

#PRINT main menu options
menu_options = ['Exit',' View Products',' Add new product',' Update existing product',' delete product']



#GET user input for main menu option
user_input = ''

open_cafe = True 

while  open_cafe == True and user_input not in ['0','1','2','3','4']:
    enumerated_list(menu_options)
    
    user_input = input('please give me a number from 0-4: ')

    #IF user input is 0:
    #EXIT app
    if user_input == '0':
    
        open_cafe = False


# products menu
#ELSE IF user input is 1:
    elif user_input == '1':
        
        enumerated_list(product_list)
        user_input = ''


    elif user_input == '2':
        
        new_product = ''

        new_product = name_insert(new_product)
        
        product_list.append(new_product)
        enumerated_list(product_list)
        user_input = ''



        
    elif user_input == '3':
        enumerated_list(product_list)

        product_index  = ''
        switch_product = ''

        product_index = list_index_number(product_index,product_list)

        switch_product = name_insert(switch_product)


    
        product_list[product_index] = switch_product
        enumerated_list(product_list)
        user_input = ''
    
        

    elif user_input == '4':
        enumerated_list(product_list)
        del_choice = ''


        del_choice = list_index_number(del_choice,product_list)

        delete_function(del_choice,product_list)

        enumerated_list(product_list)



        user_input = ''


        
