## assignment 1

first = 7
second = 44.3
print(first+second)
print(first*second)
print(second/first)

maf = """
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
"""

ans = "a=9, b=8, c=15"

## check 

a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8

print(f"a={a}, b={b}, c={c}")

print (f"a={a}, b={b}, c={c}" == ans)


### believed to be equal, though the IDE didnt like those original quotes. no diff until you add more quotes in the string.
name = "john"
name2= 'john'
print(name == name2)

## 'john's' =/= "john's"

##
#What is the issue with the code below?
#my_number = 5+5
#print("result is: "+my_number)
#Suggest an edit.

ans = "str+int no work"
num = 5+5
print(f"result is: {num}")

x = 5
y = 2.36

## expecting it to round up or down on the int constructor as no decimals allowed
## Guess: 7

print (x+int (y) )

## confirmed 7

if x>y:
    print("BIG")
else:
    print("small")

import random as random
season=random.choice([1,2,3,4])
print(season)

seasons = {1: "Spring",
           2: "Summer",
           3: "Autumn",
           4: "Winter"}

print(seasons[season])


if season == 1:
    print("Spring")
else:
    if season == 2:
        print("Summer")
    else:
        if season == 3:
            print("Autumn")
        else:
            if season == 4:
                print("Winter")
            else:
                print("Fail")


#Fix the following code without changing a or b:

a = 8
b = "123"
print(a+int(b))
#or
print(str(a)+b)

