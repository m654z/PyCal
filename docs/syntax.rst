2. Basic PyCal Syntax
*********************

Let's go over the syntax of PyCal programs.

2.1 Simple calculations
=======================

Let's try calculating 2+2 and outputting the result.

``{2+2}!``

It's as simple as that. Everything in the curly brackets are evaluated and the result is stored in the... result (as you might remember, the result is the second variable)
The ``!`` command outputs whatever is in the result.

Let's try a more complicated equasion.

``{(72*21)/3+4.5-2.22}!``

The above program should output 506.28. As you can see, PyCal supports floating point numbers as well as integers.

Now, let's try something a little different.

``{i+i}!``

Can you guess what this does? It takes two inputs (``i``), and adds them together.
Then, it outputs the result.

If you wanted to, you could even do this:

``(5){v+2}!``

This translates to the following:

``{5+2}!``

``v`` expands to the value that is in the variable. In the above program, it's 5.

2.2 The variable
================

The variable is a key element in nearly all PyCal programs, since most builtins take it as an argument.
To set the variable, you can do the following:

``(42)``

The above program sets the variable's value to 42. Pretty easy.

Now, let's do something with the variable. Let's get the *n*th Fibonacci number.

``IF!``

As you might have guessed, ``F`` is the Fibonacci builtin.
``I`` simply gets input as an integer and stores it in the variable.
``F`` takes the variable's value, and calculates the *n*th Fibonacci number with it. It's then stored in the result.

2.3 Comparison
==============

Sometimes you'll need to compare the variable and the result. PyCal has commands just for that.

First of all, you'll want to know that PyCal doesn't have booleans. The number 1 is used to represent True, and 0 to represent False.
So, let's get right in to it.

2.3.1 Is less than
------------------

``(30)IF<!``

The above program sets the variable to the value 30.
After that, it calculates the *n*th Fibonacci number and stores it in the result.
Then, it checks if the variable's value is less than the result using the ``<`` command.
If it **is** less, change the result to 1. If it isn't, the result is 0. Then it outputs the result.

2.3.2 Is greater than
---------------------

``(30)IF>!``

This is the same as the program in 2.3.1, except is uses the ``>`` command to check if the result is greater than the variable.

2.3.3 Is equal to
-----------------

``(21)IF=!``

This is the same as 2.3.1 and 2.3.2, except that it checks if the variable is equal to the result.
In the above program, the result 1 if the input is 6, since the sixth Fibonacci number is 21.