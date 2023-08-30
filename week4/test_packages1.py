from packges_test import phone_number_insert1
from packges_test import list_index_number2

phone11 = '07398952757'

def test_phone_number_insert11():
    expected = '079'
    actual = phone_number_insert1(phone11)
    assert expected == actual

test_phone_number_insert11()

phone12 = 'popopopo'

def test_phone_number_insert12():
    expected = '0'
    actual = phone_number_insert1(phone12)
    assert expected == actual

test_phone_number_insert12()

phone13 = ''

def test_phone_number_insert13():
    expected = 'empty'
    actual = phone_number_insert1(phone13)
    assert expected == actual

test_phone_number_insert13()

phone14 = '073989527573'

def test_phone_number_insert14():
    expected = '0'
    actual = phone_number_insert1(phone14)
    assert expected == actual

test_phone_number_insert14()

phone15 = '0739895275'

def test_phone_number_insert15():
    expected = '0'
    actual = phone_number_insert1(phone15)
    assert expected == actual

test_phone_number_insert15()






list_1 = [0,1,2,3,4,5]

object = 'k'

def test_list_index_number2():
    expected = 'ValueError'
    actual = list_index_number2(object,list_1)
    assert expected == actual

test_list_index_number2()

object2 = '100'

def test_list_index_number22():
    expected = 'number too high'
    actual = list_index_number2(object2,list_1)
    assert expected == actual

test_list_index_number22()


object3 = '3'

def test_list_index_number23():
    expected = 3
    actual = list_index_number2(object3,list_1)
    assert expected == actual

test_list_index_number23()

