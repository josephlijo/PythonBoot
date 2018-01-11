# Loops in Python
# To run: python 05.Loops.py

# While loop

def aWhileLoop():
  x, y = 1, 10
  print 'This is a while loop'
  while(x < y): 
	print x
	x = x + 1
	
def aForLoop():
	x, y = 4, 8
	print 'This is a for loop'
	# This will print from 4 through 7
	for item in range(x,y):
	  print item

def aCollectionLoop(): 
	collection = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	for day in collection:
		print day
		
def aBreakAndContinue():
	collection = [7, 1, 2, 4, 3, 9]
	for item in collection: 
		if (item % 2 == 0): continue # Skips the rest of the loop
		if (item == 1 or item == 9): break # Breaks the loop
		print item
		
def enum_for_index_value():
	collection = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	for x,y in enumerate(collection): 
		print x, y;

if "__main__" == __name__: 
	#aWhileLoop()
	#aForLoop()
	#aCollectionLoop()
	#aBreakAndContinue()
	enum_for_index_value()