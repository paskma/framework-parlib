LDIR="$PARLIB_FRAMEWORK_ROOT/fiber/c"
PFR=$PARLIB_FRAMEWORK_ROOT
PYTHONPATH="$PFR/parlib_c:$PFR/parlib_portable" $PYTHON_BIN $TRANSLATE --batch --cflags="$OPTS_CFLAGS" --ldflags="-L$LDIR" --gc="$OPTS_GC" $OPTS_TRANSLATE themain.py

echo Done.
