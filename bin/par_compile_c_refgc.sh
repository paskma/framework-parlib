#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh

OPTS_TRANSLATE="--translation-backendopt-none"
OPTS_GC="ref"
OPTS_CFLAGS="-g"

source $DIR/compile_c_body.sh
