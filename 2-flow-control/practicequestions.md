# Practice Questions

1. What are the two values of the Boolean data type? How do you write them?

  True

  False

2. What are the three Boolean operators?

  and, or, not

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

  | Expression          | Evaluates to...   |
  | ------------------ |:-----------------:|
  | True and True      | True              |
  | True and False     | False             |
  | False and False    | False             |

  | Expression          | Evaluates to...   |
  | ------------------ |:-----------------:|
  | True or True      | True              |
  | True or False     | True             |
  | False or False    | False             |

  | Expression          | Evaluates to...   |
  | ------------------ |:-----------------:|
  | not True      | False              |
  | not False     | True             |

4. What do the following expressions evaluate to?

  `(5 > 4) and (3 == 5)` 
  False

  `not (5 > 4)`
  False

  `(5 > 4) or (3 == 5)`
  True

  `not ((5 > 4) or (3 == 5))`
  False

  `(True and True) and (True == False)`
  False

  `(not False) or (not True)`
  True

5. What are the six comparison operators?
  - `==`
  - `!=`
  - `>`
  - `<`
  - `>=`
  - `<=`

6. What is the difference between the equal to operator and the assignment operator?
  The equal to operator (`==`) compares the values on each side.  The assignment
  operator (`=`) takes the value on the right side and assigns it to the
  variable name on the left

7. Explain what a condition is and where you would use one.

  A condition is basically a Boolean expression, except it's used in the context
  of flow control statements.

8. Identify the three blocks in this code:

  ```python
  spam = 0
  if spam == 10:
      print('eggs') #block
      if spam > 5:
          print('bacon') #block
      else:
          print('ham') #block
      print('spam')
  print('spam')
  ```

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
  ```python
  spam = 'ham'
  if spam == 1:
      print('Hello')
  elif spam == 2:
      print('Howdy')
  else:
      print('Greetings!')
  ```

10. What keys can you press if your program is stuck in an infinite loop?

  Ctrl+c (or Ctrl+d)

11. What is the difference between break and continue?
  `break` breaks out of the loop whereas `continue` jumps back to the start of the
  loop

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

  `range(10)` will start at 0 and increment by 1, up to but not including 10

  `range(0, 10)` will start at 0 and increment by 1, up to but not including 10
  (more explicit)

  `range(0, 10, 1)` will start at 0 and increment by 1, up to but not including
  10 (even more explicit)

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

```python
for i in range(10):
  print(i)
```

```python
i = 0
while i < 10:
  print(i)
  i = i + 1
```

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```python
import spam
spam.bacon()
```
