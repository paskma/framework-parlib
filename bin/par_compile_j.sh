#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh
TRANSLATE="$PYPY_ROOT/pypy/translator/goal/translate.py"

OPTS="--no-translation-backendopt-inline"

PFR=$PARLIB_FRAMEWORK_ROOT
#not simplified
PYTHONPATH="$PFR/parlib_noptjvm:$PFR/parlib_portable" $PYTHON_BIN $TRANSLATE --batch $OPTS -b jvm themain.py

echo "Preparing binding..."
$DIR/par_prepare_binding_j.sh

echo Done.
