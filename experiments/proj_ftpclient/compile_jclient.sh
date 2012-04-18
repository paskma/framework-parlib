#!/bin/bash

export CLASSPATH=jclient:unpacked

find jclient -name '*.class' | xargs rm

javac jclient/paskma/main/Main.java
