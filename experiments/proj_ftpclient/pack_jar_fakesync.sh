#!/bin/bash

rm -rf unpacked_jar
mkdir unpacked_jar
cp -r unpacked/* unpacked_jar
cp -r jclient_fakesync/* unpacked_jar
cd unpacked_jar
find . -name '*.java' | xargs rm
cd ..
jar -cfe pyftpclient.jar paskma.main.Main -C unpacked_jar .
rm -rf unpacked_jar
