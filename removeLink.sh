#!/bin/bash

echo "Name of product"
read name
cat links.json | jq --arg name "$name" 'del(.[] | select(.name == $name))' > temp.json
mv temp.json links.json