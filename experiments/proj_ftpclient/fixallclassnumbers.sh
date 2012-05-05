#!/bin/bash

for i in $(find jclient/pyftpclient_layer -name 'C*.java'); do
	echo "FIXING: $i"
	util/fixclassnumbers.py $i unpacked/pypy/
done
