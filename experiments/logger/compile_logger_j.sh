OPTS="--no-translation-backendopt-inline"
#OPTS=""

BIN=/home/paskma/B/opt/python24/bin/python

PYTHONPATH=../../parlib_soptjvm $BIN ../../../translate.py $OPTS  --batch -b jvm main.py
