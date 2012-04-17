#!/bin/bash

if [ -z "$1" ] 
then
	echo "Search jasmin (.j) files in the current directory"
	echo "for classes defined in RPython source code."
	echo ""
	echo "  usage: $0 class_name"
	echo "   e.g.: $0 WorkerThread"
	echo "   e.g.: $0 pkg_name.WorkerThread"
	exit 1
fi

ack-grep --type-add jasmin=.j  "class.*$1" -l 2>/dev/null
