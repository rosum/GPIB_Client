#!/usr/bin/env bash

echo "--> upload to nexus"

twine upload -u python -p $pw  --repository-url https://nexus.janrosum.com/repository/python/ dist/*

echo "--> uploaded to nexus"