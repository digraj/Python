#! /bin/bash

#$Author: ee364d03 $
#$Date: 2017-01-15 19:16:35 -0500 (Sun, 15 Jan 2017) $
#$Revision: 99188 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S17/students/ee364d03/Prelab01/exist.bash $
#$id$

Num_Of_Param=$#
Param_Values=$@

for (( I = $Num_Of_Param; I > 0; I-- ))
do	
	if ( ! [[ -r $1 ]])
	then
		touch $1
	else 
		echo "File $1 is readable!"
	fi	
	shift
done
