1.  Why are functions advantageous to have in your programs?

Functions help you compartmentalize your code into logical groups and reduce duplication of code.

2.  When does the code in a function execute: when the function is defined or when the function is called?

When the function is called.

3.  What statement creates a function?

`def`

4.  What is the difference between a function and a function call?

A function consists of the def statement and body.  A function call is what moves the program execution into the function, and the function call evaluates to the function's return value.

5.  How many global scopes are there in a Python program? How many local scopes are there?

There is one global scope in a Python program. A local scope is created whenever a function is called. 

6.  What happens to variables in a local scope when the function call returns?

They are removed, along with the local scope.

7.  What is a return value? Can a return value be part of an expression?

A return value is the value that a function evaluates to.  A return value can be used in an expression.

8.  If a function does not have a return statement, what is the return value of a call to that function?

`None`

9.  How can you force a variable in a function to refer to the global variable?

You can use the `global` keyword

10.  What is the data type of None?

NoneType

11.  What does the import areallyourpetsnamederic statement do?

It imports the module `areallyourpetsnamederic` so you can use its methods in your program.

12.  If you had a function named bacon() in a module named spam, how would you call it after importing spam?

`spam.bacon()`

13.  How can you prevent a program from crashing when it gets an error?

You can put the code that might cause an error in a try clause

14.  What goes in the try clause? What goes in the except clause?

Code that could potentially cause errors goes in the try clause.
The code that executes if an error happens goes in the except clause.

15.  Write the following program in a file named notrandomdice.py and run it. Why does each function call return the same number?

import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

Each function call returns the same number because random_number is a global variable assigned a value once, and each function call just uses the global variable.
