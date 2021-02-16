#!/bin/bash

# If file exists
# Create destination directory and move target file
if [ -f "$HOME/data.txt" ]
then
    mkdir /tmp/solve
    cp $HOME/data.txt /tmp/solve/data
    cd /tmp/solve
else
    echo "Input file does not exist or has different name!"
    exit 1
fi

$FILE=data

# Convert from hexdump
xxd -r $FILE $FILE0

while 
