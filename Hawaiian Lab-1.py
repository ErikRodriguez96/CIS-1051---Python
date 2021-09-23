#Erik Rodriguez - TUID: 915255369
#Section 001

#checks for hawaiian only characters from a dictionary
def isHwn(userWord):
    x = 0
    y = 0
    i = False
    wordList = list(userWord)
    wordLen = len(wordList)
    hwnLetters = {1:"a",2:"e",3:"i",4:"o",5:"u",6:"p",7:"k",8:"h",9:"l",10:"m",11:"n",12:"w",13:"'",14:" "}

    #FORMER BLACK MAGIC LOOP
    #Loop iterates through each letter of the word then compares
    #against each letter of the dictionary
    #if a valid character is found then the loop breaks early and continues
    #if all characters are valid then the loop will terminate
    #without reaching the return false statement and thus will hit the return true statement
    #if it finds none then the boolean stays set to false and the loop reaches the
    #return false statement and ends the function call
    for x in range (wordLen):
        for y in range (1,15):
            if wordList[x] == hwnLetters[y]:
                i = True
                break
            elif wordList[x].isspace() == True:
                
                i = True
                break
            else:
                i = False
        if i == False:
            return False

    return True

def hwnToEng(userWord):
    x = 0
    conTrue = False
    engWord = list()
    wordList = list(userWord)
    wordLen = len(wordList)

    #loop goes through all letters and adds english pronunciation
    #to a separate list
    
    #for vowel groups, loop checks applicable characters then checks
    #if next character would form a vowel group
    #if yes then adds the vowel group sound to english list,
    #else adds the singular vowel sound

    #adds hyphens if previous word was not a consonant, space, apostrophe, and
    #if this is not the final letter being checked
    while x < wordLen:    
        if wordList[x] == " ":
            engWord.append(" ")
            x += 1
            
        elif wordList[x] == "'":
            engWord.append("'")
            x += 1
            
        elif x != 0 and conTrue == False:
            engWord.append("-")
        
        #resets consonant boolean for next loop pass    
        conTrue = False
        
        #VOWELS   
        #letter A operations
        if wordList[x] == "a":
            if (x + 1) < wordLen:
                if wordList[x+1] == "i":
                    engWord.append("eye")
                    x += 2
                    continue
                elif wordList[x+1] == "e":
                    engWord.append("eye")
                    x += 2
                    continue
                elif wordList[x+1] == "o":
                    engWord.append("ow")
                    x += 2
                    continue
                elif wordList[x+1] == "u":
                    engWord.append("ow")
                    x += 2
                    continue
                elif wordList[x+1] == "w":
                    engWord.append("wah")
                    x += 2
                    continue
                else:
                    engWord.append("ah")
                    x += 1
                    continue
            else:
                engWord.append("ah")
                x += 1
                continue

        #letter E operations        
        elif wordList[x] == "e":
            if x + 1 < wordLen:
                if wordList[x+1] == "i":
                    engWord.append("ay")
                    x += 2
                    continue
                elif wordList[x+1] == "u":
                    engWord.append("eh-oo")
                    x += 2
                    continue
                elif wordList[x+1] == "w":
                    engWord.append("vah")
                    x += 2
                    continue
                else:
                    engWord.append("eh")
                    x += 1
                    continue
            else:
                engWord.append("eh")
                x += 1
                continue
            
                
        #letter I operations        
        elif wordList[x] == "i":
            if x + 1 < wordLen:
                if wordList[x+1] == "u":
                    engWord.append("ew")
                    x += 2
                    continue
                elif wordList[x+1] == "w":
                    engWord.append("vah")
                    x += 2
                    continue
                else:
                    engWord.append("ee")
                    x += 1
                    continue
            else:
                engWord.append("ee")
                x += 1
                continue
                
        #letter O operations        
        elif wordList[x] == "o":
            if x + 1 < wordLen:
                if wordList[x+1] == "i":
                    engWord.append("oyo")
                    x += 2
                    continue
                elif wordList[x+1] == "u":
                    engWord.append("ow")
                    x += 2
                    continue
                elif wordList[x+1] == "w":
                    engWord.append("wah")
                    x += 2
                    continue
                else:
                    engWord.append("oh")
                    x += 1
                    continue
            else:
                engWord.append("oh")
                x += 1
                continue

        #letter U operations        
        elif wordList[x] == "u":
            if x + 1 < wordLen:
                if wordList[x+1] == "i":
                    engWord.append("ooey")
                    x += 2
                    continue
                elif wordList[x+1] == "w":
                    engWord.append("wah")
                    x += 2
                    continue
                else:
                    engWord.append("oo")
                    x += 1
                    continue
            else:
                engWord.append("oo")
                x += 1
                continue

        #CONSONANTS:

        #letter P Operations
        elif wordList[x] == "p":
                engWord.append("poo")
                x += 1
                continue

        #letter W Operations
        elif wordList[x] == "w":
                engWord.append("wah")
                x += 1
                continue
                
        #letter K Operations
        elif wordList[x] == "k":
            engWord.append("k")
            x += 1
            conTrue = True
            continue
        
        #letter H Operations
        elif wordList[x] == "h":
            engWord.append("h")
            x += 1
            conTrue = True
            continue

        #letter L Operations
        elif wordList[x] == "l":
            engWord.append("l")
            x += 1
            conTrue = True
            continue

        #letter M Operations
        elif wordList[x] == "m":
            engWord.append("m")
            x += 1
            conTrue = True
            continue

        #letter N Operations
        elif wordList[x] == "n":
            engWord.append("n")
            x += 1
            conTrue = True
            continue
        
    return engWord

#variable list for main program
userWord = ""
select = "y"
engWord = ""
joinChar = ""
wordValid = False
run = True

print("**Hawaiian Word Pronunciation**")

while run == True:
    if select == "y":        
        userWord = input("Enter a Hawaiian Word: ")
        userWord = userWord.lower()
        wordValid = isHwn(userWord)
        if wordValid == False:
            print("This is not a valid Hawaiian word please try again")
        else:
            #valid word is passed to be translated, the returned list is joined into
            #the final string result
            engWord = hwnToEng(userWord)
            engWord = joinChar.join(engWord)
            engWord = engWord.capitalize()                              
            
            print(engWord)
            print("")
    elif select == "n":
        break
    
    select = input("Do you want to enter another word? (Y-Yes | N-No): ")
    select = select.lower()     
