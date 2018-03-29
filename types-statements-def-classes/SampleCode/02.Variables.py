# This is a comment line
# Declare a variable and print it
F = 0
print int(F)

# Redeclare a variable and print it
F = "Hello from Python"
print F

# Python is strongly typed; below is the proof. 
# We cannot concatenate string and number
# print "Hello" + 123

# To solve it
print 'Hello' + str(123)

# Global and local variables
# Here the variable - local - is going to be in local scope; 
# To make it on Global scope, use the `global` keyword
def demo_local_variable():
    """A function to demonstrate the usage of local variables"""
    local_var = 'I am a local variable'
    print local_var

demo_local_variable()

# The below line will issue an error
# print local_var

def demo_global_var():
    """A function which demonstrate the usage of global variables"""
    global NOT_LOCAL_VAR
    NOT_LOCAL_VAR = ' I am a global variable '
    print NOT_LOCAL_VAR

demo_global_var()
print NOT_LOCAL_VAR

# To delete the definition of a variable that is previously created:
del NOT_LOCAL_VAR
print NOT_LOCAL_VAR # Will issue an error
