#!/bin/bash

TESTS="tests/[0-9]"

for f in $TESTS
do
	res=`cat $f | ./program.py`
	ans=`cat $f"_ans"`
	echo $f
	echo -n "Input "
	cat $f
	echo -n "Output "
	echo $res
	if [ $ans = $res ]
	then
		echo "OK"
	else
		echo "Fail "
		echo "Correct Answer: $ans"
	fi
done
