'''
fcompop is a Python library that provides function composition operators.

An example of usages is following:

    >>> import fcompop
    >>> func = str._ >> (lambda x: x * 2 + 'abc') >> str.upper
    >>> func(123)
    '123123ABC'
    >>> func = (lambda x: '-' + x)._ << chr << (lambda x: x + 1) << ord
    >>> func('a')
    '-b'
'''

__author__ = 'Jun Namikawa'
__email__ = 'jnamika@gmail.com'
__version__ = '0.1'
__license__ = 'ISC License (ISCL)'
