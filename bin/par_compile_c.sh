#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh

OPTS="--translation-backendopt-none"
#OPTS=""

GC=boehm

LDIR="$PARLIB_FRAMEWORK_ROOT/fiber/c"
PFR=$PARLIB_FRAMEWORK_ROOT
PYTHONPATH="$PFR/parlib_c:$PFR/parlib_portable" $PYTHON_BIN $TRANSLATE --batch --cflags='-g' --ldflags="-L$LDIR" --gc=$GC $OPTS themain.py

echo Done.
