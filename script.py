print("hello world")
x = input("what is x?\n")
print(type(x))
x = int(x)
print(type(x))

print(f"x is {x}")
def square(n):
    y=n*n
    return y

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 25

person = Person(name='john')
squared = square(int(x))
data = {"name": "Alice", "age": 30, "city": "New York"}
print(data)