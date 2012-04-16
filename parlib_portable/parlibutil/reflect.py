import types

def clone_function(name, f):
	"""
		Copies the bytecode from f and returns a new function
		with name 'name'.
		
		The result can be specialized to another rtype.
	"""
	f_code = types.CodeType(f.func_code.co_argcount,
		f.func_code.co_nlocals,
		f.func_code.co_stacksize,
		f.func_code.co_flags,
		f.func_code.co_code,
		f.func_code.co_consts,
		f.func_code.co_names,
		f.func_code.co_varnames,
		f.func_code.co_filename,
		name,
		f.func_code.co_firstlineno,
		f.func_code.co_lnotab)

	return types.FunctionType(f_code, f.func_globals, name)

