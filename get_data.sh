#!/bin/bash 

prepare_data()
{ f="soccer.zip" #### assign a variable rather than file
  F="soccer"
  m="esdb.md5" ##### assign variable rather than file
  M="esdb"
  cd $1
  PWD
  if [[ -f "$f" ]]; then
    echo "$f exists"
  else
    echo "$f not found in Download folder. Please see READ_ME for download instructions."
    #curl  https://www.kaggle.com/hugomathien/soccer/download > soccer.zip
    exit
    fi
  cd $2
  if [[ -f $m ]]; then
    echo "$m exists"
  else
    curl https://gitlab.oit.duke.edu/bios821/european_soccer_database/raw/master/esdb.md5 > esdb.md5
    fi
  downloadm=$(md5 esdb.md5) #save md5 character/number string downloaded(32,end)  echo $downloadm
  echo $downloadm 
  substringD=$(cut -d ' ' -f 4 downloadm)
  echo $substringD
  cd $1
  echo $(md5 $f) > string #save md5 character/number string given(32,beginning)
  substring=$(cut -d ' ' -f 4 string) #cut to the first element of the string
  echo $substring
  #check congruence
  if [ $substringD == $substring ]; then
      unzip $F -d $3
	    echo "File has been downloaded and uncompressed."
	else
	  echo "md5 do not match. Please see READ_ME for download instructions."
	  #curl  https://www.kaggle.com/hugomathien/soccer/download > $1/soccer.zip
	  exit
    fi
}


prepare_data $HOME/Downloads  $HOME/Documents/GitLab/md5s  $HOME/Documents/GitLab






 
 
