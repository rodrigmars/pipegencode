# Pipegencode

Using the syntactic construction for nested functions **function_c( function_b( function_a() ) )**, it becomes complex to read a large number of functions. This python sketch uses the same concept as the pipe shell, where we use the output of functions as arguments to be used in other functions, following the flow from left to right.

As an alternative to the problem here, we explore a generator that provides functions from a list. When executing a function, its response serves as an argument to the next function in the loop. The graphic illustrates this left-to-right execution process as opposed to the block below, which uses a right-to-left execution.

![alt text](https://github.com/rodrigmars/pipegencode/blob/1df78f22a456d9bbc47a0160bfda54a4439f8200/images/modelo.png?raw=true)
