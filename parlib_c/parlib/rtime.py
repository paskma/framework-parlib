from time import sleep as _sleep


from pypy.rpython.lltypesystem import rffi
from pypy.translator.tool.cbuild import ExternalCompilationInfo
from pypy.rpython.lltypesystem import lltype

from os.path import join, dirname


_compilation_info_ = ExternalCompilationInfo(
	includes = ['pasys.h'],
	include_dirs = [join(dirname(__file__), '../../binding/c')],
	libraries = ['pasys'],
)
def external(name, args, result, **kwds):
    return rffi.llexternal(name, args, result, compilation_info=_compilation_info_, threadsafe=True, sandboxsafe=True)
ll_sig_ignore = external('sig_ignore', [rffi.INT], lltype.Void)
ll_pasys_sleep = external('pasys_sleep', [rffi.DOUBLE], rffi.INT)

def sleep(n):
	#ll_sig_ignore(30) #caused deadloc, solved by looped sleeping in pasys
	#return _sleep(n)
	return ll_pasys_sleep(n)
