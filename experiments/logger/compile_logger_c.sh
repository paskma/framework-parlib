#OPTS="--no-translation-backendopt-inline"
OPTS="--translation-backendopt-none"
#OPTS=""

BIN=/home/paskma/B/opt/python24/bin/python
#$GC=ref
GC=boehm

LDIR=`pwd`/../../fiber/c
PYTHONPATH=../../parlib_c $BIN ../../../translate.py --batch --cflags='-g' --ldflags="-L$LDIR" --gc=$GC $OPTS main.py
