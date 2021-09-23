#Erik Rodriguez - TUID: 915255369
#Section 001

print("**Welcome to \"Loop Lab 1\" by Erik Rodriguez**")
run = True
while (run == True):
    
    # Lab Selection
    def labSelect():   
        print("(1) - Bottles of Beer\n(2) - Multiplication Table\n(3) - Square Summation\n(4) - Hourglass\n(5) - Slash Figure")
        print("(6) - EXIT")
        select = int(input("Input the number next to the program you wish to run: "))
        if input == (1,2,3,4,5,6):
            print("That is not a valid selection, please try again")
            labSelect()
        else:
            return select
        
    # 99 Bottles of Beer
    def bottleBeer():
        beerNum = int(input("How many bottles of beer: "))

        while (beerNum > 0):
            print(beerNum, "bottles of beer on the wall,", beerNum, "bottles of beer\n",
                  "Take one down, pass it around", (beerNum-1), "bottles of beer on the wall")
            beerNum = beerNum - 1
            
    # Multiplication Table
    def multiTable():
        num = int(input("What integer's multiplication table would you like: "))
        x = 1
        count = 1

        if (num*num) < 10:
            spacing = 0
        if (num*num) > 10 and (num*num) < 100:
            spacing = 1
        if (num*num) >= 100:
            spacing = 2

        while x <= num*num:
            
            if x <= num * count:
                print(x, " ", end = '')
                if spacing == 1:
                    if x < 10:
                        print(" ", end = '')
                if spacing == 2:
                    if x < 10:
                        print("  ", end = '')
                    if x >= 10 and x < 100:
                        print(" ", end = ''
                              )
                x = x + count
                
            else:
                count = count + 1
                print("\n")
                x = count
        print("")
        
    # Square Summation
    def sqSum():
        num = int(input("Please give an integer for square summation: "))
        sqSum = 0

        for x in range(num + 1):
            sqSum = sqSum + (x*x)
            
        print(sqSum)

    # Hourglass
    def hourGlass():
        for x in range (11):
            if (x == 0) or (x == 10):
                print("|\"\"\"\"\"\"\"\"\"\"|")
                
            elif (x == 5):
                print("     ||")
                
            elif x < 5:
                for y in range (x):
                    print(" ", end="")
                print("\\", end="")
                for y in range ((5-x) * 2):
                    print(":", end="")
                print("/")
                
            elif x > 5:
                for y in range (10-x):
                    print(" ", end="")
                print("/", end ="")
                for y in range((x-5) * 2):
                    print(":", end ="" )
                print("\\")
            
    #Slash Figure
    def slashFig():
        print("This is a slash ascii art program.")
        num = int(input("Please input an integer: "))
        #count will be used as a reverse iterator in the main for loop,
        #from original length to 1
        count = num

        #main for loop iterates through input's length
        for x in range(num):
            
            #slash for loop prints pair of //'s for however
            #long x is, therefore prints one more pair then last line
            #every iteration
            for y in range(x):
                print("\\\\", end="")
                
            #exclamation point for loop first prints pair of !!'s for
            #however long the original input was. For each main
            #loop iteration, this count is decreased by 1, ends with
            #printing a single pair
            for y in range ((count*2) - 1):
                print("!!", end="")

            #iterating count separately from the main loop
            count = count -1

            #see previous slash for loop
            for y in range(x):
                print("//", end="")
            print("")
        
    select = labSelect()

    if select == 1:
        print("")
        bottleBeer()

    if select == 2:
        print("")
        multiTable()
        
    if select == 3:
        print("")
        sqSum()

    if select == 4:
        print("")
        hourGlass()

    if select == 5:
        print("")
        slashFig()
    
    elif select == 6:
        run = False
        
    print("")

print("**Exiting Loop Lab**")
