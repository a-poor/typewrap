"""
typewrap/__init__.py

created by Austin Poor
"""

import functools
import inspect

from typing import Callable, Any

from .exceptions import TypeCheckError


__version__ = "0.2.3"


def checkInputs(f: Callable[[Any],Any]) -> Callable[[Any],Any]:
    """Function input type-checking decorator.

    Wraps a function with argument type annotations.
    When function is called, checks input arguments
    against annotated types.

    :param f: Function with argument type hints to check
    :raises TypeCheckError: If `not isinstance(argValue,argType)`

    Example:
    >>> @checkInputs
    >>> def add(a: int, b: int):
    ...    return a + b
    >>> add(1, 2)   # Works
    >>> add(1, 2.0) # Raises TypeCheckError
    """
    # Get the function signature
    sig = inspect.signature(f)
    @functools.wraps(f)
    def inner(*args,**kwargs):
        # Check the inputs
        bound = sig.bind(*args,**kwargs)
        for arg, val in bound.arguments.items():
            argtype = sig.parameters.get(arg).annotation
            if argtype is inspect._empty: continue
            if not isinstance(val,argtype):
                raise TypeCheckError(f"Input type mismatch: `type({val!r}) != {argtype!r}`")
        # Return the result
        return f(*args,**kwargs)
    return inner

def checkOutputs(f: Callable[[Any],Any]) -> Callable[[Any],Any]:
    """Function input type-checking decorator.

    Wraps a function with argument type annotations.
    When function is called, checks output value
    type against annotated type.

    :param f: Function with return type hint to check
    :raises TypeCheckError: If `not isinstance(returnValue,returnType)`

    Example:
    >>> @checkOutputs
    >>> def add(a, b) -> int:
    ...    return a + b
    >>> add(1, 2)   # Works
    >>> @checkOutputs
    >>> def add(a, b) -> str:
    ...    return a + b
    >>> add(1, 2)   # Raises TypeCheckError
    """
    # Get the function signature
    sig = inspect.signature(f)
    @functools.wraps(f)
    def inner(*args,**kwargs):
        # Compute the result
        result = f(*args,**kwargs)
        # Check the output
        return_type = sig.return_annotation
        if return_type is not inspect._empty:
            if not isinstance(result,return_type):
                raise TypeCheckError(f"Output type mismatch: `type({result!r}) != {return_type!r}`")
        return result
    return inner
