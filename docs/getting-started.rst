1. Getting started with PyCal
*****************************

PyCal is a programming language designed for code-golf challenges, especially ones that require math.
Since PyCal is a code-golf language, it has many one-character builtins, which might make the code unreadable. However, once you learn how to use PyCal, writing programs in it will be simple.

1.1 The interpreter
===================

PyCal is an interpreted language, making it much easier to use and run than compiled languages. PyCal's interpreter is written in Python, hence the name.
You can find PyCal's official interpreter over at `GitHub <http://github.com/m654z/PyCal>`_.

1.2 Basic information
=====================

Before you start using PyCal, you'll need to get a couple things straight.
PyCal has two "variables". You can set a value to the first variable, but the second one is reserved for values that some built-ins return.
From now on, I'll call the first variable the... "variable", and the other one the "result".

1.3 Hello!
==========

Even though PyCal is a math-based programming language, let's kick this tutorial off with a Hello, world! program.

``:Hello, world!;^``

Even though it looks confusing, it's quite simple.
Everything between ``:`` and ``;`` is read and stored in the variable. **NOTE: ``:`` and ``;`` are only for reading strings. I'll get into other types in a moment.**
All ``^`` does is output whatever is in the variable.

Let's get into some more advanced topics in the next section.