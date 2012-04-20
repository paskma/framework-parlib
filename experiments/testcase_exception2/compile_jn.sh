OPTS="--no-translation-backendopt-inline"
#OPTS=""

BIN=/home/paskma/B/opt/python24/bin/python

PYTHONPATH=../../parlib_noptjvm:../../parlib_portable $BIN ../../../translate.py $OPTS  --batch -b jvm themain.py
