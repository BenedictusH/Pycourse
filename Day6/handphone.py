phones = []

class Handphone:
    def __init__(self, version, brand, color):
        self.version = version
        self.brand = brand
        self.color = color
    
    def info(self):
        print(self.version, self.brand, self.color)

    def register(self):
        phones.append(self)

while True:
    forward = input('Input a phone? (y/n)')
    if forward == 'y':
        phoneversion = input('Enter phone version: ')
        phonebrand = input('Enter phone brand: ')
        phonecolor = input('Enter phone color: ')

        phone = Handphone(phoneversion, phonebrand, phonecolor)
        phone.info()
        phone.register()
    elif forward == 'n':
        break
    else:
        print('Input invalid')

for phone in phones:
    phone.info()