#! /bin/bash

#---------------------------------------
# $Author: ee364d03 $
# $Date: 2017-01-24 17:11:30 -0500 (Tue, 24 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

finish=0
words=(banana parsimonious sesquipedalian)
option=$(( $RANDOM % 3 ))
selected=${words[option]}

num_letters=$(echo $selected | wc -c)
let num_letters=$num_letters-1

echo Your word is $num_letters letters long.
echo -n Word is:

for (( I = 0; I < $num_letters; I++ ))
do
	selected_word[$I]=${selected:$I:1}
	dummy[$I]="."	
	echo -n " ."
done

echo

while (( $finish != 1 ))
do
	let yes=1
	let match=0
	echo -n "Make a guess: "	
	read guess
	echo
	for (( I = 0; I < $num_letters; I++ ))
	do
		if [ $guess == ${selected_word[$I]} ]
		then
			let match=1
			dummy[$I]=$guess
		fi
	done

	for (( I = 0; I < $num_letters; I++ ))
	do
		if [ ${dummy[$I]} != ${selected_word[$I]} ]
		then
			yes=0 
		fi	
	done



	if (( yes == 1 ))
	then
		let finish=1
		echo Good going!
		echo Congratulations! You guessed the word: $selected
		break	
	fi


	if (( match == 1 ))
	then
		echo -n "Good going! Word is: "
	else
		echo -n "Sorry, try again. Word is: "
	fi

	
	echo ${dummy[*]}	

done
echo

exit 0
