#!/usr/bin/env bash

mkdir distribution

echo "--> build ditribution of GPIB Client"
python -m pip install dist/GPIB-Client-1.0-py3-none-any.whl

cp dist distibution
cp build distribution

echo "--> done"