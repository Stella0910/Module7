import io
from pprint import pprint

def custom_write(file_name, strings):
    name = file_name
    _list_number = list()
    _list_string = list()
    _tell = list()
    for number in range(len(strings)):
        _list_number.append(number+1)
    file = open(name, 'a', encoding='utf-8')
    for string in strings:
        _tell.append(file.tell())
        file.write(f'{string}\n')
        _list_string.append(string)
    file.close()
    strings_positions = dict(zip(zip(_list_number, _tell), _list_string))
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
