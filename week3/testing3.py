def open_file(filename,file_mode,list_of_data):
    f = open(filename,file_mode)
    lines = f.readlines()
    for line in lines:
          list_of_data

    print('file opened')
    return f



products = ['vodka']


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


file_opener("products.txt", products)

print(products) 


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


file_closer("products.txt", products)
