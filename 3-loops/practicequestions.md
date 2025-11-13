1.  What keys can you press if your Python program is stuck in an infinite loop?
CTRL + C

2.  What is the difference between break and continue?
- break will move execuion outside and just after a loop
- continue will move the execution to the start of the loop

3.  What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
- range(10) will start at 0 and iterate up to 10
- range(0, 10) is a more explicit verison of range(10), specifying to start at 0
- range(0, 10, 1) is an even more explicit version of range(0, 10) specifying to increment by 1 in each iteration
All three do basically the same thing.

4.  Write a short program that prints the numbers 1 to 10 using a for loop. Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.
```python
for i in range(1, 11):
  print(str(i))
```

```python
i = 1
while i < 11:
  print(str(i))
  i = i + 1
```

5.  If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```python
spam.bacon()
```