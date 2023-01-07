#Kosmoso uzkariautojai
import turtle
import os
import math
import random




#Ekranas
ek = turtle.Screen()
ek.bgcolor('black')
ek.title("Kosmoso uzkariautojai")



#Siena
sn_pen= turtle.Turtle()
sn_pen.speed(0)
sn_pen.color('white')
sn_pen.penup()
sn_pen.setposition(-300,-300)
sn_pen.pendown()
sn_pen.pensize(3)
for side in range(4):
    sn_pen.fd(600)
    sn_pen.lt(90)
sn_pen.hideturtle()


#Nustatyti taskus 0
taskai = 0



#Nupiesti taskus
taskai_pen = turtle.Turtle()
taskai_pen.speed(0)
taskai_pen.color("white")
taskai_pen.penup()
taskai_pen.setposition(-290,280)
taskaistring = "Taskai: %s" %taskai
taskai_pen.write(taskaistring, False, align="left", font=("Arial",14, "normal"))
taskai_pen.hideturtle()



#Zaidejas
za = turtle.Turtle()
za.color('blue')
za.shape('triangle')
za.penup()
za.speed(0)
za.setposition(0,-250)
za.setheading(90)
zaspeed = 15



#zaidejo soviniai
kulka = turtle.Turtle()
kulka.color("yellow")
kulka.shape("triangle")
kulka.penup()
kulka.speed(0)
kulka.setheading(90)
kulka.shapesize(0.5, 0.5)
kulka.hideturtle()

kulkaspeed = 20


#Kulkos stadija
#---------------
#isauta kulka
kulkastate = "ready"








#Judejimas
def move_left():
    x = za.xcor()
    x -= zaspeed
    if x < -280:
        x = -280
    za.setx(x)
    
def move_right():
    x = za.xcor()
    x += zaspeed
    if x > 280:
        x = 280
    za.setx(x)

def fire_kulka():
    #global
    global kulkastate
    if kulkastate == "ready":
        kulkastate = "fire"
    


    
        #Kulka virs zaidejo
        x = za.xcor()
        y = za.ycor() + 10
        kulka.setposition (x, y)
        kulka.showturtle()


def isCollision (t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    




#Klaveturos valdymas
turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_kulka, "space")



#priesai
#priesu skaicius
prs_skaicius = 10
#priesu skaicius
prs = []
#priesu sarasas
for i in range(prs_skaicius):
    #sukurti priesa
    prs.append(turtle.Turtle())

for pr in prs:
    
    pr.color("red")
    pr.shape("circle")
    pr.penup()
    pr.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    pr.setposition(x, y)
    
prspeed = 2





#Pagrindinis zaidimo kodas
while True:

    
    for pr in prs:
        
        #juda priesas
        x = pr.xcor()
        x += prspeed
        pr.setx(x)
 
    #priesas juda i kaire, zemyn
        if pr.xcor() > 280:
            #Pajudinti visus priesus zemyn
            for e in prs:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Pakeisti priesu krypti    
            prspeed *= -1    
       
        if pr.xcor() <-280:
            #Pajudinti visus priesus zemyn
            for e in prs:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Pakeisti priesu krypti
            prspeed *= -1    

        #susikirtimas
        if isCollision(kulka, pr):
            #perstatyt kulka
            kulka.hideturtle()
            kulkastate = "ready"
            kulka.setposition(0, -400)
            #perstatyt priesa
            x = random.randint(-200,200)
            y = random.randint(100,250)
            pr.setposition(x, y)


        if isCollision (za, pr):
            za.hideturtle()
            pr.hideturtle()
            print("Žaidimas baigtas :(")
            break

        
            #Tasku atnaujinimas
            taskai += 10
            taskaistring = "taskai: %s" %taskai
            taskai_pen.clear()
            taskai_pen.write(taskaistring, False, align="left", font=("Arial",14, "normal"))
        



    #Judinit kulka
    if kulkastate == "fire":    
       y = kulka.ycor()
       y += kulkaspeed
       kulka.sety(y)


    #kulkos ribos
    if kulka.ycor() > 275:
        kulka.hideturtle()
        kulkastate = "ready"


    
        
















    


    

