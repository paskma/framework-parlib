#
# Snippet that is included by mrun_*
# Handles signals, calls mempid.py
#

if test -z "$MEMPIDPY"
then
   MEM=../../tools/mem/mempid.py
else
   MEM="$MEMPIDPY"
fi


PID=$!

function clean_up {
	echo "TRAP"
	kill $PID
	exit
}

trap clean_up SIGINT SIGTERM


#echo pid $PID

for i in `seq 1 1`;
do
  $MEM $PID 20
  #sleep 1
done

echo "Killing $PID" 1>&2
kill $PID
