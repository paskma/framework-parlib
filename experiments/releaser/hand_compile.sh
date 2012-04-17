
# To be used in /tmp directory. Useful for hand patching of generated c files.

IPASYS=/home/paskma/projects/pypygit/pypy/translator/goal/pygraph_r/fiber/c
ITRANSC=/home/paskma/projects/pypygit/pypy/translator/c
IPYTHONC=/home/paskma/B/opt/python24/include/python2.4

cd testing_1

echo ENTER TST
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c testing_1.c -o testing_1.o
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c structimpl.c -o structimpl.o
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c nonfuncnodes.c -o nonfuncnodes.o
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c implement.c -o implement.o

cd ..
cd module_cache

echo ENTER MODC
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c module_0.c -o module_0.o
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c module_1.c -o module_1.o
cc -O0 -fomit-frame-pointer -pthread -g -I../$IPASYS -I$ITRANSC -I$IPYTHONC -c module_2.c -o module_2.o

cd ..

echo LINK
cc -pthread -L$IPASYS testing_1/testing_1.o testing_1/structimpl.o testing_1/nonfuncnodes.o testing_1/implement.o module_cache/module_0.o module_cache/module_1.o module_cache/module_2.o -lpasys -lpthread -o handc
