def name_insert(name):
    while name == '0':
         name = input("Please insert the name of the order: ")
    return name

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
    print('all done')
    

        

    
