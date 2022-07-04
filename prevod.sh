#!/usr/bin/bash

sed -i '/\[\[\[ excs.*/,/\]\]\]/s/- \(.*\)/::exc[excs>\1]/' $1
sed -i 's/\[\[\[ excs/##/' $1
sed -i '/\]\]\]/d' $1
