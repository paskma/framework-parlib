#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
source $DIR/../environment.sh
PU="$PARLIB_FRAMEWORK_ROOT/binding/java/parlibutil"

rm -rf unpacked
mkdir unpacked
javac $PU/*.java
cp -r $PU unpacked
echo -n "Number of classes in themain-jvm.jar: "
unzip themain-jvm.jar -d unpacked | wc -l
rm -rf unpacked/com unpacked/META-INF
