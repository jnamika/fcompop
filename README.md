*fcompop*: _Function composition operators(>>, <<) for functional programming with Python_

Copyright (c) 2014, Jun Namikawa <jnamika@gmail.com>
License: ISC License (ISCL)



**fcompop** is a Python library that provides function composition operators.

An example of usages is following:

    >>> import fcompop
    >>> fcompop.inject()  # adding operators to builtin&user functions
    >>> func = str._ >> (lambda x: x * 2 + 'abc') >> str.upper
    >>> func(123)
    '123123ABC'
    >>> func = (lambda x: '-' + x)._ << chr << (lambda x: x + 1) << ord
    >>> func('a')
    '-b'
