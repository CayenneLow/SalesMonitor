#!/bin/bash

echo "StaticIce link:"
read link
echo "Name of product"
read name
echo "Highest price that you're willing to pay"
read upperBound
echo "Lowest price that you're willing to pay"
read lowerBound
cat links.json | jq --arg name "$name" --arg link "$link" --arg upperBound "$upperBound" --arg lowerBound "$lowerBound" '.[.| length] |= . + {"name": $name, "link":$link, "upperBound":$upperBound, "lowerBound":$lowerBound}' > temp.json
mv temp.json links.json