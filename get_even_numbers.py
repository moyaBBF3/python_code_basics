def get_even_numbers(number):
    '''
    Функция принимает число и возвращает
    в виде строки все чётные числа от 1 до 
    введённого числа включительно. Числа в 
    результате разделены запятыми
    '''
    counter = 1
    result = ''
    while counter <= number:
        if counter % 2 == 0:
            result = result + str(counter) + ','
        counter += 1
    return result[:-1] + '.'


print(get_even_numbers(10))
