import sys
import os
sys.path.append('fcompop')
sys.path.append(os.path.join('fcompop', 'tests'))
from setuptools import setup
from fcompop import __version__, __license__, __author__, __email__, __doc__

setup(
    name         = 'fcompop',
    version      = __version__,
    description  = 'Function composition operators for functional programming',
    long_description = __doc__,
    author       = __author__,
    author_email = __email__,
    license      = __license__,
    url          = 'https://github.com/jnamika/fcompop',
    keywords     = 'function composition operator functional programming',
    packages     = ['fcompop'],
    #package_dir  = {'fcompop' : 'src'},
    test_suite   = 'test4fcompop',
    classifiers  = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: %s' % __license__,
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
