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
- `type(1)` is `<class 'int'>`

### Strings
- By default strings are **Unicode text in Python3** and **ASCII text in Python2**.
- String's can be defined by single, double, or triple quotes.
- Triple quotes (""") are normally used to represent doc-types to give documentation for your statement / functions
- `String` is of type `class str`
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

## Control flow statements

### If Statements
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

### for Statements
- To loop over a list of items, we can use `for ... in`
```
>>> fav_tools = ["Java", "Python"]
>>> for tool in fav_tools: # There will be 2 iterations here and we don't control the index
...   print(tool, len(tool))
...
Java 4
Python 6
```
- To loop over and insert an item, it is recommended to loop over a copy which could be done by slicing (`[:]`)
```
>>> fav_tools = ["Java", "Python"]
>>> for tool in fav_tools[:]:
...   if tool != "JavaScript":
...     fav_tools.insert(0, "JavaScript")
...
>>> fav_tools
['JavaScript', 'JavaScript', 'Java', 'Python']
```
- `for ... in` can be used with `List` type and strings; Python *abstract away the underlying type while using for...in*
```
>>> name = "Bond"
>>> for letter in name:
...   print(letter)
...
B
o
n
d
```
- There can be cases where we need to know the *index* and other underlying details while doing iteration; in this case, we can use `range()` function  
sometimes in combinatin with `len()`
```
>>> i = 0
>>> for index in range(5):
...   i += index
...   print("index is {0}; i is {1}".format(index, i))
...
index is 0; i is 0
index is 1; i is 1
index is 2; i is 3
index is 3; i is 6
index is 4; i is 10
```
- **Starting from zero index and iterating n times**: Here `range(5)` starts from 0 and goes all the way till *index < 5*  
- **Starting from a specified index**: We can specify a starting index to `range`, say to start from 2 and iterate 3 times: range(2, 5)  
- **Each iteration to move a specific index**: For example, *start from 0, increment 2 for 5 times* is
```
>>> for index in range(0, 10, 2):
...   print("index is {0}".format(index))
...
index is 0
index is 2
index is 4
index is 6
index is 8
```

### Break and Continue
- `Break` keyword can be used to **break out of a loop and stop further iteration**
```
>>> fav_tools = ["Java", "JavaScript", "C"]
>>> for tool in fav_tools:
...   if tool == "JavaScript":
...     print("Found JavaScript")
...     break # <-----------------------
...   print("Current tool is {0}".format(tool))
...
Current tool is Java
Found JavaScript
```
- `Continue` keyword can be used to **continue the iteration and skip the logic after `continue` check inside a loop**
```
>>> # Don't do anything specific for "me"
... starts = ["I", "me", "they", "you"]
>>> for item in starts:
...   if item == "me":
...     continue
...   print("I met {0}".format(item))
...
I met I
I met they
I met you
```

### While loops
- To execute some logic *while a condition is met* - we can use `while` loop; `while` loops are useful as they checks the condition before even they enter the loop. It is up to coder to *control the iteration* unlike in `for ... in` - so be **careful not to cause infinite loops**.  
`Break` keyword becomes more useful sometimes in `while always true` if we need to run *a piece of logic until a condition is met*.  
Example of `while` loop usage: 
```
>>> rank = 10
>>> while rank < 20:
...   print("Rank is {0}".format(rank))
...   rank += 5
...
Rank is 10
Rank is 15
```


## Data structures

### List
- List can hold *dynamic types*, for example, *string*, and *number* (though this is not good in any good scenario)
- List holds a series of values and the values can be accessed by using *index*
```
>>> fav_tools = ["JavaScript", "Python", "C"]
>>> print(fav_tools[0])
JavaScript
```
- Indexing **starts with 0** and to access the last element we can also use *-1* and previous element by **-1-1 = -2**  
Note: there is no *-0* though indexing starts with *0*
```
>>> fav_tools = ["JavaScript", "Python", "C"]
>>> fav_tools[-1]
'C'
>>> fav_tools[-2]
'Python'
```
- `List` can be used as `Stack` data structure by `append`ing to the end of the list (`push`) and `pop`ing which removes the item at the end of the list - **LIFO** by `append` and `pop`
- `List` can also be used like a `Queue` - **FIFO**, but it is not so efficient as once the item is removed (**dequeued**) from the *start* of a `List` the other items [needs to be shifted by one](https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues).

**List functions**
- *append* to append to the end of a list `fav_tools.append("C#")`
- To *check existence* `"C#" in fav_tools`
- To check the length, pass in the list to `len` function `len(fav_tools)`
- To delete an item we use `del` keyword and for iteration we can use `for ... in`:
```
>>> del fav_tools[0]
>>> for i in fav_tools:
...   print(i)
```
- *List slicling* or *skipping* can be done by specifying number of elements to skip **[n:]** or **[n:-n]** (Note: List is not modified in this case)
```
>>> fav_tools = ["Java", "JavaScript", "Python"]
>>> fav_tools[1:]
['JavaScript', 'Python']
```

### Dictionary
- `Dictionary` holds key-value pairs as an item
- The *value* can be of any type in a dictionary
- Example: 
```
>>> person = {
...   "name": "Foo",
...   "age": 20
... }
>>> print(student)
{'name': 'John', 'age': 20}
>>> for item in student:
...   print(item)
...
name
age
```
Note: the iteration printed the `key` only
- **Nested dictionaries* are when we have value as another dictionary
- Useful when working with `JSON` as it is structured similar
- *List of dictionary* is *similar to array of objects in JavaScript*
```
>>> person_list = [
...    {"name": "Foo", "age": 20},
...    {"name": "Bar", "age": 22}
... ]
```
- Access value **by passing key**: 
```
>>> person = {"name": "Foo Bar", "age": 20}
>>> person["name"]
'Foo Bar'
```
- Access value **by using `get`**: 
```
>>> person.get("name")
'Foo Bar'
```
- Note `KeyError` can occur if we access non-existing key:
```
>>> person["first_name"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'first_name'
```
- `KeyError` can be prevented by passing a second argument to `get`:
```
>>> person.get("first_name", "Not valid")
'Not valid'
```
- To **get all values**: `person.values()` which returns *dict_values(['Foo Bar', 20])*
- To **insert / update**: `person["newKey_or_existing_key"] = value`
- To **delete** an item: `del person["name"]`

## References
- [Python Data structures](https://docs.python.org/3/tutorial/datastructures.html)
