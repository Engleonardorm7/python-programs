class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f"hello, my name is {self.name} and I am {self.age} years old")

if __name__=="__main__":
    person = Person("David",34)

    print(f"Age: {person.age}")
    person.say_hello()