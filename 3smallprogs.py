#Erik Rodriguez - TUID: 915255369
#Section 001
def threeSort():
    print("")
    print("--Three Sort--")
    print("**This program sorts 3 integers of your choosing**")
    
    num1 = int(input("Input first integer: "))
    num2 = int(input("Input second integer: "))
    num3 = int(input("Input third integer: "))

    numList = [num1, num2, num3]
    numList.sort()

    print(numList)

def temp():
    print("")
    print("--Temperature Conversion (C -> F)--")
    print("**This program converts Celsius temperatures to Fahrenheit")

    temp = float(input("Input Celsius temperature: "))
    print((temp * (9/5)) + 32, "°F")

def secToHr():
    print("")
    print("--Seconds to Hours Conversion--")
    print("**This program will convert an amount of seconds")
    print("into hours, minutes, and seconds**")

    init = int(input("Input number of seconds as an integer: "))
    secs = init
    hrs = int(secs / 3600)
    secs = secs - hrs*3600
    mins = int(secs / 60)
    secs = secs % 60

    print(init, "seconds =", hrs, "hours,", mins, "minutes, and", secs, "seconds")

run = True
while(run == True):
    print("")
    print("***Three Small Programs***")
    print("(1) - Three Sort")
    print("(2) - Temperature Conversion")
    print("(3) - Seconds to Hours Conversion")
    print("(4) - EXIT")
    print("")
    select = int(input("Please input the number to the left of the program you want: "))

    if select == 1:
        threeSort()
    elif select == 2:
        temp()
    elif select == 3:
        secToHr()
    elif select == 4:
        print("**Exiting Program**")
        run = False
    else:
        print("That is not a valid selection, please try again")
