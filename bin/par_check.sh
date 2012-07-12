#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh

WORKDIR="$(basename `pwd`)"
TARGET=$JPF_ROOT/$WORKDIR
echo "Using directory directory $TARGET"
mkdir -p $TARGET
cp -r unpacked/* $TARGET

cd $JPF_ROOT
java RunJPF +vm.classpath=$WORKDIR pypy.Main

