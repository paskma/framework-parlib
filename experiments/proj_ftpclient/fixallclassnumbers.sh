#!/bin/bash

# TODO: instead of this fixing, use hash instead of the number suffixes

for i in $(find jclient/pyftpclient_layer -name 'C*.java'); do
	echo "FIXING: $i"
	util/fixclassnumbers.py $i unpacked/pypy/
done
