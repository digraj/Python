#! /bin/bash

#$Author: ee364d03 $
#$Date: 2017-01-15 19:12:21 -0500 (Sun, 15 Jan 2017) $
#$Revision: 99180 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S17/students/ee364d03/Prelab01/check_file.bash $
#$id$

Num_Of_Param=$#
Param_Values=$@

if (( $Num_Of_Param == 1 ))
then
	if ([[ -e $1 ]])
	then
		echo "$1 exists " 
	else
		echo "$1 does not exist"	
	fi

	if ([[ -d $1 ]])
	then
		echo "$1 is a directory " 
	else
		echo "$1 is not a directory"	
	fi

	if ([[ -f $1 ]])
	then
		echo "$1 is an ordinary file " 
	else
		echo "$1 is not an ordinary file"	
	fi

	if ([[ -r $1 ]])
	then
		echo "$1 is readable " 
	else
		echo "$1 is not readable"	
	fi

	if ([[ -w $1 ]])
	then
		echo "$1 is writable " 
	else
		echo "$1 is not writable"	
	fi

	if ([[ -x $1 ]])
	then
		echo "$1 is executable " 
	else
		echo "$1 is not executable"	
	fi
elif (($Num_Of_Param != 1))
then
	echo "Usage: ./check_file.bash <filename>"
	exit 1
fi

exit 0