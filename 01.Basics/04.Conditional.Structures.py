# Conditional structures in Python
# To run this file: python 04.Conditional.Structures.py

# Usage of `if` 

def main():
	x, y = 10, 20
	
	if (x < y):
	  print 'x is less than y'
	elif (x > y):
	  print 'x is greater than y'
	else: 
	  print 'x and y are both equal'

# Using conditional statements in Python
# a if C else b

def con_state(x, y):
	print 'x is less than y' if (x<y) else 'x is greater than or equal to y'
	
if __name__ == '__main__':
	main()
	con_state(1,2)
	con_state(2,1)
	con_state(2,2)