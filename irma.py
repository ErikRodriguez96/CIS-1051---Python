#Erik Rodriguez - TUID: 915255369
#Section 001

import turtle
import csv


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    t.st()
    t.pu()
    t.width(0)
    
    with open('irma.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cat = 0
        i = 0
        #skipping first line
        next(csv_reader)

        for row in csv_reader:
            if i == 0:
                t.setx(float(row[3]))
                t.sety(float(row[2]))
                t.color("White")
                t.pd()
                i += 1
                print("INIT LOOP CALLED")
            else:
                break
            
            
        for row in csv_reader:
            t.setx(float(row[3]))
            print("X: ", float(row[4]))
            t.sety(float(row[2]))
            print("Y: ", float(row[3]))
            
            cat = float(row[4])
            print("WIND SPEED: ", cat)
            if cat < 74.0:
                t.color("White")
                print("COLOR SET TO WHITE")
                t.width(1)
                
            elif cat >= 74.0 and cat <= 95.0:
                t.color("Blue")
                print("COLOR SET TO BLUE")
                t.width(2)
                t.write("1")
                
            elif cat >= 96.0 and cat <= 110.0:
                t.color("Green")
                print("COLOR SET TO GREEN")
                t.width(3)
                t.write("2")
                
            elif cat >= 111.0 and cat <= 129.0:
                t.color("Yellow")
                print("COLOR SET TO YELLOW")
                t.width(5)
                t.write("3")
                
            elif cat >= 130.0 and cat <= 156.0:
                t.color("Orange")
                print("COLOR SET TO ORANGE")
                t.width(8)
                t.write("4")
                
            elif cat >= 157.0:
                t.color("Red")
                print("COLOR SET TO RED")
                t.width(12)
                t.write("5")
            

if __name__ == "__main__":
    irma()











