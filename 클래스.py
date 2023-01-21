class Person:
    age = 10
    name = 'sun'
    number = 100

    def set(self,a):
        print(a)

class student(Person):
    age = 50
    def __init__(self,age):
        super()
        self.age = age

class baby(student):
    age =1


hyun = baby(27)

print(hyun.name)



