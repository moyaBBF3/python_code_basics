def does_contain(string, char):
    '''
    Функция проверяет с учётом регистра,
    содержит ли строка указанную букву.
    Принимает строку и букву для поиска.
    '''
    index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False


string = 'A grate favour'
print(does_contain(string, 'A'))
print(does_contain(string, 'f'))
print(does_contain(string, 'z'))
