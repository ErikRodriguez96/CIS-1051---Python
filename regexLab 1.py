#Erik Rodriguez - TUID: 915255369
#Section 001
import re

words = open(r"words.txt","r")
str = ""

(val1A, val1B, val2, val3, val4A, val4B, val5, val6, val7, val8, val9, val10) = 0,0,0,0,0,0,0,0,0,0,0,0

for line in words:
        str = line.lower()
        if (re.search("cat", str)) != None:
                val1A += 1
        if (re.search("dog", str)) != None:
                val1B += 1
        if (re.search("^....$", str)) != None:
                val2 += 1
        if (re.search("hun", str)) != None:
                val3 += 1
        if (re.search("ing$", str)) != None:
                val4A += 1
        if (re.search("ion$", str)) != None:
                val4B += 1
        if (re.search("q[^u]", str)) != None:
                val5 += 1
        if (re.search("^[^aeiou]+$", str)) != None:
                val6 += 1
        if (re.search("^[aeiou]+$", str)) != None:
                val7 += 1
        if (re.search("'nt$", str)) != None:
                val8 += 1
        if (re.search("[aeiou]{2}", str)) != None:
                val9 += 1
        if (re.search(".*[aeiou].*[aeiou].*", str)) != None:
                val10 += 1
                
print("[1] Dog and Cat: ",val1A + val1B)
print("[2] 4 Letter Words: ",val2)
print("[3] Hun : ", val3)
print("[4] ing Words: ", val4A, "| ion Words: ", val4B)
print("[5] q not followed by u: ", val5)
print("[6] Words with no vowels: ", val6)
print("[7] Words made of only vowels: ", val7)
print("[8] \"not\" contractions (nt): ", val8)
print("[9] 2 vowels in a row: ", val9)
print("[10] 2 vowels at least: ", val10)

