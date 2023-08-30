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

        if type(k) != int or k > len(listname) :
            print('please insert a valid number thats within the order list')
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
                else:
                    print('number inserted is valid')
                    break
    
    return k  
    
    


   
