#!/bin/sh
mkdir package
pip3 install --target ./package -r requirements.txt
zip -r upload.zip ./package/* *.py links.json