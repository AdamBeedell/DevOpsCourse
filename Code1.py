hellostring = "hello"
print(hellostring)
print(type(hellostring))

integ = 5
print(integ)
print(type(integ))

booleg = False
print(booleg)
print(type(booleg))

sumresult = integ + 5
print(sumresult)

try:
    hellostring+booleg
except:
    print("This fails")

checkresult = (hellostring==integ)
print(f"{checkresult} was saved as checkresult")


print("Part 2")

fivestr = "5"
fiveint = 5
str_int_check = (fivestr == fiveint)

print(str_int_check)

try:
    fivestr+fiveint
except:
    print("This fails")


print(5>5.5)
print(True==False)
print("hello" > "helloo")