#! /bin/bash

#$Author: ee364d03 $
#$Date: 2017-01-15 19:12:21 -0500 (Sun, 15 Jan 2017) $
#$Revision: 99180 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S17/students/ee364d03/Prelab01/sensor_sum.sh $
#$id$

if (( $# == 1 ))
then
	if [[ -r $1 ]]	
	then	
		while read sensorid n0 n1 n2
		do
			sensor=$(echo $sensorid | cut -b 1-2)
			echo -n "$sensor "
			addition=$(($n0+$n1+$n2))
			echo "$addition"
		done < $1
	else
		echo "error: $1 is not a readable file!"
		exit 1
	fi
else
	echo "usage: sensor_sum.sh log"
	exit 1
fi

exit 0
