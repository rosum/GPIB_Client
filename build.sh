#!/usr/bin/env bash

mkdir distribution

echo "--> build ditribution of GPIB Client"

python setup.py bdist_wheel

cp dist distibution
cp build distribution

echo "--> done"