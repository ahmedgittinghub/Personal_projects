import csv
from collections import Counter
from datetime import datetime
import copy
import uuid

# ======================================================================================================================================================================
#VARIABLES:
# 1) data = extracted raw data from CSV file. 
# This lists: PURCHASE DATE, BRANCH, CUSTOMER NAME, ITEMS, TOTAL, METHOD OF PAYMENT, CARD NO. - key names may not correspond. Be careful!

# 2) reformatted_data = data reformatted to have products in a list of their own inside the dictionaries
# This lists: PURCHASE DATE, BRANCH, CUSTOMER NAME, ITEMS (reformatted), TOTAL, METHOD OF PAYMENT, CARD NO. - key names may not correspond. Be careful!

# 3) reformatted_cleaned_data= reformatted data and cleaned of customer information. 
# This lists: PURCHASE DATE, BRANCH, ITEMS, TOTAL, METHOD OF PAYMENT - key names may not correspond. Be careful!

# 4) sorted_final_products_table_with_branches_reassigned = sorted into alphabetical order and given corresponding product id list of unique products
# This lists: product name, product price, product i.d, number of times product is ordered in total??

# 5) payment_table = list of payment methods
# This lists: payment_id, payment_method

# 6) branches_list = list of branches enumerated
# This lists: branch_id, branch_name

# 7) big_table = list of main elements for Main table but with branch name instead of branch id
# This lists: transaction_id, transaction date + time, method of payment, order id, products ordered, total, branch name


# 8) big_table_with_branch_id = list of main elements for Main table
# This lists: transaction_id, transaction date + time, method of payment, order id, products ordered, total, branch id


# 9)big_table_total_prods = list of main elements for Main table but with total products not indv quantities
#  This lists: transaction_id, transaction date + time, method of payment, order id, total products ordered, total, branch name
# need to fix!

# 10) orders_table_list = list of main elements for orders table
# This lists: transaction id, product, quantity 
# ======================================================================================================================================================================

def enumerated_list(listname): #Gives enumerated list of objects (can be used to find products uniquely)
    for index,items in enumerate(listname):
        print(f'Index: {index}. {items}')
        print()

def guid_reassigner(list_to_change, key_to_change):
    for data in list_to_change:
        new_guid_id_value = str(uuid.uuid4())
        data[key_to_change] = new_guid_id_value
    return list_to_change

def extract_sales_data(file_name, list_name): #Extracts data from CSV file but does not clean it
    try:
        with open(file_name, 'r') as file:
            source_file = csv.DictReader(file, fieldnames=['purchase_date', 'branch', 'customer_name', 'items', 'total', 'mode_of_payment', 'cardnumber'], delimiter=',')
            for row in source_file:#the following lines correct the date format so it can be uploaded to a database later
                date_str = row["purchase_date"]
                datetime_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
                row["purchase_date"] = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
                list_name.append(row)
    except Exception as error:
        print("An error occurred: " + str(error))
    return list_name


data = []
data = extract_sales_data('chesterfield_13-08-2023_09-00-00.csv',data)


def separate_items_into_list_within_a_list(list_name1,col_name):
    for d in list_name1:
        if col_name not in d:
            print('The column name inserted is not in the list inserted, please insert a valid input')
            list_name1 = 1
            break
        else:
            d[col_name] = d[col_name].split(",")
    return list_name1


reformatted_data = separate_items_into_list_within_a_list(data,'items') #data extracted is now in form A list of dictionaries with the items field as a list aswell


def coloumn_deleter(list_name, coloumn_name): #removes sensitive data
    for items in list_name:
        if coloumn_name in items:
            del items[coloumn_name]
    return list_name

reformatted_cleaned_data = coloumn_deleter(reformatted_data,'cardnumber') #removes card number field from data
reformatted_cleaned_data = coloumn_deleter(reformatted_cleaned_data,'customer_name') #removes customer name field from data


#THIS DATA LIST IS THE FINAL ONE WE WILL USE- reformatted_cleaned_data
# ====================================================================================================================================


