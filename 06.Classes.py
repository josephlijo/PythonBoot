# Class, Inheritance and method overriding in Python
# To run: 06.Classes.py

class Person():
	# Notice that we are using 'self' as it is a class
	# `Self` would refer to the instance of the class that we are referring to
	def greet(self): 
		print 'I am a person'
	def greetWithMessage(self, message):
		print 'This is a greeting', message

class Administrator(Person): # Example of inheritance
	def greet(self):
		Person.greet(self)
		print 'I am an Administrator'
		
c = Person() # Instantiate a class or new up an instance. We don't need to use `new`.
c.greet()
c.greetWithMessage("from Python class")

# Another instance of `Person`
d = Person()
d.greetWithMessage("from John Doe")

# Inherited class
e = Administrator()
e.greet()

