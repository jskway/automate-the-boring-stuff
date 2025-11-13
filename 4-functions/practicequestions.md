# Practice Questions

1. Why are functions advantageous to have in your programs?

  Functions are the primary way to compartmentalize your code into logical
  groups (that can get executed multiple times).

2. When does the code in a function execute: when the function is defined or when the function is called?

  When the function is called.

3. What statement creates a function?

  `def`

4. What is the difference between a function and a function call?

  You define a function using the `def` statement.  A function is not executed
  until it is called, not when the function is first defined.

5. How many global scopes are there in a Python program? How many local scopes?

  One global scope.  One local scope per function that is called.

6. What happens to variables in a local scope when the function call returns?

  The local scope is destroyed and the variables are forgotten.

7. What is a return value? Can a return value be part of an expression?

   A return value is the value that a function call evaluates to.  When an
   expression is used with a return statement, the return value is what this
   expession evaluates to.


8. If a function does not have a return statement, what is the return value of a call to that function?

  `None`

9. How can you force a variable in a function to refer to the global variable?

  By using the `global` keyword before the variable name

10. What is the data type of None?

  NoneType

11. What does the import areallyourpetsnamederic statement do?

  It tries to import a module called `areallyourpetsnamederic` and returns a
  ModuleNotFoundError: "No module named 'areallyourpetsnamederic'"

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

  `spam.bacon()`

13. How can you prevent a program from crashing when it gets an error?

  Use the `try` and `except` statements.

14. What goes in the try clause? What goes in the except clause?

  The code that could potentially cause an error goes in the `try` clause.  The
  error message to print goes in the `except` clause.
