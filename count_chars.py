def count_chars(string, char):
    '''
    Функция считает повторения указанного символа
    в строке. Принимает строку и символ. Возвращает число.
    '''
    result = 0
    index = len(string) - 1
    while index >= 0:
        if string[index] == char:
            result += 1
        index -= 1
    return result


string = 'A cosminc responsibility'
print(count_chars(string, 'i'))
print(count_chars(string, 'o'))
print(count_chars(string, 'z'))
