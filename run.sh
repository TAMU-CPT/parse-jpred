#!/bin/bash

for i in jpred_data/*; do
    echo $i
    for jalview in $i/*.jalview; do
        echo "$jalview";
    done
    for name in $i/*.name; do
        echo "$name";
    done
    python parse-jpred.py $name $jalview
done
