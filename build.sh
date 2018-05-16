#!/bin/bash

source env/bin/activate
pip3 install -r requirements.txt
mkdir -p dist
rm -r dist/*
cp *.py dist/
cp -rf env/lib/python3.6/site-packages/* dist/
cd dist
zip github_to_s3.zip -r ./*
mv github_to_s3.zip ../
