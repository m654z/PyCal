3. Loops
********

Loops in PyCal are useful for all sorts of different tasks.

The basic loop syntax is ``*times[code]``.
For example, ``*10[!]`` will output the result ten times.

3.1 Numbers from 0 to n
=======================

Let's make a simple program that counts up from 0 to *n*.

``*i[^+]``

``i`` in a loop makes the loop run as many times as the user specified.
``^+`` outputs the variable and adds one to it.

3.2 First n Fibonacci numbers
=============================

``*i[F!+]``

``F`` outputs the *n*th Fibonacci number (*n* is the variable's value), and ``+`` adds one to the variable.
