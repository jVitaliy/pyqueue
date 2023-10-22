grammar Desc;
script : cmd ';'(cmd ';')* EOF;
cmd : setBranch
    | setRepoSource
    | cloneGitToTmp
    | closeGitRepo
    | deployTo
    | startSystemService
    | stopSystemService
    | buildProject
    ;

setBranch : BRANCH '(' branchName ')';
setRepoSource : REPO_HOST '(' host ')';
host : (namingChars+ DOT)* namingChars+;

buildProject : BUILD_PROJECT '(' projectLanguage COMMA builderType')';
projectLanguage : LANGUAGE '=' (JAVA17 | NEXT | PYTHON39);
builderType : 'type=' (MAVEN | GRADLE);
deployTo : DEPLOY_TO '(' (pathFrom ',')? pathForDeployTo (
                    (COMMA excludePattern)
                    | (COMMA deployPattern)
                    | (COMMA deployPattern ',' excludePattern)
                    | (COMMA excludePattern ',' deployPattern)
                     )?
                     (COMMA MERGE)?')';
excludePattern : 'exclude=' pattern ('|' pattern)*;
deployPattern : 'pattern=' pattern ('|' pattern)*;
pathForDeployTo : pathForDeploy;
pathFrom : 'from=' pathForDeploy;


cloneGitToTmp : OPEN_GIT_REPO_LOCALLY '(' (repoPath  (COMMA repoAliasName)?)? ')';
closeGitRepo : CLOSE_GIT_REPO '(' repoAliasName? ')';
repoPath: (pathChars | DOT)+ ;
pathForDeploy : pathChars+ ;
pattern : (namingChars | '*' | DOT ) +;
branchName : namingChars+ ;
startSystemService : START_SYSTEM_SERVICE '(' serviceName ')';
stopSystemService : STOP_SYSTEM_SERVICE '(' serviceName ')';
serviceName : namingChars+;
repoAliasName : namingChars+ ;
namingChars: NUM | CHARS | '-' | '_' ;
pathChars : namingChars | '/' ;
MERGE : 'merge';
DOT : '.';
GRADLE : 'gradle';
MAVEN : 'maven';
JAVA17 : 'java17';
NEXT : 'next';
PYTHON39 : 'python39';
LANGUAGE : 'language';
COMMA : ',';
BUILD_PROJECT: 'buildProject';
START_SYSTEM_SERVICE : 'startSystemService';
STOP_SYSTEM_SERVICE : 'stopSystemService';
BRANCH : 'branch';
DEPLOY_TO : 'deployTo';
REPO_HOST : 'repoHost';
OPEN_GIT_REPO_LOCALLY: 'openGitRepoLocally';
CLOSE_GIT_REPO: 'closeGitRepo';
NUM : [0-9] ;
CHARS : [a-zA-Z] ;
WS : [ \t\n\r]+ -> skip ;
LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;