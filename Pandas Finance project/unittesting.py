# Unit Testing
import pandas as pd
import numpy as np
import datetime
from pandas_datareader import data
import seaborn as sns 
from packages import * 


# testing with correct date

date1 = '2001-07-23'


def test_date1():
    actual = '1'
    expected = 'y'
    actual = check_date(date1, checkdate= actual)
    assert expected == actual

test_date1()
    

# testing with letters
date2 = '2001-07-kk'


def test_date2():
    actual = '1'
    expected = 'n'
    actual = check_date(date2, checkdate= actual)
    assert expected == actual

test_date2()


# testing with only with no day inserted

date3 = '2001-07'


def test_date3():
    actual = '1'
    expected = 'n'
    actual = check_date(date3, checkdate= actual)
    assert expected == actual

test_date3()


# testing with only with MONTH inserted but wrong length

date4 = '2001-7-04'


def test_date4():
    actual = '1'
    expected = 'n'
    actual = check_date(date4, checkdate= actual)
    assert expected == actual

test_date4()


# testing with only with YEAR inserted but wrong length

date5 = '200-07-04'


def test_date5():
    actual = '1'
    expected = 'n'
    actual = check_date(date5, checkdate= actual)
    assert expected == actual

test_date5()


# testing with only with DAY inserted but wrong length

date5 = '2001-7-4'


def test_date5():
    actual = '1'
    expected = 'n'
    actual = check_date(date5, checkdate= actual)
    assert expected == actual

test_date5()