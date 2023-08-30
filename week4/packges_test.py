def phone_number_insert1(phone):
    if len(phone.strip()) != 0:
        if phone.isdigit() == False or len(phone.strip()) != 11 :
            print('invalid input, please ensure you insert the right phone number')
            phone = '0'

        else:
            print('valid phone number')
            phone = '079'
    else:
        phone = 'empty'
    
    return phone  
         
         
              



def list_index_number2(k, listname):
    try:
         k = int(k)       
    except ValueError:
            print('Please insert a valid input.')
            k = 'ValueError'
            
    else:
            print('Well done, that\'s great!')

    if type(k) == int and k > len(listname):
            print('please insert a lower number ')
            k = 'number too high'
    elif type(k) == int and k == len(listname):
            print('please insert a lower number ')
            k = 'lower number please'
    elif type(k) != int :
         print(k)
    else:
          print(listname[k])
              
    return k

        
