# Class is Python
# To run: 06.Classes.py

class Person():
	def greet(self): # Notice that we are using 'self' as it is a class
		print 'I am a person'
	def greetWithMessage(self, message):
		print 'This is a greeting', message

		
c = Person()
c.greet()
c.greetWithMessage("from Python class")

