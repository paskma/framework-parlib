OPTS="--translation-backendopt-none"
#OPTS=""

BIN=/home/paskma/B/opt/python24/bin/python

# GC=boehm|ref|marksweep|semispace|statistics|generation|hybrid|none, suggested:hybrid]

#$GC=ref
GC=marksweep

LDIR=`pwd`/../../fiber/c
PYTHONPATH=../../parlib_c:../../parlib_portable $BIN ../../../translate.py --batch --cflags='-g' --ldflags="-L$LDIR" --gc=$GC $OPTS themain.py