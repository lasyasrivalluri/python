# if statement
number = 8
if number < 4:
    print(number* number)
#if-else statement
number = 8
if number < 4:
    print(number* number)
else:
   print(number+number)
#if-elif-else statement
def user_check(choice):
    if choice == 1:
        print("admin")
    elif choice ==2:
        print("editor")
    elif choice ==3:
        print("guest")
    else:
        print("wrong enter")
user_check(1)
user_check(2)
user_check(3)
user_check(4)

#nested if-else statement
x=60
if x > 10:
    print("above 10")
    if x < 20:
        print("above 20")
    else:
        print("not above 50")

# for loop
fruits=["apple","mango","banana"]
for x in fruits:
   print(x)
#for loop using break
fruits=["apple","banana","mango"]
for x in fruits:
    if x == "banana":
       print(x)
       break
#for loop direcly
for x in "lasya":
    print(x)
#for loop using continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#for loop using range
for x in range((10)):
    print(x)
#for loop using ranges
for x in range(2, 6):
  print(x) 
#for loop using ranges
for x in range(2,30,3):
  print(x) 
#while loop
i=1
while i <10:
   print(i)
   i +=1
