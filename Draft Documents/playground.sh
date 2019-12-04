#!/bin/bash
F="soccer.zip"
curl https://gitlab.oit.duke.edu/bios821/european_soccer_database/raw/master/esdb.md5 > esdb.md5
downloadm=$(md5 esdb.md5) #save md5 character/number string downloaded(32,end)
echo $downloadm
echo $downloadm > downloadS
substringD=$(cut -d ' ' -f 4 downloadS)
echo $substringD
string=$(md5 $F) #save md5 character/number string given(32,beginning)
echo $string
#substring=$(cut -d ' ' -f 1 string > substring) #cut to the first element of the string
#check congruence