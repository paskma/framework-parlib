#!/bin/bash

if [ -z "$1" ] 
then
	echo "Search jasmin (.j) files in the current directory"
	echo "(or a particular file)"
	echo "for methods defined in RPython source code."
	echo ""
	echo "  usage: $0 method_name [filename to search]"
	echo "   e.g.: $0 doOperation"
	echo "   e.g.: $0 doOperation pkg_a/pkg_b/filename/MyClass"
	exit 1
fi

ack-grep --type-add jasmin=.j  "\.method.*o$1\(" --nogroup $2  2>/dev/null
