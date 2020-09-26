# Type-Wrap

_created by Austin Poor_

[![Build Status](https://travis-ci.org/a-poor/typewrap.svg?branch=master)](https://travis-ci.org/a-poor/typewrap)
[![PyPI](https://img.shields.io/pypi/v/typewrap)](https://pypi.org/project/typewrap/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/typewrap)](https://pypi.org/project/typewrap/)
[![codecov](https://codecov.io/gh/a-poor/typewrap/branch/master/graph/badge.svg)](https://codecov.io/gh/a-poor/typewrap)



Super tiny python package for function typechecking.


## Installation

Install with pip

```bash
$ pip install typewrap
```

## Usage

### `typewrap.typeCheck`

A decorator function that checks the function input and outputs against the function annotations.

Example:

```python
from typewrap import typeCheck

def add_noChecks(a: int, b: int) -> int:
    """Has annotations but doesn't
    check argument types."""
    return a + b

@typeCheck
def add_checkInputs(a: int, b: int) -> int:
    return a + b

@typeCheck
def add_checkOutputs(a: int, b: int) -> int:
    return float(a+b)

# Unwrapped function with 
# uninforced type annotations
add_noChecks(1,2.0) # No errors


# Wrapped function with bad
# input arguments
add_checkInputs(1,2.0) # Raises TypeError


# Wrapped function with
# bad output type
add_checkOutputs(1,2) # Raises TypeError
```

### `typewrap.checkInputs`

A decorator function that checks the function inputs against the function annotations.

Example:

```python
from typewrap import checkInputs

def add_noChecks(a: int, b: int) -> int:
    """Has annotations but doesn't
    check argument types."""
    return a + b

@checkInputs
def add_inputs(a: int, b: int) -> int:
    return a + b

@checkInputs
def add_outputs(a: int, b: int) -> int:
    return float(a+b)

# Unwrapped function with 
# uninforced type annotations
add_noChecks(1,2.0) # No errors


# Wrapped function with bad
# input arguments
add_inputs(1,2.0) # Raises TypeError


# Wrapped function with
# bad output type
add_outputs(1,2) # No errors
```







