def is_leap_year(input_year):
    '''
    Функиця проверяет год на високосность.
    Возвращает логическое значение.
    Год будет високосным, если он кратен 400
    или он одновременно кратен 4 и не кратен 100
    '''
    if input_year % 400 == 0 or (input_year % 4 == 0
    and input_year % 100 != 0):
        return True
    return False


print(is_leap_year(1880))
print(is_leap_year(1920))
print(is_leap_year(2008))
print(is_leap_year(2013))
print(is_leap_year(2014))
print(is_leap_year(2019))
