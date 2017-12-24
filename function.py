######## defining function 

def functionName( parameters ):
   "function_docstring"
   function_suite
   return [expression]

######### simple example of function  

def myFunction():
	return "Hello Python!!" 
	pass 

print myFunction()	# print function directly 
x = myFunction()	# store function in variable in x
print x				# print variable x

######## creating your own function to print
def printIt( str ):
	print str
	pass

######## passing a parameter in function
printIt("Passing this srting to print in my own function.")

######## Concatenating string example with parameter value
def appendFunction( mystr ):
	print "this is default value", mystr
  	pass  

appendFunction("and this is parameter value")

######### Example of Required arguments
def printme( str ):
   "This prints a passed string into this function"
   print str
   pass

# Now you can call printme function
printme() # this will through error // TypeError: printme() takes exactly 1 argument (0 given)
printme("But not this") # this will print // But not this  

######### Example of Keyword arguments

def keyArg( str ):
   print str
   pass

# Now you can call keyArg function
keyArg( str = "My string")

# you can pass multiple args 
def multiKeyArg( name, age ):
   print "Name: ", name
   print "Age ", age
   pass

# Now you can call multiKeyArg function
multiKeyArg( age=22, name="Rajnish" )

# The return Statement
def returnFun(arg1, arg2):
	returnArg = arg1 + arg2
	return returnArg
	pass

print(returnFun(10, 10))
# you can store it in another variable too
returnStorage = returnFun(10, 10);
print(returnStorage);