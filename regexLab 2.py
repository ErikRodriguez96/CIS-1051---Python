#Erik Rodriguez - TUID: 915255369
#Section 001
import re

str = ""

print("PART 1 - NAMES")
print()

part1List = ["Satoshi Nakamoto","Alice Nakamoto","Robocop Nakamoto","satoshi Nakamoto","Mr. Nakamoto","Nakamoto","Robocop nakamoto"]
x = 0
for x in range (len(part1List)):
    
    str = part1List[x]
    print(str, " - ",end='')
    if re.search("^[A-Z][a-z]+\sNakamoto", str) != None:
        print(True)
    else:
        print(False)

print()
print("PART 2 - NUMBERS")
print()

part2List = ["twenty","twenty-one","thirty","thirty-two","sixty-six","eighty-three","ninety-nine","thirsty","thirsty-hungry"]
x = 0
for x in range (len(part2List)):
    
    str = part2List[x]
    print(str, " - ",end='')
    if re.search("twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety", str) != None:
        print(True)
    else:
        print(False)

print()
print("PART 3 - DOLLARS")
print()

part3List = ["$100.00","$10,000.00","$1234","$5000.00","$1,000,000","$1234.567","$50,00.00","$1,234.567","1234","#1234"]
x = 0
for x in range (len(part3List)):
    
    str = part3List[x]
    print(str, " - ",end='')
    if re.search("^\$(([1-9][0-9]{0,2}(,?[0-9]{3})*)|0)?(\.[0-9]{1,2})?$", str) != None:
        print(True)
    else:
        print(False)
