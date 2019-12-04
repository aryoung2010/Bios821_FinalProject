## BIOS821 Final Project: European Soccer Database
### Allison Young
#### November 2019

### Description

This repository contains code to retrieve and organize data from a kaggle resource of soccer data, 
found at https://www.kaggle.com/hugomathien/soccer. Code for the following steps described in the README, are available as a Jupyter notebook entitled "European_Soccer_Database_Pipeline.ipynb".

### Operating System and Docker Requirements

This package and corresponding code was designed to work with a Mac Operating System (OS) and for users who are already set up to use Docker containers. Please keep this distinction in mind as you use the code and troubleshoot any issues you may encounter. For information on how to set up an account and get started using Docker, you can find useful information on this github page:  
https://github.com/docker/labs/tree/master/beginner/

### Getting Started

#### 1. Download the Data
This repository does not contain any actual data. Thus, in order to use this code, you must first download the database
from https://www.kaggle.com/hugomathien/soccer. From there, the code may be used to automate the rest of the process.

#### 2. Create a MapBox Account
If you wish to add additional functionality using the included soccer_geocode package, you will need to create your own account at https://www.mapbox.com/. Once you have made your own account, locate your account key via the account dashboard for mapbox. Copy this key, which should be a string of characters starting with "pk.", and add it export this vaule as the environmental variable "MAP_PASS" in your local home directory.

In this case, the variable added to your .bash_profile should look something like this, with your own pass key in place of the Xs:

export MAP_PASS="pk.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

For assistance with creating local environment variables in Mac OS, you can check out this helpful article : https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255

### Setting Up Your Environment

Once you have downloaded the data to your computer's Download Folder, created your MapBox Account, and added your API key variable, you are ready to set up your working environment to best utilize the included scripts and packages. 

#### 3. Clone Repo to Local Machine
Clone this repository to desired location on your local machine using gitlab.


#### 4. Build and Run Docker Image (if you do not have appropriate packages and software on your local machine)
Next, start a docker image on your machine, using the provided Dockerfile. To do this, simply navigate from terminal to your local copy of the repo and type the following into bash:

*"docker build -t soccer"*

This will create a container image on your local machine, called soccer. The build process may take several minutes to complete. Once finished, you can check the image has been built correctly by typing the following into bash, and checking that "soccer" is listed.

*"docker images"*

Finally, to run the container, type the following into bash:

*"docker run -it soccer bash"*

This will open the container on your terminal. 

#### 5. Open Repo in Jupyter Notebook or Lab
From here, you can simply type 
*"Jupyter Notebook"*
into the terminal, and it will bring you to a web portal, where you will enter the token provided as part of the html link the first time you open Jupyter. You have the option to set a password for future, more efficient access. 

Finally, you should see the repo on Jupyter Notebook, and be able to access the rest of the code via the jupyter notebook entitled "European_Soccer_Database_Pipeline".

To exit the container at any time and return to your local terminal , press ctrl+d.


### The remaining scripts and codes should now be accessible through the European_Soccer_Database_Pipeline file
This jupyter notebook walks through the process of unzipping the downloaded file, connecting to the soccer database, geocoding the
latitude and longitude of countries and adding them to a new table in the database. Finally, there is script to create analytical
datasets that look at the average number of goals scored per game per season for each country in the database, as well as a summary
dataset that classifies and summarizes the number of "good seasons" listed in the database for each country. A "good season" is defined
as a season where the average number of goals per game is greater than 2.75.

