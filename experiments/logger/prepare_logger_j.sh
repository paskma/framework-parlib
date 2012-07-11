#!/bin/bash

rm -rf unpacked
mkdir unpacked
rm -rf parlibutil
cp -r ../../java_binding/parlibutil .
javac parlibutil/*.java
mv parlibutil unpacked
unzip main-jvm.jar -d unpacked | wc -l
rm -rf unpacked/com unpacked/META-INF

export CLASSPATH="unpacked"
#java pypy.Main
