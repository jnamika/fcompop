import sys
import types
import ctypes
if sys.version >= '3.0':
    import builtins
else:
    import __builtin__ as builtins


class PyObject(ctypes.Structure):
    pass


PyObject._fields_ = [('ob_refcnt', ctypes.c_int64 if hasattr(ctypes.pythonapi,
                      'Py_InitModule4_64') else ctypes.c_int),
                     ('ob_type', ctypes.POINTER(PyObject))]


class PyObjectPointer(PyObject):
    _fields_ = [('dict', ctypes.POINTER(PyObject))]


def proxy_builtin(cls):
    name = cls.__name__
    slots = getattr(cls, '__dict__', name)
    pointer = PyObjectPointer.from_address(id(slots))
    namespace = {}
    ctypes.pythonapi.PyDict_SetItem(ctypes.py_object(namespace),
                                    ctypes.py_object(name), pointer.dict)
    return namespace[name]


class Composition(object):
    def __init__(self, func):
        self.func = func

    def __rshift__(self, func):
        def _(*args, **kwds):
            return func(self.func(*args, **kwds))
        return Composition(_)

    def __lshift__(self, func):
        def _(*args, **kwds):
            return self.func(func(*args, **kwds))
        return Composition(_)

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)


proxy_builtin(types.BuiltinFunctionType)['_'] = property(Composition)
proxy_builtin(types.BuiltinMethodType)['_'] = property(Composition)
proxy_builtin(types.FunctionType)['_'] = property(Composition)
proxy_builtin(types.MethodType)['_'] = property(Composition)
proxy_builtin(type)['_'] = property(Composition)
proxy_builtin(type(type.__subclasses__))['_'] = property(Composition)
