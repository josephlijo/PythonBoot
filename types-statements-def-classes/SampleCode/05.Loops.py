# Loops in Python
# To run: python 05.Loops.py

# While loop

def func_with_while():
    """Function demonstratin the usage of `while` loop"""
    x, y = 1, 10
    print 'This is a while loop'
    while x < y:
        print x
        x = x + 1

def func_with_for():
    """Function demoing the usage of `for` loop"""
    x, y = 4, 8
    print 'This is a for loop'
	# This will print from 4 through 7
    for item in range(x, y):
        print item

def func_with_collection():
    """Function demoing collection"""
    collection = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in collection:
        print day

def func_with_break_continue():
    """Function demoing the usage of `break` and `continue`"""
    collection = [7, 1, 2, 4, 3, 9]
    for item in collection:
        if item % 2 == 0:
            continue # Skips the rest of the loop
        if (item == 1 or item == 9):
            break # Breaks the loop
        print item

def enum_for_index_value():
    """Function demoing enumeration"""
    collection = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for x, y in enumerate(collection):
        print x, y

if __name__ == "__main__":
    func_with_while()
    func_with_for()
    func_with_collection()
    func_with_break_continue()
    enum_for_index_value()
