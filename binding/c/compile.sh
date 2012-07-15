#!/bin/sh

gcc -c pasys.c -o pasys.o
gcc -c simplenet.c -o simplenet.o
gcc -c simplecon.c -o simplecon.o
echo static lib
ar rcs libpasys.a pasys.o simplenet.o simplecon.o
rm pasys.o
echo static prg
rm -f libpasys.so.1.0.1
gcc -static client.c -L. -lpasys -lm -o client_static -lpthread
echo dynamic lib
gcc -c -fPIC pasys.c -o pasys.o
gcc -c -fPIC simplenet.c -o simplenet.o
gcc -c -fPIC simplecon.c -o simplecon.o
gcc -shared -lm -Wl,-soname,libpasys.so.1 -o libpasys.so.1.0.1  pasys.o simplenet.o simplecon.o
echo dyn prg
rm libpasys.a
gcc client.c  -L. -lpasys -o client_dyn -lpthread

