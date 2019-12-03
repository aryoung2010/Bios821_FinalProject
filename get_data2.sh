#!/bin/bash 

prepare_data(){
  F = "soccer.zip" #### assign a variable rather than file
  m= "esdb.md5" > m ##### assign variable rather than file
  cd $1
  if [[ -f $F ]]; then
    echo "$F exists"
  else
    curl  https://www.kaggle.com/hugomathien/soccer/download > soccer.zip
    fi
  cd $2
  if [[ -f $m ]]; then
    echo "$m exists"
  else
    curl https://gitlab.oit.duke.edu/bios821/european_soccer_database/raw/master/esdb.md5 > esdb.md5
    fi
  md5 esdb.md5 > downloadm #save md5 character/number string downloaded(32,end)
  downloadS = cat downloadm
  substringD = cut -d ' ' -f 4 downloadS
  string = md5 $F #save md5 character/number string given(32,beginning)
  substring = cut -d ' ' -f 1 string > substring #cut to the first element of the string
  #check congruence
  if [$substringD == $substring]; then
      cd $1
      unzip $F -d $3
	    echo "File has been downloaded and uncompressed."
	else
	  echo "md5 do not match. Downloading database."
	  curl  https://www.kaggle.com/hugomathien/soccer/download > $1/soccer.zip
	  cd $3
	  unzip $F -d $3
	  echo "File has been downloaded and uncompressed."
	  exit
    fi
    }

prepare_data $HOME/Downloads  $HOME/Documents/GitLab/md5s  $HOME/Documents/GitLab






 
 
