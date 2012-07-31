#!/bin/bash

F="test_protocol.txt"

echo "==Test protocol `date`." > $F
echo "==Pure Python:" >> $F
par_run_pure.sh >> $F
echo "==C:" >> $F
par_compile_c.sh
par_run_c.sh >> $F
echo "==Java:" >> $F
par_compile_j.sh
par_run_j.sh >> $F
echo "==Test done." >> $F
cat $F
