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


