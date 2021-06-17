x=[100,110,120,130,140,150,]
p=[y*5 for y in x]
print(p)

    

def divisisble_by_three(n):
    for x in n:
        if x%3==0:
            return x


def numbers(): 
    p=[]
    sublist=[[1,2],[3,4],[5,6]]
    
    for list in sublist:
        p.extend(list)
    print(p)
numbers()

def smallest():
      a=[2,5,4,6,8,4]
      print(min(a))
smallest()
def  letter():
    r= ['a','b','a','e','d','b','c','e','f','g','h']
    return r.sort()
    
letter()
def divisible_by_seven ():
    h=range(100,200)
    for g in h:
        if g%7==0:
            print(g)
divisible_by_seven()
def greet():
   
    students=[{"name":"Eunice","age":19},{"name":"Agnes","age":21},{"name":"Teresa","age":18},{"name":"Asha","age":22}]
    
    return f"Hello {students.name}, you were born in {2021-students.age}"
greet()
class Rectangle():
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.length*self.width
    area(6,8)
    def perimeter(self):
        return 2(self.width*self.length)
    perimeter(2(8*6))
   
    x=[[1,2],[3,4],[5,6]] 
    new_list=list(sum*(x))
    print(new_list)   
    