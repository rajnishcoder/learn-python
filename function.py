# defining function 

def functionName( parameters ):
   "function_docstring"
   function_suite
   return [expression]

# simple example of function  

def myFunction():
	return "Hello Python!!" 
	pass 

print myFunction()	# print function directly 
x = myFunction()	# store function in variable in x
print x				# print variable x

# creating your own function to print
def printIt( str ):
	print str
	pass

# passing a parameter in function
printIt("Passing this srting to print in my own function.")

# Concatinating string example with parameter value
def appendFunction( mystr ):
	print "this is default value", mystr
  	pass  

appendFunction("and this is parameter value")