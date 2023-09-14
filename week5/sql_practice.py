from python_packages5 import *
import pymysql
import os
from dotenv import load_dotenv
from sql_packages import * 

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")


connection, cursor = setup_db_connection()





def address_fucntion(something):
     
     while something == '0' :
          unit_number = 0
          street_name = 0
          emptyy = ''
          while unit_number == 0 :
            unit_number = input('please give me your Unit Number ').title().strip()
          while street_name == 0 :
            street_name = input('Please insert your street address ').title().strip()

          if unit_number.strip() != emptyy and street_name.strip() :
                 print("houe / flat number and street address was inserted ")
                 something = f'{unit_number}, {street_name}'       
            
          elif unit_number.strip() == emptyy and street_name.strip() == emptyy :
                print("Address was not insurted")
                something = ''
          else:
              something = '!'
     return something
            
                





def postcode_function(something):
    while something == '0':
        postcode1 = 0
        postcode2 = 0
        emptyy = ''
        while postcode1 == 0:
            postcode1 = input('please insert the first part of your postcode')
            if postcode1.strip() != '':
                    if len(postcode1) < 2 or len(postcode1) > 4:
                        print('please input the correct characters')
                        postcode1 = 0
                    else:
                        print('thankyou for your input')
        while postcode2 == 0:
            postcode2 = input('please insert the second part of your postcode')
            postcode2 = input('please insert your 2NDpostcode ').capitalize().strip()
            if address_postcode2 != '':
                if len(address_postcode2) != 3:
                    print('please input a potcode of 3 character')
                    address_postcode2 = 0
                else:
                    print('thank you for your input')
        
        if postcode1.strip() != emptyy and postcode2.strip() != emptyy :
             print("houe / flat number and street address was inserted ")
             something = f'{postcode1} {postcode2}'
        elif postcode1.strip() == emptyy and postcode2.strip() ==emptyy :
            print('No postcode was inserted')
            something = ''
        else:
            something = '!'
         

a = ['1','2','3']
a = ','.join(a)


print(a)