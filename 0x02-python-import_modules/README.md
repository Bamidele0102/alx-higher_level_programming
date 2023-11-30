Python - import & modules - Task Questions
============================================================
# 0. Import a simple function from a simple file
**Mandatory**

Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

- You have to use print function with string format to display integers
- You have to assign:
the value 1 to a variable called a
the value 2 to a variable called b
- and use those two variables as arguments when calling the functions add and print
a and b must be defined in 2 different lines: a = 1 and another b = 2
- Your program should print: < a value> + < b value >  = < add(a, b) value > followed with a new line
- You can only use the word add_0 once in your code
- You are not allowed to use * for importing or __ import__
- Your code should not be executed when imported - by using __ import__, like the example below.

![Alt text](image.png)
===========================================================
# 1. My first toolbox!
**Mandatory**

Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

- Do not use the function print (with string format to display integers) more than 4 times
- You have to define:
the value 10 to a variable a
the value 5 to a variable b
and use those two variables only, as arguments when calling functions (including print)
a and b must be defined in 2 different lines: a = 10 and another b = 5
- Your program should call each of the imported functions. See example below for format
the word calculator_1 should be used only once in your file
- You are not allowed to use * for importing or __import __
- Your code should not be executed when imported.
===========================================================
# 2. How to make a script dynamic!
**Mandatory**

Write a program that prints the number of and the list of its arguments.

## The output should be:
- Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
- one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of argv can be retrieved by using: len(argv)
- You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
===========================================================
# 3. Infinite addition
**Mandatory**

Write a program that prints the result of the addition of all arguments

- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported
_Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:_
![Alt text](image-1.png)
_Remember how you did (or did not) do it in C? #pythoniscool_
![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231130%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231130T203650Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d679db9048b04a50cfbc9f5990ef137f7fbc96cbc43a901cc7472f564949e4f9)
===========================================================
# 4. Who are you?
**Mandatory**

Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

- You should print one name per line, in alpha order
- You should print only names that do not start with __
- Your code should not be executed when imported
- Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)
===========================================================
# 5. Everything can be imported
**Mandatory**

Write a program that imports the variable a from the file variable_load_5.py and prints its value.

- You are not allowed to use * for importing or __import __
- Your code should not be executed when imported
===========================================================
# 6. Build my own calculator!
**Advanced**

Write a program that imports all functions from the file calculator_1.py and handles basic operations.

_Usage: ./100-my_calculator.py a operator b_
- If the number of arguments is not 3, your program has to:
print Usage: ./100-my_calculator.py < a> < operator> < b> followed with a new line
exit with the value 1
## operator can be:
+ for addition
- for subtraction
* for multiplication
/ for division
- If the operator is not one of the above:
print Unknown operator. Available operators: +, -, * and / followed with a new line
exit with the value 1
- You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
- The result should be printed like this: < a> < operator> < b> = < result>, followed by a new line
- You are not allowed to use * for importing or __ import__
- Your code should not be executed when imported
===========================================================
# 7. Easy print
**Advanced**

Write a program that prints #pythoniscool, followed by a new line, in the standard output.

- Your program should be maximum 2 lines long
You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py
===========================================================
# 8. ByteCode -> Python #3
**Advanced**

Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
===========================================================
# 9. Fast alphabet
**Advanced**

Write a program that prints the alphabet in uppercase, followed by a new line.

- Your program should be maximum 3 lines long
## You are not allowed to use:
- any loops
- any conditional statements
- str.join()
- any string literal
- any system calls