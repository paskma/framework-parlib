#!/bin/bash

./go-integration-fakesync.sh
par_compile_j.sh
echo "Compiling client..."
./compile_jclient_fakesync.sh
echo "Packing jar..."
./pack_jar_fakesync.sh
echo "Done."
