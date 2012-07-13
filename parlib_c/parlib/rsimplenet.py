from pypy.rpython.lltypesystem import rffi
from pypy.translator.tool.cbuild import ExternalCompilationInfo
from pypy.rpython.lltypesystem import lltype

from os.path import join, dirname


_compilation_info_ = ExternalCompilationInfo(
	includes = ['simplenet.h'],
	include_dirs = [join(dirname(__file__), '../../binding/c')],
	libraries = ['pasys'],
)
def external(name, args, result, **kwds):
    return rffi.llexternal(name, args, result, compilation_info=_compilation_info_, threadsafe=True, sandboxsafe=True)

ll_simplenet_connect = external('simplenet_connect', [rffi.CCHARP, rffi.INT], rffi.INT)
ll_simplenet_read = external('simplenet_read', [rffi.INT], rffi.INT)
ll_simplenet_close = external('simplenet_close', [rffi.INT], rffi.INT)
ll_simplenet_write_buf = external('simplenet_write_buf', [rffi.INT, rffi.CCHARP, rffi.INT], rffi.INT)
ll_simplenet_write_char = external('simplenet_write_char', [rffi.INT, rffi.INT], rffi.INT)
ll_simplenet_flush = external('simplenet_flush', [rffi.INT], rffi.INT)
ll_simplenet_set_timeout = external('simplenet_set_timeout', [rffi.INT, rffi.INT], rffi.INT)

