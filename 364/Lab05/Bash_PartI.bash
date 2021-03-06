#! /bin/bash

#----------------------------------
# $Author: ee364d03 $
# $Date: 2017-02-14 17:14:29 -0500 (Tue, 14 Feb 2017) $
#----------------------------------

function part_a 
{               
	python3.4 prelab.py > output.txt 2>&1
    	return                      
}                               

function part_b
{              
    # Fill out your answer here
    return                     
}                              

function part_c
{
	rm a.out > /dev/null 2>&1
    	for names in ./src/*.c
	do
		gcc $names > /dev/null 2>&1
		name=$(echo $names | cut -d"/" -f3)
		if [[ -e a.out ]]
		then
			echo "$name: success"
		else
			echo "$name: failure"
		fi
	done
    	return
}

function part_d
{
   	Arr=(a.txt b.txt c.txt d.txt)
	option=$(( $RANDOM % 4 ))
	selected=${Arr[option]}
	value=$(cat $selected)
	toprint=$(echo $value | cut -d" " -f4-6)
	toprint_2=($toprint)
	echo ${toprint_2[0]}
	echo ${toprint_2[1]}
	echo ${toprint_2[2]}
    	return
}

function part_e
{
    	value=$(ping ecegrid.ecn.purdue.edu -U -c3 | tail -n1)
	average=$(echo $value | cut -d"/" -f5)
	echo $average ms

	return
}

# To test your function, you can call it below like this:
#
part_a
part_c
part_d
part_e
