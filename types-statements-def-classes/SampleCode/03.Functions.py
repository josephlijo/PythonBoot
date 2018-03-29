# Functions in Python
# To run this file do: python 03.Functions.py

# Function without arguments
def func_without_args():
    """Function without arguments"""
    print 'This is function without arguments'

func_without_args()

# Function with arguments
def func_with_args(arg1, arg2):
    """Function which accepts two arguments"""
    print 'This function has arguments: ', str(arg1), ' and ', str(arg2)

func_with_args(1, 3)

def get_square_root(num):
    """Function which calculates square root of the passed in argument"""
    return num * num

def get_cube_root(arg1):
    """Function which calculates cube root of the passed in argument"""
    print 'The cube root is: ', str(arg1 * arg1 * arg1)

print get_square_root(3)
get_cube_root(2)
print get_cube_root(3) # Since there is no return value, it returns `None`

# Function with default parameters
def func_with_def_values(num1, num2=2):
    """Function which has default parameters"""
    print 'Value of argument 1 is ', num1, '; argument 2 is ', num2

func_with_def_values(1, 10)
func_with_def_values(2)
func_with_def_values(num1=20, num2=40)
func_with_def_values(num1=443)
#funWithDefaults(num2=99993) # This will give error as we haven't passed the required argument

# Function with variable number of arguments
def func_with_var_args(*args):
    """Function with variable number of arguments"""
    result = 0
    for item in args: # looping items in the argument list
        result = result + item
    return result

ADD_RESULT = func_with_var_args(1, 30, 2, 43)
print ADD_RESULT
