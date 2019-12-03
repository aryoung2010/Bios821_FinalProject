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

#### 4. Build and Run Docker Image
Next, start a docker image on your machine, using the provided Dockerfile. To do this, simply navigate from terminal to your local copy of the repo and type the following into bash:

*docker build -t soccer*


