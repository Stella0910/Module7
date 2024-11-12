from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'




class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result

    def add(self, *products):
        for i in products:
            if isinstance(i, Product):
                file = open(self.__file_name, 'r')
                if f'{i.name}' in file.read():
                    print(f'Продукт {i.name} уже есть в магазине')
                    file.close()
                else:
                    file = open(self.__file_name, 'a')
                    file.write(f'{i.__str__()}\n')
                    file.close()
            else:
                print(f'Товар {i} не подходит для списка продуктов в этом магазине.')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
