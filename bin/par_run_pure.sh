#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh

PFR=$PARLIB_FRAMEWORK_ROOT
PYTHONPATH="$PFR/parlib_soptpure:$PFR/parlib_portable" python themain.py $@
