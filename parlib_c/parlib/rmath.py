from time import sleep as _sleep


from pypy.rpython.lltypesystem import rffi
from pypy.translator.tool.cbuild import ExternalCompilationInfo
from pypy.rpython.lltypesystem import lltype

from os.path import join, dirname


_compilation_info_ = ExternalCompilationInfo(
	includes = ['pasys.h'],
	include_dirs = [join(dirname(__file__), '../../fiber/c')],
	libraries = ['pasys'],
)
def external(name, args, result, **kwds):
    return rffi.llexternal(name, args, result, compilation_info=_compilation_info_, threadsafe=True, sandboxsafe=True)


sin = external('pasys_sin', [rffi.DOUBLE], rffi.DOUBLE)
