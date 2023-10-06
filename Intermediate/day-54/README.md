## Introduction to Web Development With Flask
- Command Line
- Python Decorators
- Web Development with Flask

 In order to build a website which has a frontend and a back end we have to understand three important
concepts
- Client
- Server
- Database
They determine how the backend will work

** Maelezo **

### Command Line on Windows, Mac and Linux
It is also known as a shell.

Why use the command Line
It's all about control. It's easier and faster to do
these common things.

Where I am in the directory
```commandline
pwd
```
list
```commandline
ls
```
displays all files and directories present in the directory

change directory and to parent directory
```commandline
cd
cd ..
```
create a new folder
```commandline
mkdir
```
create a new file
```commandline
touch file_name
```
delete the file and folder
```commandline
rm file_name

rm -rf folder_name
```
### \__name__ and \__main__ special attributes built into python
At any given point you could tap into the name to find out
what is the current class, function ,method or descriptors name.

### Python Decorators
A decorator function is a function that gives additional functionality
to an existing function.

Python decorator function
```python
def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function
```
Basically a decorator function is just a function that
wraps another function and gives that function some additional
functionality.

example
```python
import time
def say_hello():
    time.sleep(2)
    print("Hello")
```
```python
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you ?")
say_hello()
```

Generally a decorator function is a function that wraps another
function ang gives it some additional functionality or modifies the functionality.

The @sign is known a syntatic sugar
