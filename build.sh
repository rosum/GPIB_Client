#!/usr/bin/env bash

mkdir distribution

echo "--> build ditribution of GPIB Client"

python setup.py bdist_wheel

cp -rf dist distibution


echo "--> done"