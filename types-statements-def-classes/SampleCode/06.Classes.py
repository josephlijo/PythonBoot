# Class, Inheritance and method overriding in Python
# To run: 06.Classes.py

class Person():
    """Demoing the usage of class"""
	# Notice that we are using 'self' as it is a class
	# `Self` would refer to the instance of the class that we are referring to
    def greet(self):
        """Greet function"""
        print 'I am a person'
    def greet_with_message(self, message):
        """Function with parameter"""
        print 'This is a greeting', message

class Administrator(Person): # Example of inheritance
    """Demoing inheritance"""
    def greet(self):
        Person.greet(self)
        print 'I am an Administrator'

# Class usage
c = Person() # Instantiate a class or new up an instance. We don't need to use `new`.
c.greet()
c.greet_with_message("from Python class")

# Another instance of `Person`
d = Person()
d.greet_with_message("from John Doe")

# Inherited class
e = Administrator()
e.greet()
