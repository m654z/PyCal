4. Builtins
***********

Let's go over some of PyCal's builtins. Builtins are a big part of PyCal, so it's a good idea to learn what all of them do.

4.1 ``S`` - Square root
=======================

The ``S`` gets the square root whatever is in the variable, and stores the it in the result variable.

Example usage:

``(7)S!`` outputs the square root of 7.

4.2 ``C`` - Ceiling
===================

The ``C`` command rounds the variable towards the ceiling.

Example usage:

``(4.3)C!`` outputs 5.

4.3 ``f`` - Floor
=================

The ``f`` command rounds the variable towards the floor.

Example usage:

``(7.6)f!`` outputs 7.

4.4 ``x`` - Factorial
=====================

The ``x`` command calculates the factorial of the variable.

Example usage:

``(4)x!`` outputs the factorial of 4.

4.5 ``E`` - Exponent
====================

The ``E`` command calculates the exponent of the variable.

Example usage:

``(11)E!`` outputs the exponent of 11.

4.6 ``T`` - Time
================

The ``T`` command gets the current time.

Example usage:

``T!`` outputs the current time.

4.7 ``D`` - Date
================

The ``D`` command gets the current date.

Example usage:

``D!`` outputs the current date.

4.8 ``P`` - Primes
==================

The ``P`` command calculates the first *n* prime numbers.

Example usage:

``(20)P!`` outputs the first 20 prime numbers as a list.

4.9 ``s`` - Statistics mode
===========================

The ``s`` command starts statistics mode, which has a handful of useful commands for calculating the mode, median and mean of a list.
You can use ``.`` to exit out of statistics mode.

4.9.1 ``M`` - Mean
------------------

The ``M`` command calculates the mean (average) of a list.

Example usage:

``(1,2,3,3,4,4,4,5)sM.!`` outputs the average of the list (3.25)

4.9.2 ``m`` - Median
--------------------

The ``m`` command gets the median (middle item) of a list.

Example usage:

``(1,2,3,3,4,4,4,5,5)sm.!`` outputs the median of the list (4)

4.9.3 ``O`` - Mode
------------------

The ``O`` command gets the mode (item that appears the most) of a list.

Example usage:

``(1,2,3,3,4,4,4,5)sO.!`` outputs the mode of the list (4)