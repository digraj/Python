#! /bin/bash

#$Author: ee364d03 $
#$Date: 2017-01-15 19:12:21 -0500 (Sun, 15 Jan 2017) $
#$Revision: 99180 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S17/students/ee364d03/Prelab01/svncheck.bash $
#$id$

num_lines=$( svn list | wc -l)

while read data
do
	filename=$( svn list $data )
	if [ "$filename" == "$data" ]
	then	
		if ( ! [[ -x $data ]] )
		then
			echo "here"
			svn propset svn:executable ON $data
		fi		
	elif [[ -e $data ]]
	then
		if ( ! [[ -x $data ]] )
		then		
			#echo "$data is not in SVN. Exists but is not executable."			
			echo -n "Make $data executable? (y/n) "	
			read -r answer </dev/tty
			if [ "$answer" == "y" ]
			then
				chmod +x $data
				svn add $data			
			fi	
		else
			svn add $data
		fi
	else
		echo "Error: File $data appears to not exist here or in svn"	
	fi			
	num_lines=$(($num_lines-1))
done < "file_list"
svn commit
echo Auto-commiting code

exit 0
