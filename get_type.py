def get_type(sentence):
    '''
    Функция определяет тип предлоожения.
    '''
    last_char = sentence[-1]
    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'
    result = ('Sentence is {}'.format(sentence_type))
    return result


print(get_type('It\'s obvious'))
print(get_type('I feel progress!'))
print(get_type('Do you like this format?'))
