#!/bin/bash

./go-integration.sh
par_compile_j.sh
echo "Compiling client..."
./compile_jclient.sh
echo "Packing jar..."
./pack_jar.sh
echo "Done."
