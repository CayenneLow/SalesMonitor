#!/bin/sh
pip3 install --system --target ./package -r requirements.txt
cd package
zip -r upload.zip ./* 
mv ./upload.zip ../
cd ..
zip upload.zip *.py links.json