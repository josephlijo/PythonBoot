# Functions in Python
# To run this file do: python 03.Functions.py

# Function without arguments
def funWithoutArgs():
	print 'This is function without arguments'

funWithoutArgs()

# Function with arguments
def funWithArgs(arg1, arg2): 
  print 'This function has arguments: ', str(arg1), ' and ', str(arg2)

funWithArgs(1, 3)

def getSquare(num):
  return num * num

def getCube(arg1):
	print 'The cube root is: ', str(arg1 * arg1 * arg1)

print(getSquare(3))
getCube(2)
print(getCube(3)) # Since there is no return value, it returns `None`

# Functions with default parameters
def funWithDefaults(num1, num2 = 2):
  print 'Value of argument 1 is ', num1, '; argument 2 is ', num2

funWithDefaults(1, 10)
funWithDefaults(2)
funWithDefaults(num1=20, num2=40)
funWithDefaults(num1=443)
#funWithDefaults(num2=99993) # This will give error as we haven't passed the required argument

# Function with variable number of arguments
def multiAdd(*args): 
  result = 0
  for item in args: # looping items in the argument list
	result = result + item
  return result
  
addResult = multiAdd(1, 30, 2, 43)
print(addResult)