#! /bin/bash

#$Author: ee364d03 $
#$Date: 2017-01-15 19:08:44 -0500 (Sun, 15 Jan 2017) $
#$Revision: 99170 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S17/students/ee364d03/Prelab01/sum.bash $
#$id$

Num_Of_Param=$#

addition=0

for (( I = $Num_Of_Param; I > 0; I-- ))
do	
	addition=$(($addition+$1)) 
	shift
done

echo "$addition"

exit 0
