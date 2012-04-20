#!/bin/bash

PU=../../watersystem_opt/parlibutil

rm -rf unpacked
mkdir unpacked
javac $PU/*.java
cp -r $PU unpacked
unzip themain-jvm.jar -d unpacked | wc -l
rm -rf unpacked/com unpacked/META-INF

export CLASSPATH="unpacked"
echo "Not running java pypy.Main"
