#using for loop
list = ["lasya","sree","valluri"]
for x in list:
    print(x)
    #another way
for x in "banana":
    print(x)
    #using break to stop the loop
list =["apple","mango","banana","cheery"]
for x in list:
    print(x)
    if x =="banana": 
      break
 #another way
list =["kavya","sujatha","chinnari"]
for x in list:
    if x=="sujatha":
        break
    print(x) 
    #using continue statement
list=["a","b","c","d"]
for x in list:
    if x =="b":
        continue
    print(x)
    #range() function
for x in range(1,9):
    print(x)
    #three parameters pass chasinapudu
for x in range(2,30,3):
    print(x)
    #else in for loop
for x in range(6):
    print(x)
else:
    print("finally finished")
    #another way
for x in range (6):
    if x ==3:
        break
    print(x)
else:
    print("finish")
    #nested loop
list1=["apple","mango","banana"]
list2=["red","blue","green"]
for x in list1:
    for y in list2:
        print(x,y)