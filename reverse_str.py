def reverse_str(string):
    '''
    Функция принимает строку и переворачивает её
    '''
    if string:
        index = len(string) - 1
        result = ''
        while index >= 0:
            current_char = string[index]
            result += current_char
            index -= 1
        return result
    return False


print(reverse_str(''))
print(reverse_str('The road turns'))
print('Tenet')
