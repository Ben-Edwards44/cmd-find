#!/usr/bin/env bash


if [ $1 = "1" ]
then
    help
elif [ $1 = "2" ]
then
    help -d $2
else
    echo "INVALID ARGUMENTS"
fi