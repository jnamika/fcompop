import sys
import types
import ctypes
import functools
if sys.version >= '3.0':
    import builtins
else:
    import __builtin__ as builtins


class _PyObject(ctypes.Structure):
    pass


_PyObject._fields_ = [('ob_refcnt', ctypes.c_int64 if hasattr(ctypes.pythonapi,
                      'Py_InitModule4_64') else ctypes.c_int),
                     ('ob_type', ctypes.POINTER(_PyObject))]


class _PyObjectPointer(_PyObject):
    _fields_ = [('dict', ctypes.POINTER(_PyObject))]


def proxy_builtin(cls):
    name = cls.__name__
    slots = getattr(cls, '__dict__', name)
    pointer = _PyObjectPointer.from_address(id(slots))
    namespace = {}
    ctypes.pythonapi.PyDict_SetItem(ctypes.py_object(namespace),
                                    ctypes.py_object(name), pointer.dict)
    return namespace[name]


class Composition(functools.partial):
    def __rshift__(self, func):
        def _(*args, **kwds):
            return func(self(*args, **kwds))
        return Composition(_)

    def __lshift__(self, func):
        def _(*args, **kwds):
            return self(func(*args, **kwds))
        return Composition(_)


def inject(*args):
    proxy_builtin(types.BuiltinFunctionType)['_'] = property(Composition)
    proxy_builtin(types.BuiltinMethodType)['_'] = property(Composition)
    proxy_builtin(types.FunctionType)['_'] = property(Composition)
    proxy_builtin(types.MethodType)['_'] = property(Composition)
    proxy_builtin(type)['_'] = property(Composition)
    proxy_builtin(type(type.__subclasses__))['_'] = property(Composition)
    proxy_builtin(functools.partial)['_'] = property(Composition)
    for arg in args:
        proxy_builtin(arg)['_'] = property(Composition)
