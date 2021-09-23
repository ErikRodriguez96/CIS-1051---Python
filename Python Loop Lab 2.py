#Erik Rodriguez - TUID: 915255369
#Section 001

#Vowel program
def vowels():

    #Filter function
    def getVowel(word):
        
        vowList = ['a','e','i','o','u']

        if(word in vowList):
            return True
            
        else:
            return False

    print("** Vowels **")
    
    #input
    word = str(input("Please input a word: "))
    wordList = [char for char in word]
    print(" ")

    #word list filtered using filter() method
    filteredWord = list(filter(getVowel, wordList))
    print(filteredWord)

    #final output
    print("There are", len(filteredWord), "vowels in the word", word)


#Even Digit Program
def evens():

    #Variable declarations
    i = 0
    evens = 0
    print("** Even Digits **")

    #number input
    num = int(input("Please input an integer: "))
    i = num
    print(" ")

    #loop checks if current number is divisible by 2 (if so then add 1 to the count)
    #then divides by 10 to be able to check the next integer on next loop
    while(i > 0):

        if (i % 2) == 0:
            evens += 1
        
        i = int(i / 10)
    #final output    
    print("There are: ", evens, " even digits in this integer")


#Armstrong Number Program
def armNum():

    #variable declarations
    i = 0
    x = 0
    numSum = 0
    print("**Armstrong Numbers**")

    #number input
    num = int(input("Please input an integer: "))
    x = num
    print(" ")

    #loop goes takes the last digit of the current num and cubes
    #this cube is added to a sum and tallied
    #loop is broken up for readability, calculations can be done more succintly
    while(x > 0):

        i = int((x % 10))
        i = i**3

        numSum += i

        x = int(x / 10)

    #final output
    if (numSum == num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


#Riddler Program
def riddle():
    #separated into methods checking each of the 4 criteria

    #checks if digits are the same or different, simple comparisons
    def diffDigits(i1, i2, i3, i4):

        if (i1 == i2 or i1 == i3 or i1 == i4):
            return False
        if (i2 == i3 or i2 == i4):
            return False
        if (i3 == i4):
            return False
        else:
            return True

    #checks if digit in thousandths place is 3 times the digit in the tens place
    def thou3Ten(i4, i2):

        if ((i2 * 3) == i4):
            return True
        else:
            return False

    #checks if the sum of the numbers digits equals 27
    def digitSum(i1, i2, i3, i4):

        y = i1+i2+i3+i4

        if (y == 27):
            return True
        else:
            return False

    print("-- RIDDLER PARSER EXECUTED --")
    print("-- SCANNING ALL POSSIBLE ADDRESSES --")
    print(" ")

    #for loop goes through all 4 digit numbers that work with criteria
    #increments by 2 to only parse odd numbers
    for x in range(1001, 9999, 2):
        i = x

        #gets and assigns digit values
        i1 = i % 10
        i = int(i/10)
        i2 = i % 10
        i = int(i/10)
        i3 = i % 10
        i = int(i/10)
        i4 = i

        #runs number through every criteria method, stops if encounters
        #unfulfilled criteria
        if thou3Ten(i4, i2) == True:
            if diffDigits(i1, i2, i3, i4) == True:
                if digitSum(i1, i2, i3, i4) == True:
                    print("!!!!! ADDRESS FOUND !!!!!")
                    print(" ")
                    print("-- RIDDLER WILL STRIKE AT: ", end = '')
                    print(x, "PENNSYLVANIA AVENUE --")
                    break

select = 0
print("**Loop Problem Set 2**")
print(" ")

#Program selection
while (select != 999):
    
    print(" ")
    print("Enter 1 for Vowel Program")
    print("Enter 2 for Even Digit Program")
    print("Enter 3 for Armstrong Number Program")
    print("Enter 4 for Riddler Program")
    print("Enter 999 to EXIT")
    print(" ")

    select = int(input("Selection: "))
    print("____________________________________________")

    if select == 1:
        vowels()
    elif select == 2:
        evens()
    elif select == 3:
        armNum()
    elif select == 4:
        riddle()
    elif select == 999:
        print("** EXITING PROGRAM **")

    print("____________________________________________")