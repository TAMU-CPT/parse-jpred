#!/bin/bash

for i in jpred_data/*; do
    for file in $i/*; do
        if [[ $file == *.name ]]
            then
                basename=$(basename $file);
                name=${basename::-5}
        fi
        if [[ $file == *.jalview ]]
            then
                jalview=$file;
        fi
    done
    python parse-jpred.py $name $jalview
done
