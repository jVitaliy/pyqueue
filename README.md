# PyQUEUE project
This project developed for continuous delivery purposes. It can be used on any basis - 
scan folder with task files every N minutes or with queue (zeroMQ for example).
This project works on scanning based. Start file is `process-tasks.sh`. After starting this shell script the scanning will be started at first.
Scanner looks files which ends with `.git` in folder which must be set via PYQUEUE_QUEUE_FOLDER variable.
If there is any task file in queue folder then this file will be opened and the path and branch will be read from it.
Then if in script folder there is a script for this project the interpreter will be started and all directives from this script file will be read and executed.

## Task file
Task file should be named in following scheme: <branch_name>.<repo_name>
For example: develop.ui.git, master.mega-scripts.git.
Task file should contain target path and branch:
```
path:/home/git/rootfolder/project-repo.git
branch:develop
```

Branch from file content should be equal to branch in name of task file
Example:
task file: _*develop.ui.git*_
file content:
```
path:/home/git/rootfolder/ui.git
branch:develop
```

## Folders and files
`interpreter` - is the interpreter package based on Antlr4

`tests` - folder with tests

`processor` - folder with class for processing task files 

`pyqueue_init.sh` - script to put into /etc/sysconfig/tauproject/alcyone-pdm
Script contains system variables for pyqueue scripts and should contain following variables:
- PYQUEUE_QUEUE_FOLDER path to folder where task files are stored
- PYQUEUE_SCRIPT_FOLDER path to folder with DeSc scripts
- PYQUEUE_GIT_HOME git home folder, used to make repo path as relative
- PYQUEUE_LOG_HOME path to log file


# Deploy Script (DeSc)
This is a language to processing deploy from git repo. It is a functional language and grammar likes to Python.
All functions should be separated with semicolon. And all functions joined by logical stage.

There are 7 stages
- Initialization
- Pre-building
- Building
- Post-building
- Configuring
- Deploying
- Cleaning

## Initialization
This stage includes opening git repo and setup for cloning

`branch(master);`  function to open scope for the master branch. 
If the branch name from this function does not match branch name from task file 
then script interpretation will be stopped. 

`repoHost(localhost);`  function to set git repo host or url

`openGitRepoLocally();`  clones git repo locally to temp folder, if there is no any parameter then current repo url will be used.
Current repo url means the url which was read by scanner from task file (path in task file).

## Pre-building

## Building

## Post-building

## Configuring

## Deploying
`deployTo(from=relative/path, /absolute/path, exclude=<pattern>, pattern=<pattern> );` deploy to folder `/absolute/path` parameters 
from, exclude and pattern are not mandatory. Folder `to` should have an absolute path to destination folder.
Folder `from` should have the relative path, it is related on local repo folder which has been created by git clone.
exclude and pattern contain the list of patterns separated by pipline `|`.

Example:
```
deployTo(from=subfolder, /absolute/path, exclude=.git|*.sh, pattern=file.txt|*.jar);
```

## Cleaning
`closeGitRepo();` close locally cloned git repo (removing physically)