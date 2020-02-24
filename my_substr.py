def my_substr(string, length):
    '''
    Функция извлекает из строки подстроку
    указанной длины. Она принимает н вход два
    аргумента: строку и длину. Возвращает подстроку,
    начиная с первого символа
    '''
    result = ''
    index = 0
    if length > len(string):
        return 'substring longer than string'
    elif length < 0:
        return 'value is less than zero'
    else:
        while index < length:
            result += string[index]
            index += 1
        return result


string = 'To carry on'
print(len(string))
print(my_substr(string, 12))
print(my_substr(string, -1))
print(my_substr(string, 0))
print(my_substr(string, 8))
print(my_substr(string, 3))
