
from sql_packages import *

product1 = 'Fanta'
checker1 = ''
checker1 = product_name_check(product1, checker1)

def product_1_check():
   
    expected = 'yes'
    actual = checker1
    assert expected == actual

product_1_check()    