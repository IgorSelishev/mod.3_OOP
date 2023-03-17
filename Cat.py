class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age

cat_1 = Cat("Baron", "boy", 2)
cat_2 = Cat("Sam", "boy", 2)

class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

dog_1 = Dog('Felix', 'boy', 2)

class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.first_name}, {self.second_name}. "{self.city}. Баланс: {self.balance} руб.'
    def get_guest(self):
        return f'{self.first_name}, {self.second_name}, г. {self.city}'
    
customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
customer_2 = Customers('Владимир', 'Зайцев', 'Кострома', 45)
customer_3 = Customers('Олеся', 'Янина', 'Новосибирск', 40)

guest_list = [customer_1, customer_2, customer_3]

for guest in guest_list:
    print(guest.get_guest())






print(cat_1.get_name(), cat_1.get_gender(), cat_1.get_age())
print(cat_2.get_name(), cat_2.get_gender(), cat_2.get_age())
print (dog_1.get_pet())