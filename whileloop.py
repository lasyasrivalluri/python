#using while loop
i=1
while i<6:
    print(i)
    i +=1
    #using break in while loop
i=1
while i <6:
    print(i)
    if i == 3:
        break
    i += 1
    #using continue statement we can stop the current iteration
i=0
while i<6:
    i+=1
    if i == 3:
        continue
    print(i)
    #using else statementin while loop
i=0
while i <6:
    print(i)
    i +=1
else:
    print("i is no longer less than 6")    
