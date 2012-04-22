#!/bin/bash

# parameter should be mrun_c.sh and similar

COUNT[0]=100;      LOOP[0]=10000000
COUNT[1]=1000;     LOOP[1]=1000000
COUNT[2]=10000;    LOOP[2]=100000
COUNT[3]=100000;   LOOP[3]=10000


BIN="./$1"
OUT="report_$1"

echo "BIN $BIN INTO $OUT"

cat HEADER > $OUT
export MEMPIDCSV="yes"

L=`expr ${#COUNT[*]} - 1`
for i in `seq 0 $L`;
do
	echo "PERF" ${COUNT[$i]} ${LOOP[$i]}
	
	echo -n "${COUNT[$i]};${LOOP[$i]};" >> $OUT
	# the last zero is important
	$BIN ${COUNT[$i]} ${LOOP[$i]} 0 >> $OUT
done
