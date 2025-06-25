#List Compreshension
numbers=[1,2,3]
# new_number=[new_item for item in list]
new_number=[n+1 for n in numbers]
print(new_number)

name="Angela"
new_list=[letter for letter in name]
print(new_list)

range=range(1,5)
new_range=[2*n for n in range]
print(new_range)

#Conditional List Comprehension

#new_list=[new_item for item in list if test],
names=["Alex","Beth","Carloline","Dave","Eloanor"]
short_names=[name.upper() for name in names if len(name)>5]
print(short_names)