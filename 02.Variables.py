# This is a comment line
# Declare a variable and print it
f = 0
print f

# Redeclare a variable and print it
f = "Hello from Python"
print f

# Python is strongly typed; below is the proof. 
# We cannot concatenate string and number
# print "Hello" + 123

# To solve it
print 'Hello' + str(123)

# Global and local variables
# Here the variable - local - is going to be in local scope; 
# To make it on Global scope, use the `global` keyword
def demoLocal(): 
  local = 'I am a local variable'
  print local
  
demoLocal()
# The below line will issue an error
# print local

def demoGlobal(): 
  global notLocal 
  notLocal = ' I am a global variable '
  print notLocal

demoGlobal()
print notLocal

# To delete the definition of a variable that is previously created:
del notLocal
print notLocal # Will issue an error