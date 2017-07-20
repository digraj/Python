#! /bin/bash

sum=0

for (( i = 0; i < $#; i++ ))
do
	echo $i	$1
	sum=$(($sum+$1))
	shift
#	echo $sum
done

echo $sum
