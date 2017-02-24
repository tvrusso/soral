# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_soral', [dirname(__file__)])
        except ImportError:
            import _soral
            return _soral
        if fp is not None:
            try:
                _mod = imp.load_module('_soral', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _soral = swig_import_helper()
    del swig_import_helper
else:
    import _soral
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _soral.new_doubleArray(nelements)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _soral.delete_doubleArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _soral.doubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _soral.doubleArray___setitem__(self, index, value)

    def cast(self):
        return _soral.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _soral.doubleArray_frompointer
    if _newclass:
        frompointer = staticmethod(_soral.doubleArray_frompointer)
doubleArray_swigregister = _soral.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(t):
    return _soral.doubleArray_frompointer(t)
doubleArray_frompointer = _soral.doubleArray_frompointer


def toValArray(size, inArray):
    return _soral.toValArray(size, inArray)
toValArray = _soral.toValArray
class AreaIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AreaIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AreaIterator, name)
    __repr__ = _swig_repr

    def __init__(self, p_allocation, p_resource_num):
        this = _soral.new_AreaIterator(p_allocation, p_resource_num)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _soral.delete_AreaIterator
    __del__ = lambda self: None

    def increment(self):
        return _soral.AreaIterator_increment(self)

    def __ref__(self):
        return _soral.AreaIterator___ref__(self)

    def atEnd(self):
        return _soral.AreaIterator_atEnd(self)

    def getResource(self):
        return _soral.AreaIterator_getResource(self)
AreaIterator_swigregister = _soral.AreaIterator_swigregister
AreaIterator_swigregister(AreaIterator)

class ResourceIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ResourceIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ResourceIterator, name)
    __repr__ = _swig_repr

    def __init__(self, p_allocation, p_area_num):
        this = _soral.new_ResourceIterator(p_allocation, p_area_num)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _soral.delete_ResourceIterator
    __del__ = lambda self: None

    def increment(self):
        return _soral.ResourceIterator_increment(self)

    def __ref__(self):
        return _soral.ResourceIterator___ref__(self)

    def atEnd(self):
        return _soral.ResourceIterator_atEnd(self)

    def getArea(self):
        return _soral.ResourceIterator_getArea(self)
ResourceIterator_swigregister = _soral.ResourceIterator_swigregister
ResourceIterator_swigregister(ResourceIterator)

class ActiveAreasIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ActiveAreasIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ActiveAreasIterator, name)
    __repr__ = _swig_repr

    def __init__(self, p_allocation):
        this = _soral.new_ActiveAreasIterator(p_allocation)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _soral.delete_ActiveAreasIterator
    __del__ = lambda self: None

    def getCurrentActiveAreaNum(self):
        return _soral.ActiveAreasIterator_getCurrentActiveAreaNum(self)

    def __ref__(self):
        return _soral.ActiveAreasIterator___ref__(self)

    def increment(self):
        return _soral.ActiveAreasIterator_increment(self)

    def atEnd(self):
        return _soral.ActiveAreasIterator_atEnd(self)
ActiveAreasIterator_swigregister = _soral.ActiveAreasIterator_swigregister
ActiveAreasIterator_swigregister(ActiveAreasIterator)

class Allocation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Allocation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Allocation, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _soral.delete_Allocation
    __del__ = lambda self: None

    def getEndurance(self, resourceNum):
        return _soral.Allocation_getEndurance(self, resourceNum)

    def getEffectiveness(self, areaNum, resourceNum):
        return _soral.Allocation_getEffectiveness(self, areaNum, resourceNum)

    def calcAllocation(self):
        return _soral.Allocation_calcAllocation(self)

    def getCoverage(self, areaNum):
        return _soral.Allocation_getCoverage(self, areaNum)

    def getPOD(self, areaNum):
        return _soral.Allocation_getPOD(self, areaNum)

    def getPOS(self, areaNum):
        return _soral.Allocation_getPOS(self, areaNum)

    def getNewPOC(self, areaNum):
        return _soral.Allocation_getNewPOC(self, areaNum)

    def getTotalPOS(self):
        return _soral.Allocation_getTotalPOS(self)
Allocation_swigregister = _soral.Allocation_swigregister
Allocation_swigregister(Allocation)

class AreaAssignment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AreaAssignment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AreaAssignment, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _soral.delete_AreaAssignment
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _soral.new_AreaAssignment(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def getAreaNum(self):
        return _soral.AreaAssignment_getAreaNum(self)

    def getTime(self):
        return _soral.AreaAssignment_getTime(self)
AreaAssignment_swigregister = _soral.AreaAssignment_swigregister
AreaAssignment_swigregister(AreaAssignment)

class ResourceAssignment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ResourceAssignment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ResourceAssignment, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _soral.delete_ResourceAssignment
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _soral.new_ResourceAssignment(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def getResourceNum(self):
        return _soral.ResourceAssignment_getResourceNum(self)

    def getTime(self):
        return _soral.ResourceAssignment_getTime(self)
ResourceAssignment_swigregister = _soral.ResourceAssignment_swigregister
ResourceAssignment_swigregister(ResourceAssignment)

class ActiveArea(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ActiveArea, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ActiveArea, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _soral.delete_ActiveArea
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _soral.new_ActiveArea(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def getActiveAreaNum(self):
        return _soral.ActiveArea_getActiveAreaNum(self)
ActiveArea_swigregister = _soral.ActiveArea_swigregister
ActiveArea_swigregister(ActiveArea)


def newCharnesCooper(p_no_resources, p_no_areas, p_effectiveness, p_available, p_POC):
    return _soral.newCharnesCooper(p_no_resources, p_no_areas, p_effectiveness, p_available, p_POC)
newCharnesCooper = _soral.newCharnesCooper
class CharnesCooper(Allocation):
    __swig_setmethods__ = {}
    for _s in [Allocation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CharnesCooper, name, value)
    __swig_getmethods__ = {}
    for _s in [Allocation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CharnesCooper, name)
    __repr__ = _swig_repr

    def __init__(self, p_no_resources, p_no_areas, p_effectiveness, p_available, p_POC):
        this = _soral.new_CharnesCooper(p_no_resources, p_no_areas, p_effectiveness, p_available, p_POC)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _soral.delete_CharnesCooper
    __del__ = lambda self: None
CharnesCooper_swigregister = _soral.CharnesCooper_swigregister
CharnesCooper_swigregister(CharnesCooper)


_soral.ROW_swigconstant(_soral)
ROW = _soral.ROW

_soral.COLUMN_swigconstant(_soral)
COLUMN = _soral.COLUMN
class Array2D(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Array2D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Array2D, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _soral.new_Array2D(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _soral.delete_Array2D
    __del__ = lambda self: None

    def printSelf(self):
        return _soral.Array2D_printSelf(self)

    def get(self, rowIndex, colIndex):
        return _soral.Array2D_get(self, rowIndex, colIndex)

    def set(self, rowIndex, colIndex, value):
        return _soral.Array2D_set(self, rowIndex, colIndex, value)

    def getNumColumns(self):
        return _soral.Array2D_getNumColumns(self)

    def getNumRows(self):
        return _soral.Array2D_getNumRows(self)
Array2D_swigregister = _soral.Array2D_swigregister
Array2D_swigregister(Array2D)

# This file is compatible with both classic and new-style classes.


