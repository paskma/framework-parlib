#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh

LD_LIBRARY_PATH="$PARLIB_FRAMEWORK_ROOT/fiber/c" ./themain-c $@
