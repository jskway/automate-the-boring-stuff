# Chapter 5 - Practice Questions

1.  Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

```python
assert int(spam) >= 10, 'The spam variable is less than 10.'
```

2.  Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)

```python
assert eggs.lower() !== bacon.lower(), 'The eggs and bacon variables are the same!'
```

3.  Write an assert statement that always triggers an AssertionError.

```python
assert False, 'This assertion always triggers.'
```

4.  What two lines must your program have to be able to call logging.debug()?

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
```

5.  What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?

```python
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s)
```

6.  What are the five logging levels?
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

7.  What line of code can you add to disable all logging messages in your program?

```python
logging.disable(logging.CRITICAL)
```

8.  Why is using logging messages better than using print() to display the same message?

You can disable logging messages without removing the logging function calls.
You can selectively disable lower-level logging messages.
You can log to a text file and customize the format.
Logging messages provide a timestamp.


9.  What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

- Step Over executes the next line in a file, but if its a function, it will rush through the code in the function
- Step In executes the next line in a file, but if its a function, it will jump to the function's first line of code
- Step Out will cause the debugger to execute lines of code at full speed until it returns from the current function

10.  After you click Continue, when will the debugger stop?
Until it reaches the end of the program or a line with a breakpoint

11.  What is a breakpoint?
A breakpoint is a red dot set on a specific line of code that forces the debugger to pause whenever the program execution reaches that line.

12.  How do you set a breakpoint on a line of code in Mu?
By clicking on the line number in the file editor to make a red dot appear next to it

