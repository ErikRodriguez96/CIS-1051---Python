#Erik Rodriguez - TUID:915255369
#Section 001

def findFirstVowel(word):
    #x is the location of the first vowel
    #x = 100 is the default state and remains this way if there is no vowel
    x = 100

    if word.find('a') != -1 and word.find('a') < x:
        x = word.find('a')
    if word.find('e') != -1 and word.find('e') < x:
        x = word.find('e')
    if word.find('i') != -1 and word.find('i') < x:
        x = word.find('i')
    if word.find('o') != -1 and word.find('o') < x:
        x = word.find('o')
    if word.find('u') != -1 and word.find('u') < x:
        x = word.find('u')
    return x

def convertToPigLatin(word):
    i = findFirstVowel(word)
    
    #findFirstVowel returns 100 if there's no vowel
    if i == 100:
        word = word + "way"
        return word
    else:
        firstVowel = word[i]

    #we check to see if the first letter is a vowel or not
    #depending on this we do either of the two following sequences
    if i == 0:
        sliceFirst = slice(1,len(word))
        word = word[sliceFirst]
        word = word + firstVowel + "way"
        return word
    else:
        sliceFirst = slice(0,i)
        sliceLast = slice(i, len(word))
        wordFirst = word[sliceFirst]
        word = word[sliceLast]
        word = word + wordFirst  + "ay"
        return word

    
def main():
    userWord = ""
    while(userWord != "done"):
        userWord = input("Please input a word: ")
        userWord = userWord.lower()
        if userWord == "done":
            break
        convWord = convertToPigLatin(userWord)
        print("Converted word is : " + convWord)
        
main()
    
