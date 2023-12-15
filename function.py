# creating a function
def function_name():
    print("hello from a function")
function_name() #function call 
#passing arguments
def function(fname):
    print(fname + " lasya")
function("name")
function("surname")
function("last name")
#passing number of arguments
def function_name1(fname,lastname):
    print(fname+" "+lastname)
function_name1("lasya","sree")
function_name1("punitha","sree")
#yani arguments pass chayalo thaliyaka pothey apudu *ni use chasthey chalu
def abc(*toys):
    print("the younger child is" +toys[2])
abc("lasya","sri","valluri")
#key=value niuse chasi kuda arguments ni pass chayavachu
def xyz(child1,child2,child3):
    print("your chid is"+ " "+child3)
xyz(child1="lasya",child2="suji",child3="punitha") 
#return values
def my_function(x):
    return 5+x
print(my_function(5))
print(my_function(3))
print(my_function(6))

