class Retail:
    def __init__(self, item, description, units, price):
        self.__item = item
        self.__description= description
        self.__dept = units
        self.__job= price

    def set_units(self, units):
        self.__dept = units
    def set_price(self, price):
        self.__job = price
    def get_item(self):
        return self.__item
    def get_description_number(self):
        return self.__description
    def get_units(self):
        return self.__dept
    def get_price(self):
        return self.__job
    def __str__(self):
        return 'item: ' + self.__item + '\n' +\
               'description: ' + str(self.__description) + '\n' +\
               'units: ' + self.__dept + '\n' +\
               'price: ' + self.__job

susan = Retail ('item#1','jacket', '12', '59.95$')
mark = Retail('item#2', 'designer jeans','40', '34.95$')
joy = Retail('item#3' ,'shirt', '20', '24.95$')
tick = Retail('item#4','lungi','13', '35.25$')

print(susan, end = '\n\n')
print(mark, end = '\n\n')
print(joy, end = '\n\n')
print(tick)

