# Python Boot
A repository intended to learning Python or refresing the knowledge.

## What can I use Python for?
- Python is open source programming language
- It is strongly typed language in the sense every object in the language has a definite type, and generally there is no way to circumvent that type
- It is dynamically typed, meaning there is no typing checking of your code prior to running it; This is in contrast to statically typed languages like C++, Java where compiler does lot of type checking for you rejecting misused objects. 
- Python uses **duck typing** - where an objects suitability for a context is only determined at run time. 
- Python is an interpreted language; Python is normally compiled into byte code before it is executed; however this compilation happens invisibly - i.e. there isn't noticable compilation phase and hence we see Python as interpreted language 
- Python uses white space to delimit code blocks
- There are multiple implementation of Python: 
  - The version written in C is called CPython - the commonly used one 
  - Jython written in Java to target JVM
  - IronPython written in C# to target .NET runtime
  - pypy which is written in specialized subset of Python called RPython
- *Batteries included* which means that you can use Python straightaway without needing to install third party packages. Python comes with Python Standard Library. 
- Python is portable language, meaning we can use it in all different Operating Systems like, for example, Windows, Linux, and Mac OS
- It can be used to build:
  - Scripts
  - Console applications
  - Desktop applications
  - Web back-ends
  - Scientific computations
  - Home Automation
  - Machine Learning or Artificial Intelligence apps
- Use-cases?
  - Cross-platform desktop application which has the same look in different OS
  - Automate something, say parsing a CSV file? - Use Python scripts
  - App which recognizes pictures and categorize them? Use Python with TensorFlow library
  - Youtube, Instagram, Reddit, and Dropbox are using Python web frameworks such as [Django](https://www.djangoproject.com/), [Flask](http://flask.pocoo.org/), or [Pyramid](https://trypyramid.com/).
  - Scientific computing using libraries such as [Astropy](http://www.astropy.org/), [Biopython](https://biopython.org/), [Numpy](http://www.numpy.org/), [Scipy](https://www.scipy.org/)
  - Python also is useful for cloud configuration. [Ansible](https://www.ansible.com/), [Boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for Amazon Web Services, [Azure Python SDK](https://docs.microsoft.com/en-us/python/azure/?view=azure-python)
  - Data analysis, visualization and Machine Learning using - [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Bokeh](https://bokeh.pydata.org/en/latest/), [Tensorflow](https://www.tensorflow.org/), [scikit-learn](http://scikit-learn.org/stable/) 

## import this - Zen of Python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>

## Python 2 vs. Python 3
- Python 3 is not backward compatible with version 2. However, both can co-exist on the same machine (python --version && python3 --version).
- Python 2 is given extended [EOL (end-of-life) by 2020](https://pythonclock.org).

## Installing Python and IDE
- Installation can be done on Mac OS, PC, and Linux machines
- Python installation installs the Python Interpreter and it also comes with standard IDLE - a Python IDE
- Check the installation by checking the version in any CLI `python --version`
- We can also install a free Python IDE - [PyCharm](https://www.jetbrains.com/pycharm/)

### Installation on Windows
- Head to python.org -> Downloads -> Windows 
- Make sure that you add Python to PATH environment variable so that it is accessible from a shell 
- After installation, open up a PowerShell windows and type `python` to get to the triple arrow point for input >>>

### Installation on macOS
- Although macOS might include a Python version, it might be the legacy 2.x version. So, head over to python.org -> Download -> Mac .. -> Install the package
- After installation, cleanup the installer to trash 
- Open terminal, and type `python3` to see the triple arrow point for input >>> 

## REPL - Read, Evaluate, Print, Loop
- Python CLI is a REPL environment which will read the statement that we type in, evaluate it, print the results, and then loop back to the top of where we started. 

PS C:\WINDOWS\system32> py
Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 4 <----- Read, Evaluate
5         <----- Print
>>>       <----- Loop

- Another with variable and recently printed value
>>> x = 1
>>> x
1
>>> x = 2
>>> x
2
>>> _ <----- recently printed value
2
>>>

- Python uses indentation to differentiate the code blocks (default is *4 white spaces*); terminate with blank line and space and enter 
- colon : makes a difference - meaning the next line needs indendation and leading to a clear readability
- Prefer spaces (four spaces) to tabs; never mix
- indentation idea is good against curly braces scenario - for example, we can avoid curly braces in single line following an if and we can include it - in Python we just leave it to single way - don't use it - much readable for humans and computers

## PEP - Python Enhancement Proposals
- Future ideas and proposals to be included in Python version
- PEP's are not only about feature proposals, but development proposals too (for example how we should developer friendly atmosphere of code) >>> *import this*

## Python Standard Library - Batteries Included
- Python comes with library - which is structured as **modules** 
- We get access to standard library modules using the **import** keyword - `import module_name` 
- To import a module for math, we use `import math` and for further drilling down we use `math.something` and for understanding further about the module `help(math)`
PS C:\WINDOWS\system32> py
Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> print(math.sqrt(9))
3.0
>>> help(math)
Help on built-in module math:
...
- Factorial for example
>>> math.factorial(3)
6
>>> help(math.factorial)
Help on built-in function factorial in module math:

factorial(...)
    factorial(x) -> Integral

    Find x!. Raise a ValueError if x is negative or non-integral.

>>>
- ways to improve import and readability. There are: 
  - from math import factorial
    - and then we use factorial(3)
  - from math import factorial as fac
    - and then we use fac

## Learning
- [Types, statements, functions, classes](./types-statements-def-classes)
