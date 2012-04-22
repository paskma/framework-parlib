#!/bin/bash

PYTHONPATH=../../parlib_soptpure:../../parlib_portable python themain.py $@ &

. ./memsnip.sh
