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
>>> "123".isdigit() # Useful when converting to int
True
>>> "Hello" == 'Hello'
True
>>> "Hello" == """Hello"""
True
>>> "Foo,Bar,21".split(",") # Useful when working with CSV files
['Foo', 'Bar', '21'] # gets a List
```
- Formatting
```
>>> "Name: {0}; Position: {1}".format("John Doe", "Software Engineer")
'Name: John Doe; Position: Software Engineer'
```
- Formatting via **String Interpolation**
```
>>> name = "Sarah Doe"
>>> position = "Manager"
>>> f"Please meet {name}, the {position} of XYZ company"
'Please meet Sarah Doe, the Manager of XYZ company'
```

### Booleans and **None**
- Indicates `True` or `False`
```
>>> task_completed = True
>>> int(task_completed) == 1
True
```
- Python also has `NoneType` represented by `None`. It can be used as place-holder values.  
If we declare a variable and don't assign any value, Python interpreter results in error, which can be avoided by using `None`
```
>>> task_completed = None
>>> time_to_complete
NameError: name 'time_to_complete' is not defined
```

## Conditional statements

### If statements
- If statements check conditions and can be clubbed with else block
```
>>> number = 5
>>> if number == 5:
...   print("Number is 5")
... else:
...   print("Number is not 5")
...
Number is 5
>>>
```
- In Python, the interpreter evaluates the statement based on indentation, not by the presence of curly braces or other characters
- The `if` and `else` statement both ends with `:`, which is also a requirement in Python
- `==`, double equality is used to check the values
- `is` can be used to check if two objects are pointing to same location in memory  

**Truthy and Falsy values**
- Example:
```
>>> num = 11
>>> if num:
...   print("num variable is defined and hence it is truthy")
...
num variable is defined and hence it is truthy
>>> txt = "Hello"
>>> if txt:
...   print("txt variable is defined and hence it is truthy")
...
txt variable is defined and hence it is truthy
>>>
```
- Number variables which holds **value other than zero are truthy**
- Text variables which **doesn't have empty string is truthy**
- We could make use of this to check if the *value is defined*
- These check can also be done against *Boolean* and *None* type. *True value is truthy* and *None type is falsy*

**!= and not**
- We can use *!=* to check it is *not a value*
- *not* keyword can be used for evaluating against
- Example,
```
>>> number = 2
>>> if number != 3:
...   print("Number is not 3")
...
Number is not 3
>>> is_python = True
>>> if not is_python:
...   print("Is not Python")
... else:
...   print("Is Python")
...
Is Python
```

**Multiple conditions**
- *and*, *or* keywords can be used for checking against multiple conditions:
```
>>> ranking = 10
>>> is_valid = True
>>> if ranking == 10 and is_valid:
...   print("Order is successful")
...
Order is successful
```

**Ternary If statements**
- Compared to other languages which uses *?* to check and evaluate one or other statement, Python uses a different format:
```
>>> a = 1
>>> b = 2
>>> "a is bigger" if a > b else "b is greater than a"
'b is greater than a'
```
