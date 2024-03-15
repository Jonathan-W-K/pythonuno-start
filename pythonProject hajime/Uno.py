# this is a sigle line comment
"""
this is a multiline comment
"""
# variables
Name = "Shikigami"
Age = "18"  # data type is integer
Mark_awarded = "98.0"  # data type is float
is_male = "true"  # data type is boolean

# outputting the values in the variables
print(Name)
print(Age)
print(Mark_awarded)

# variable naming in python
book_price = float(input("Enter book price: 50.00"))
# noinspection PyRedeclaration
book_price = "50.00"

"""
when naming the variables you cannot
 start with numbers or anything else
  apart from letters and '_' (Underscore) 
"""

x = z = y = 50  # assigning multiple variables the same value
x, y, z =30, 40, 70 # assigning variables different values

if constituency == "Embakasi" or "Kasarani" or "Westlands":
    print("Viable Candidate")
else:
    print("Not Viable Candidate")

result = "total is :" + str(total) + "KSH"

X=27
Y=2
I=X % Y
if I == 1 :
      print("X is odd NO.")
else:
      print("X is even NO.")
NAme = ["Hesbon", "Majid", "Ryan", "Mike", ""]
for x in NAme:
    print(x)
    if x == "Ryan":
        break

# break ita fika na i simame hapo

x=0
while x<=5 :
  print("Shinee")
  x+=1

"""
x=0
while x<=5
  print("Shinee)
  x+=1
"""

# CONTINUE ikifikia chenye unataka itaruka iendele
I=0
while I < 6 :
 I +=1
 if I == 3:
  continue
 Print(I) 

#if...else example
age = 18 
if age >= 18: 
print('You are eligible to vote. ')
else: print('You are not eligible to vote. ') 
# Output: # 'You are eligible to vote.

country=input("Name of country:")
if country == "Kenya":
    print("East Africa")
elif country == "UG":
    print("East Africa")
elif country == "Rwanda":
    print("East Africa")
elif country == "TZ":
    print("East Africa")
elif country == "Ethiopia":
    print("East Africa")
else:
    print("Not in the database")

x = 1
while x <= 10:
    if x == 3:
        x += 1
        continue
    print("type your number:", x)
    x += 1
else:
    print("end")


x = 1
while x <= 10:
    if x == 3 or x == 5:
        x += 1
        continue
    print("type your number:", x)
    x += 1
else:
    print("end")

# there is a problem here ask later
z=0
s=1
while s <= 10:
        if s % 2 != 0:
                z += s
                s += 1
                print(s)

"""
# ask later
KE = 0
UG = 0
while KE >= 0 and UG >= 0:
    input("Are you Kenyan?:")
    if input("Are you Kenyan?") == "yes":
        KE = KE + KE
        continue
    elif input("Are you Kenyan?") == "no":
        UG += UG
    print(KE + UG)
"""

"""
NAme = ["Hesbon", "Majid", "Ryan", "Mike", ""]
for x in NAme:
    print(x)
    if x == "Ryan":
        break



for y in range(1,6):
    print("y")
"""
"""
sum_odd=0
for i in range(10):
    if i%2!=0:
         sum_odd += i
         print("sum is:", sum_odd)
"""

"""
t=0
n=10
for i in range(1,11,2):
    t+=n
    print(t)
"""

# students= list(["Hesbon", "Majid", "sdfgj"])
# print(students)
"""
students = list()  # empty list
#print(students)
students = ["Hesbon", "Majid", "sdfgj"]  # full list
#print(students)
students.remove("Majid")
print(students)
"""

p=[input("Enter Name:"), input("Enter Name:"), input("Enter Name:")]
print(p)
