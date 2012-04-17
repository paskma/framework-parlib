#!/bin/bash

# parameter should be mrun_c.sh and similar

BIN="./$1"
OUT="report_$1"

echo "BIN $BIN INTO $OUT"

cat HEADER > $OUT
export MEMPIDCSV="yes"

echo "PERF"

# the last zero is important
$BIN >> $OUT

