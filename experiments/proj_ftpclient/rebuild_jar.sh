#!/bin/bash

./go-integration.sh
./compile_jn.sh
./prepare_j.sh
echo "Compiling client..."
./compile_jclient.sh
echo "Packing jar..."
./pack_jar.sh
echo "Done."
