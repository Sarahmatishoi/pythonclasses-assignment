class Car:
    
    def __init__(self,color,make,model,speed):
        self.color=color
        self.make=make
        self.model=model
        self.speed=speed
    def move(self):
        return f" {self.color} {self.make} {self.model} moves at a speed of {self.speed} kilometers per hour."
    def accelerator(self):
        return f"{self.color} {self.make} {self.model} accelerate 10 seconds after its speed changes to {self.speed}"

        