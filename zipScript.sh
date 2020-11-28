#!/bin/sh
pip3 install --system --target ./package -r requirements.txt
zip -r upload.zip ./package/* *.py links.json