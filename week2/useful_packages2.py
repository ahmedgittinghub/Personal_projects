def name_insert(name):
    while name == '0':
         name = input("Please insert the name of the order: ")
    return name

def phone_number_insert(phone):
         
         
         while phone ==  '0' :
            phone = input('please insert a phone number with 11 digits or leave blank by pressing enter ')
            if len(phone.strip()) != 0:
                if phone.isdigit() == False or len(phone.strip()) < 11 :
                    print('invalid input, please ensure you insert the right phone number')
                    phone = '0'
                else:
                    break
            else:
                break
    
         return phone
                
                 
                
            
                   
            
   
                
            
              
    
def open_file(filename,file_mode):
    f = open(filename,file_mode)
    print('file opened')
    return f




 

  

def list_to_file(listname,filevariable):
        
        for items in listname:
            # write each item on a new line
            filevariable.write(items + '\n')
        filevariable.close()
        print('All done, files closed')
        return ''
        
        






def enumerated_list(listname):
    for index,items in enumerate(listname):
        print(index,items)
        
        










def list_index_number(k, listname):
    while type(k) != int or k > len(listname):
        try:
            k = int(input('Please insert a number of the item you wish to change/delete: '))
        except ValueError:
            print('That\'s not a number!')
        else:
            print('Well done, that\'s great!') 
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


  




    
