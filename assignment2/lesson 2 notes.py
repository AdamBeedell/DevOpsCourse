#Assignment 2
import datetime
now = datetime.datetime.now()
#print(now)
#print(now.day)
#print(datetime.datetime.today().weekday())

weekdaydict = {0: "Sunday",
               1: "Monday",
               2: "Tuesday",
               3: "Wednesday",
               4: "Thursday",
               5: "Friday",
               6: "Saturday"}

print(weekdaydict[datetime.datetime.today().weekday()])

name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John, and you are also 23")


alist = [1,2,3,4,5]
if 3 in alist:
    print(alist)

alist = [1,2,3,4,5]
print(alist[-1])

print(alist[len(alist)-1])

print(alist[-7])

nested = [[[[[[[[[[0]]]]]]]]]]
print(nested)

import itertools

def flatten_list(nested_list):
    return list(itertools.chain(*nested_list))

print(flatten_list(nested))


nested = [[[[[[[[[[0]]]]]]]]]]
layer=nested[0]
while isinstance(layer, list):
    layer=layer[0]
print(layer)

import random

Students = {}
IDs = set(range(11111111, 99999999))
randomID = random.choice(tuple(IDs))
IDs.remove(randomID)
len(Students)
Students[randomID] = {
        "name": "Adam",
        "age": 23,
        "payment_status": True
    }
print(Students)

def add_student(name, age, payment_status):
    Students.update()
    randomID = random.choice(tuple(IDs))
    IDs.remove(randomID)
    Students[randomID] = {
                 "name": name,
                 "age": age,
                 "payment_status": payment_status
                 }
    

for i in range(1,30):
    name = "B"+(i*"o")+"b"
    age = random.choice(range(18,90))
    payment_status = random.choice([False,True])
    add_student(name, age, payment_status)

print(Students)


#Students.append({"name": "Adam",
#                 "age": 23,
#                 "payment_status": True})