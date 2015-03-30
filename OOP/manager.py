from OOP.person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def raisePay(self, percent, bonus=0.1):
        Person.raisePay(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager('Thomas Edison', 50, 50000)
    print(tom)
    Manager.raisePay(tom, .5)
    print(tom.pay)
