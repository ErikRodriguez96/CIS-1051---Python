#Erik Rodriguez - TUID: 915255369
#Section 001
import re

userPass = ""
test1,test2,test3,test4 = False, False, False, False

userPass = input("Input Password: ")

if re.search(".{8,}", userPass) != None:
    print("Test 1 Passed")
    test1 = True

if re.search("[a-z]+", userPass) != None:
    print("Test 2 Passed ")
    test2 = True
    
if re.search("[A-Z]+", userPass) != None:
    print("Test 3 Passed")
    test3 = True

if re.search("\d+", userPass) != None:
    print("Test 4 Passed")
    test4 = True

if test1 == True and test2 == True and test3 == True and test4 == True:
    print("Password is Strong")
else:
    print("Password is NOT Strong")
