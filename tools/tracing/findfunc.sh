#!/bin/bash

if [ -z "$1" ] 
then
	echo "Search generated .c files in the current directory"
	echo "for the method defined in the particular RPython"
	echo "class."
	echo ""
	echo "  usage: $0 simple_class_name method_name"
	echo "   e.g.: $0 WorkerThread run"
	exit 1
fi

ack-grep --type=cc "$1.*$2" --nogroup 2>/dev/null
