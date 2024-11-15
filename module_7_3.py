class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        self.all_words = {}
        marks = [',', '.', '=', '!', '?', ';', ':', ' - ', '–', '—', '(', ')']
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                lines = ''
                for line in file:
                    for m in marks:
                        line = (line.lower()).replace(m, '')
                    lines += line
                self.all_words[name] = lines.split()
        return self.all_words

    def find(self, word):
        self.find_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(0,len(words)):
                if word == words[i]:
                    self.find_word [name] = i+1
                    break
        return self.find_word

    def count(self, word):
        self.count_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            counter = 0
            for i in range(0,len(words)):
                if word == words[i]:
                    counter += 1
                self.count_word [name] = counter
        return self.count_word


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))