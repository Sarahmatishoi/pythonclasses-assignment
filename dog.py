class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def eat(self):
        return f"{self.color} {self.name} with {self.age} years old eats borns."
    def dance(self):
        return f"{self.color} {self.name} with {self.age} likes to dance."

        