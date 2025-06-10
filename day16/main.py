# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# #timmy.pencolor('red')
# timmy.color('blue')
# my_screen= Screen()
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.align = "l"

table.field_names = ["pokemon", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])

print(table)

