#! /bin/bash

#$Author: ee364d03 $
#$Date: 2017-01-15 19:16:35 -0500 (Sun, 15 Jan 2017) $
#$Revision: 99188 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S17/students/ee364d03/Prelab01/line_num.bash $
#$id$

Num_Of_Param=$#
counter=1
if (( $Num_Of_Param == 1 ))
then
	if ([[ -r $1 ]])
	then
		while read data
		do
			echo "$counter:$data"
			counter=$(($counter+1))	
		done < $1
	else
		echo "Cannot read $1"
		exit 1		
	fi
elif (($Num_Of_Param != 1))
then
	echo "Usage: line_num.bash <filename>"
	exit 1
fi

exit 0
