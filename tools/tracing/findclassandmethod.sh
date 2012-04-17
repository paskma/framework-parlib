#!/bin/bash

if [ -z "$1" ] 
then
	echo "Search jasmin (.j) files in the current directory"
	echo "for the method defined in the particular RPython"
	echo "class."
	echo ""
	echo "  usage: $0 class_name method_name"
	echo "   e.g.: $0 WorkerThread run"
	echo "   e.g.: $0 pkg_a.WorkerThread run"
	exit 1
fi


FLIST=`findclass.sh $1`
LINES=0

for i in $FLIST; do
	LINES=`expr $LINES + 1`
done


if [ $LINES == 0 ]; then
	echo "Class $1 not found."
	exit 1
fi

if [ $LINES -ge 2 ]; then
	echo "Disambigous, class $1 found in $LINES files:"
	echo $FLIST
	exit 1
fi
	
echo -n "$FLIST:"
findmethod.sh $2 $FLIST
