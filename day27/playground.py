#Unlimited Arguments
#def add(*args):
#    for n in rangs:
#        print(n)
def add(*args):
    total=0
    for n in range(0,len(args)):
        total+=args[n]
    return total
print(add(1,2,3,4,5,6,7,8,9))

def calculate(n,**kwargs):
    # for(key,value) in kwargs.items():
    #     print(value)
    n+=kwargs['add']
    n*=kwargs['multiply']

    print(n)
calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make=kw['make']
        self.model=kw['model']
my_car=Car(make='Nissan',model='GT-R')

print(my_car.make)