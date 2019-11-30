#!/usr/bin/env bash

echo "--> build ditribution of GPIB Client"
python setup.py bdist_wheel
echo "--> done"