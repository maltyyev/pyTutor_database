class Person(object):
    def __init__(self, name, age, pay, job):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)

    def updateName(self, name):
        self.name = name

    def raisePay(self, percent):
        self.pay *= (1.0 + percent)

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'dev')
    sue = Person('Sue Jones', 45, 40000, 'hdw')
