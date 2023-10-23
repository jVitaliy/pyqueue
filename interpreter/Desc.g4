grammar Desc;
script : (setBranch SEMICOLON) (setRepoSource SEMICOLON) gitRepoScope* EOF;
gitRepoScope : (cloneGitToTmp SEMICOLON)  scopeCmds* (closeGitRepo SEMICOLON);
scopeCmds : (deployTo SEMICOLON)
    | (startSystemService SEMICOLON)
    | (stopSystemService SEMICOLON)
    | (buildProject SEMICOLON)
    | gitRepoScope
    ;

setBranch : BRANCH '(' branchName ')';
setRepoSource : REPO_HOST '(' host ')';
host : (namingChars+ DOT)* namingChars+;

buildProject : BUILD_PROJECT '(' projectLanguage COMMA builderType (COMMA buildDir)?')';
projectLanguage : LANGUAGE '=' (JAVA17 | NEXT | PYTHON39);
builderType : 'type=' (MAVEN | GRADLE | NPM);
buildDir : 'dir=' buildFolder;
buildFolder : pathChars+;
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
NPM : 'npm';

LANGUAGE : 'language';
COMMA : ',';
SEMICOLON : ';';
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