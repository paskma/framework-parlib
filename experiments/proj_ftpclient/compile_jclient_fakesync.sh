#!/bin/bash

echo "Copying to jclient_fakesync..."
rm -rf jclient_fakesync
cp -r jclient jclient_fakesync

echo "Fixing for fakesync..."
for i in $(find jclient_fakesync/pyftpclient_layer -name 'C*.java'); do
	echo "FIXING: $i"
	util/fixclassnumbers.py $i unpacked/pypy/
done

export CLASSPATH=jclient_fakesync:unpacked

find jclient_fakesync -name '*.class' | xargs rm

javac jclient_fakesync/paskma/main/Main.java
