import turtle

def draw_square(some_turtle):
        for i in range (0 , 4):
            some_turtle.forward(100)
            some_turtle.right(90)
        
def draw_art():
     window = turtle.Screen()
     window.bgcolor("red")

     #create turtle Brad - Draws square
     brad = turtle.Turtle()
     brad.shape("turtle")
     brad.color("yellow")
     brad.speed(2)
     for i in range(0 , 36):
         draw_square(brad)
         brad.right(10)

     #create turtle Angie - Draws circle
    # angie = turtle.Turtle()
     #angie.shape("arrow")
    # angie.color("blue")
    # angie.speed(2)
     #angie.circle(100)

     window.exitonclick()

a = 1+2
print a

if __name__ == "__main__":
    draw_art()
    #draw_square()
    
