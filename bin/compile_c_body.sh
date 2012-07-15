LDIR="$PARLIB_FRAMEWORK_ROOT/binding/c"
PFR=$PARLIB_FRAMEWORK_ROOT
TRANSLATE="$PYPY_ROOT/pypy/translator/goal/translate.py"
PYTHONPATH="$PFR/parlib_c:$PFR/parlib_portable" $PYTHON_BIN $TRANSLATE --batch --cflags="$OPTS_CFLAGS" --ldflags="-L$LDIR" --gc="$OPTS_GC" $OPTS_TRANSLATE themain.py

echo Done.
