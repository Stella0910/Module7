import io
from pprint import pprint

def custom_write(file_name, strings):
    name = file_name
    string_positions = {}
    counter_lines = 0
    file = open(name, 'a', encoding='utf-8')
    for string in strings:
        counter_lines += 1
        string_positions[(counter_lines, file.tell())] = string
        file.write(f'{string}\n')
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)