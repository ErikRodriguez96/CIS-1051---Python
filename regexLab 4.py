#Erik Rodriguez - TUID: 915255369
#Section 001
import re
import random

passList = []
x = 0
i = 0
randWord = 0
word = ""
words = open(r"words.txt","r")
finalPass = ""

while x < 4:
    
    randWord = random.randint(0,45401)
    fp = open("words.txt")
    for i,line in enumerate(fp):
        if i == randWord:
            if line.islower() == True:
                word = line
                word = word.rstrip()
                print(word)
                passList.append(word)
            else:
                x = x - 1
                continue
    x += 1
    
finalPass = finalPass.join(passList)
print("Generated Password = ", finalPass)
