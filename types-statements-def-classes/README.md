# Types, statement, functions and classes

This section holds the basic python concepts and code scripts.  
To run the script, run `python *filename*` in your favorite command line tool

## Data types in Python & **Type Hinting**
- Python is a **dynamically typed language** - which means that we don't have to give the variables a type beforehand
- Python interpreter will interpret it
```
whole_number = 1
string_e = "A string"
```
- This causes problems for example if a function expects two whole number for doing addition, but we pass in a whole number and a string instead
```
def add_numbers(a, b):
  return a + b
add_numbers(whole_number, string_e)
```
- **Type Hinting**, a new feature added in v 3.5 can help around this. Note that, it is help (hint) for IDEs or editors, not the interpreter.
```
def add_numbers(a: int, b: int) -> int:
  return a + b
```

### Integers and Floats
- Integers are whole numbers (+, 0, -) and floats are numbers with decimal points
```
a = 42 # Integer
b = 3.5 # Float
a + b # 45.5
```
- Casting can be done:
```
float(a) # 42.0
int(b) # 3
```

### Strings
- By default strings are **Unicode text in Python3** and **ASCII text in Python2**.
- String's can be defined by single, double, or triple quotes.
- Triple quotes (""") are normally used to represent doc-types to give documentation for your statement / functions
```
>>> "hello".capitalize()
'Hello'
>>> "hello".replace("e", "a")
'hallo'
>>> "hello".isalpha()
True
>>> "hello".isdigit()
False
>>> "123".isdigit()
True
>>> "Hello" == 'Hello'
True
>>> "Hello" == """Hello"""
True
```