def branch_list(data): #Creates an enumerated dictionary of branches 
    branches= []
    correct= []
    for x in data:
        y= x["branch"]
        if y not in branches:
            branches.append(y)
    count = 1
    for z in branches:
        ok = {"branch_id": count, "branch": z}
        correct.append(ok)
        count += 1
    return correct

branches_list = branch_list(reformatted_cleaned_data)
branches_list = guid_reassigner(branches_list, "branch_id")


def branch_id_reassigner(list_to_change,list_to_search):
    new_list=[]
    for li in list_to_change:#creates a new list so big_table isnt changed
        d2 = copy.deepcopy(li)
        new_list.append(d2)
    for d in new_list:  # changes the branch name value to its branch id value
        search_value = d["branch"]
        next_list = next(item for item in list_to_search if item["branch"] == search_value)
        id = next_list["branch_id"]
        d["branch"] = id 
    for e in new_list: #changes key "branch name"  to be "branch id" in this new list
        e["branch_id"] = e.pop("branch")
    return new_list

def payment_id_reassigner(list_to_change,list_to_reference):#changes information in list_to_change depending on what is in list_to_reference
    for d in list_to_change:  
        search_value = d["method_of_payment"]
        next_list = next(item for item in list_to_reference if item["payment_method"] == search_value)
        id = next_list["payment_id"]
        d["method_of_payment"] = id 

    return list_to_change

def form_initial_products_list(list_name1, list_name2):
    data_dict = {'product_name': '', 'product_price': '', 'product_id': '', 'number_of_product_ordered': 0, 'branch':''}
    list101 = []
    for d in list_name1:
        if 'items' not in d:
            print('The list inserted doesn\'t have an "items" column to work with')
            list101 = 1
            break
        for item in d['items']:
            if '-' not in item:  # Fixed this line
                print('The data source you inserted is in an invalid format. There are no commas!')
                list101 = 2
                break
            else:
                m = item.split("-")
                if len(m) == 2:
                    data_dict['product_name'] = m[0].rstrip().lstrip()
                    try:
                        data_dict['product_price'] = float(m[1])
                    except ValueError:
                        print('Price is invalid')
                        list101 = 3
                        break
                    data_dict['product_id'] = len(list101) + 1
                    data_dict["branch"] = d["branch"]
                    list101.append(data_dict)  # Use copy() to create a new dictionary
                    data_dict = {'product_name': '', 'product_price': '', 'product_id': '', 'number_of_product_ordered': 0, 'branch':''}
                elif len(m) == 3:
                    data_dict['product_name'] = m[0].rstrip().lstrip() + ' ' + m[1].rstrip().lstrip()
                    try:
                        data_dict['product_price'] = float(m[2])
                    except ValueError:
                        print('Price is invalid')
                        list101 = 3
                        break
                    data_dict['product_id'] = len(list101) + 1
                    data_dict["branch"] = d["branch"]
                    list101.append(data_dict)  # Use copy() to create a new dictionary
                    data_dict = {'product_name': '', 'product_price': '', 'product_id': '', 'number_of_product_ordered': 0, 'branch':''}
                elif len(m) > 3:
                    print('The software isn\'t accustomed to work with this format')
                    list101 = 4
                    break
    list_name2 = list101  # Add processed data to list_name2
    return list_name2

products_table = [] #create an empty list
initial_products_table = form_initial_products_list(reformatted_cleaned_data,products_table) #fill empty products table with just the product: name, price, id and soon number ordered 

def drop_duplicate(list_name,list_name2,col_name): #will remove duplicates of each product
    # Validity
    unique_list = set()
    result = []
    for dict in list_name:
        if dict[col_name] not in unique_list:
            unique_list.add(dict[col_name])
            result.append(dict)
    list_name2 = result
    return list_name2

new_products_table = drop_duplicate(initial_products_table,initial_products_table,'product_name') #removes all duplicate products 


def create_final_products_list(big_data_list,products_list):
    for d in big_data_list:
        for items in d['items']:
            m = items.split("-")
            if len(m) == 2:
                product_name = m[0].rstrip().lstrip()
                product_price = float(m[1])
            elif len(m) == 3:
                product_name = m[0].rstrip().lstrip() + ' ' + m[1].rstrip().lstrip()
                product_price = float(m[2])
            else:
                continue
            for k in products_list:
                if k['product_name'] == product_name:
                    k['number_of_product_ordered'] = k['number_of_product_ordered'] +1
    return products_list


