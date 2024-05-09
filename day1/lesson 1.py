from turtle import *

#we want tu paint a house

#step 1 paint square

width(6)
color("grey")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(70)
left(90)
color("brown")
begin_fill()
forward(90)
right(90)

forward(50)
right(90)

forward(90)
end_fill()
penup()

goto(200,200)
pendown()
color("green")
begin_fill()
right(135)
forward(140)

left(90)
forward(140)
end_fill()

penup()
goto(150,120)
pendown()
color("blue")
begin_fill()
right(135)
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()

penup()
goto(10,120)
pendown()
color("blue")
begin_fill()
right(90)
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
end_fill()

penup()
goto(200,200)
pendown()
color("grey")
begin_fill()
left(80)

forward(170)
right(80)

forward(150)
right(83)

forward(180)
end_fill()

penup()
goto(200,200)
pendown()
color("black")
left(83)
forward(200)

penup()
goto(200,200)
pendown()
left(80)

right(180)
right(35)
color("green")
begin_fill()
color("black")
forward(140)
right(150)
forward(240)
right(46)
forward(71)
end_fill()
right(30)
forward(160)
right(85)
forward(180)
right(2)
forward(190)
right(94)
forward(202)
right(40)
forward(140)


exitonclick()