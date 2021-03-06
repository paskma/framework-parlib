#!/bin/bash

PU="$PARLIB_FRAMEWORK_ROOT/binding/java/parlibutil"


rm -rf unpacked
mkdir unpacked
javac $PU/*.java
cp -r $PU unpacked
unzip themain-jvm.jar -d unpacked | wc -l
rm -rf unpacked/com unpacked/META-INF

export CLASSPATH="unpacked"
java pypy.Main &

. ./memsnip.sh
