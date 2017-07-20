#! /bin/bash

#---------------------------------------
# $Author: ee364d03 $
# $Date: 2017-01-17 16:18:07 -0500 (Tue, 17 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

medal_sum=0
athlete_sum=0
highest=0
player=0
if (( $# != 2 )) 
then
	echo "Usage: collect_stats.bash <file> <sport>"
	echo
	exit 1
else
	if ( ! [[ -e $1 ]] )
	then
		echo "Error: $1 does not exist"
		echo
		exit 2
	else
		while read data
		do
			name=$(echo $data | cut -d"," -f1)
			sport=$(echo  $data | cut -d"," -f2)
			medals=$(echo  $data | cut -d"," -f3)
			if [[ $2 == $sport ]]
			then
				let medal_sum=$medal_sum+$medals
				let athlete_sum=$athlete_sum+1
				if (( $highest < $medals ))
				then
					let highest=$medals
					player=$name
				fi
			fi	
		done < $1 
	fi
fi

echo Total athletes: $athlete_sum
echo Total medals won: $medal_sum
echo $player won the most medals: $highest
echo

exit 0
