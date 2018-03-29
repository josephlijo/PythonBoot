# Types, statement, functions and classes

This section holds the basic python concepts and code scripts.  
To run the script, run `python *filename*` in your favorite command line tool

## Data types in Python && **Type Hinting**
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
