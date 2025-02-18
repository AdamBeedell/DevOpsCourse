#A
x = 1
y = 2
if x > y:
    print("BIG")
elif x < y:
    print("small")

#B
for i in range(1,5):
    print(i)

#C
import random
season = random.randint(1,4)
if season == 1:
    print("spring")
elif season == 2:
    print("summer")
elif season == 3:
    print("autumn")
elif season == 4:
    print("winter")

#D

#9
#10

count = 1
while count <11:
    print(count)
    count=count+1


#E

age = 32
fl = "B"
wat = 50
flying = True
apt = None

print(age)
print(fl)
print(wat)
print(flying)
print(apt)

print (age+wat)

#f

print("what is your phone number?")
numba = input()
print(f"Your number is {numba}")

#g

def printHello():
    print("Hello")

def calculate():
    print(5+3+2)


#h

def echoecho(string):
    print(string)

def divby2(num):
    if isinstance(num, int):
        print(num/2)
    else:
        print("error")


#i

def add2(num, num2):
    if isinstance(num, int) and isinstance(num2, int):
        print(num+num2)
    else:
        print("error")

def concatwspace(strang, strang2):
    print(f"{str(strang)} {str(strang2)}")


#j

listy = [1,2,3]

for num in listy:
    print (num)


#k 

print(sum(listy))

#l

uberdict = {}
uberdict["bob"] = {"one": "bobby"}
uberdict["jeff"] = {"two": "jeffy"}

for key in uberdict:
    #print(key)  ## hash or unhash depending on interpretation of the question
    for key2 in uberdict[key].keys():
        print(key2)


#m

for i in range(1,6):
    print("#"*i)


#n
box = []
y=7
x=7
for i in range(0,y):
    line=[]
    for i2 in range(0,x):
        line.append(" ")   ### no idea what the nested one needed to do really
    line[i] = "#"
    line[-i-1] = "#"    
    box.append(line)

for line in box:
    print("".join(line))

#o

def getnumba():
    print("multiple digit int plz")
    numba = input()
    if len(str(numba)) > 1:
        print(f"Your number is {numba}")
        return numba
    else:
        print("fail")
        return 25

def adddigits():
    numba = getnumba()
    maf = 0
    for inty in str(numba):
        maf+=int(inty)
    return maf
     

print(adddigits())


#p 
 
tup = ('h', 'e', 'l', 'l', 'o')

stringy = ""

for item in tup:
    stringy = stringy+item

print(stringy)

#q

listy=[9,2,3,4,1,6]
listy.sort()
print(listy[0])

## alternatively

min=999999999
for item in listy:
    if item<min:
        min=item
print(min)

