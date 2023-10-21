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