final_products_table = create_final_products_list(reformatted_cleaned_data,new_products_table)

final_products_table_with_branches_reassigned = branch_id_reassigner(final_products_table, branches_list) # this is the final products table used to fill products table with branch names reassgined to their respective product_ids

def sorting_hat(list_to_be_sorted, value, k ): #sorts the products into alphabetical order and corrects their product i.d
    newlist = sorted(list_to_be_sorted, key=lambda d: d[value])
    newlist2 = enumerate(newlist)
    newlist3 = []
    for x, y in newlist2:
        y[k] = x + 1
        newlist3.append(y)
    return newlist3

sorted_final_products_table = sorting_hat(final_products_table, "product_name", 'product_id') # Full list of unique products final_products_table in alphabetical order

sorted_final_products_table = guid_reassigner(sorted_final_products_table, "product_id")


sorted_final_products_table_with_branches_reassigned = branch_id_reassigner(sorted_final_products_table, branches_list)

payment_table = [{'payment_id':1, 'payment_method': 'CASH'},{'payment_id':2, 'payment_method': 'CARD'}] #creating payment table list
payment_table = guid_reassigner(payment_table,'payment_id')

def create_main_table_list(list_to_be_extracted_from, product_table, list_to_be_filled): #This gives us the information i  need for the main table: Transaction id, date/time, method of payment, products ordered, total and locations 
    data_dict = {'Transaction_id':1, 'Transaction_date_and_time': '','method_of_payment':'' ,'order_id': 1, 'products_ordered': [], 'order_sum': 0,'branch':''}
    for d in list_to_be_extracted_from:
        for items in d['items']:
            m = items.split("-")
            if len(m) == 2:
                product_name = m[0].rstrip().lstrip()
                product_price = float(m[1])
            elif len(m) == 3:
                product_name = m[0].rstrip().lstrip() + ' ' + m[1].rstrip().lstrip()
                product_price = float(m[2])
            else:
                continue
            for k in product_table:
                if k['product_name'] == product_name:
                    data_dict['products_ordered'].append(k['product_id'])
                    data_dict['order_sum'] += product_price
        data_dict['Transaction_date_and_time'] = d['purchase_date']
        if d['mode_of_payment'] == 'CASH':
            data_dict['method_of_payment'] = 'CASH'
        elif d['mode_of_payment'] == 'CARD':
            data_dict['method_of_payment'] = 'CARD'
        data_dict["branch"] = d["branch"]
        # Add the completed order to the list
        list_to_be_filled.append(data_dict)
        # Reset the data_dict for the next order
        data_dict = {'Transaction_id': data_dict['order_id'] + 1, 'Transaction_date_and_time': '','method_of_payment':'' ,'order_id': data_dict['order_id'] + 1, 'products_ordered': [], 'order_sum': 0,'branch':''}
    return list_to_be_filled

big_table = []

big_table = create_main_table_list(reformatted_cleaned_data,final_products_table,big_table) #list of information needed for main table

big_table=guid_reassigner(big_table, "Transaction_id")


def orders_table_func(table):#creates list required for orders table listing transaction id, product, quantity 
    list_to_create =[]
    dict = {}
    for d in table:
        y = d["products_ordered"]
        c = Counter(y)
        for x in c:
            dict["transaction_id"] = d["Transaction_id"]
            dict["product_id"] = x
            dict["quantity"] = c[x]
            list_to_create.append(dict)
            dict = {}
    return list_to_create

orders_table_list=orders_table_func(big_table) #list i will use to create orders table



big_table_with_branch_id= branch_id_reassigner(big_table,branches_list)
big_table_with_branch_id= payment_id_reassigner(big_table_with_branch_id,payment_table) #changes information in big_table_with_branch_id to have payment_method key as the correct guid payment_id

print("Processed complete! All required data for SQL tables have been extracted and sorted.")




