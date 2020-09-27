import turtle
shri = turtle.Turtle()
shri.shape('turtle')

number_list = [1,2,3,4,5,6,7,8,9,10]

shri.color("green")
for number in number_list:
    shri.forward(number*10)
    shri.left(60)