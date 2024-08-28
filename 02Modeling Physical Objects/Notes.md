# Modeling Physical Objects with object-oriented programming.

## Building Software Models of Physical Objects
To model a real-world object in code, we need to decide what data will represent the object's attributes and what operations it can perform. These two concepts are often referred to as an object's *state* and *behavior*, respectively: the state is the data the object remembers, and the behaviors are the actions that the object can do.

## Introduction to Classes and Objects
A class is a template or a blueprint that defines what an object will look like when one is created. We create objects from a class.
Code that defines what an object will rememeber (its data or state) and the things that it will be able to do (its functions or *behavior*).

**Instantiation**: The process of creating an object from a class.

### Writing a class in Python

```python
class <ClassName>():
  def __init__(self, <optional param1>, ..., <optional paramN>):
    # any initialization code here

  # Any number of functions that access the data

  def <functionName1>(self, <optional param1>, ..., <optional paramN>):
    # body of function
```


**Method:** A function defined inside a class. A method always has at least one parameter, which is usually named `self`.

> The first method in every class should have the special name `__init__`. Whenever you create an object from a class, this method will run automatically. 


### Scope and Instance Variables
Object-oriented programming and classes introduce a level of scope, typically called *object scope* (or *class scope*): the scope consists of all the code inside the class definition.

Methods can have both local variables and *instance variables*. In a method, any variable whose name does not start with `self.` is a local variable. *Instance varabiles* have object scope, which means they are available to all methods defined in a class.

**Instance variable:** In a method, any variable whose name begins with the prefix `self`. 

Each object created from a class gets its own set of instance variables, idependent of any other objects instantiated from that class.

### Differences Between Functions and Methods
There are three differences between a function and a method:
1. All methods of a class must be indented under the `class` statement.
2. All methods have a special first parameter that is named `self`.
3. Methods in a class can use instance variables, written in the form `self.<variable_name>`.

### Creating an Object from a Class.
To use a class, you have to tell Python to make an object from the class. The typical way to do this is to use an assignment statement like:
`<object> = <ClassName>(<optional arguments>)`

### Calling Methods of an Object
After creating an object from a class, to call a method of the object, you use the genenric syntax:

`<object>. <method_name>(<any arguments>)`

### Creating Multiple Instances from the Same Class
You can instantiate as many objects as you want from a single class. 


## OOP as a solution
Summary of how object-oriented programming solves three problems that are inherent in procedural coding:
1. A well-written class can be easily reused in many different programs. 
2. Object-oriented programming can reatly reduce the number of global variables required, because a class provide a way that code and data exists in one group.
3. Objects created from a class only have access to their own data.

## Summary
* The class defines the shape and capabilities of an object.
*  An object is a single instance of a class that has its own set of all the data defined in the instance variables of the class.
* Each piece of data you want an object to contain is store as an instance variable, which is available within all methods defined in the class.
* 