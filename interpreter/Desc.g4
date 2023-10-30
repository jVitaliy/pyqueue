grammar Desc;
script : ((setBranch SEMICOLON) (setRepoSource SEMICOLON)? (variableSet SEMICOLON)* gitRepoScope*)+ EOF;
gitRepoScope : (cloneGitToTmp SEMICOLON)  scopeCmds* (closeGitRepo SEMICOLON);
scopeCmds : (deployTo SEMICOLON)
    | (startSystemService SEMICOLON)
    | (stopSystemService SEMICOLON)
    | (startSystemServiceRemote SEMICOLON)
    | (stopSystemServiceRemote SEMICOLON)
    | (buildProject SEMICOLON)
    | (buildProject SEMICOLON)
    | (deployToRemote SEMICOLON)
    | (applyConfiguration SEMICOLON)
    | gitRepoScope
    ;

setBranch : BRANCH '(' branchName ')';
setRepoSource : REPO_HOST '(' host ')';
host : (namingChars+ DOT)* namingChars+;
variableSet : variableName EQUALS function ;
variableName : namingChars+;
function : sshCredentials ;
sshCredentials : SSH_CREDENTIALS '(' remoteHostParam COMMA remoteUserParam (COMMA remoteUserPassParam)? ')' ;
buildProject : BUILD_PROJECT '(' (javaBuild | nextBuild | pythonBuild)  (COMMA buildDir)?')';
javaBuild :  LANGUAGE EQUALS JAVA17 COMMA 'type' EQUALS (MAVEN | GRADLE) ;
nextBuild :  LANGUAGE EQUALS NEXT COMMA 'type' EQUALS NPM ;
pythonBuild : LANGUAGE EQUALS PYTHON39 COMMA 'type' EQUALS INSTALL ;
buildDir : 'dir' EQUALS buildFolder;
buildFolder : pathChars+;
deployToRemote : DEPLOY_TO_REMOTE '(' variableName COMMA (pathFrom COMMA)? pathForDeployTo (
                    (COMMA excludePattern)
                    | (COMMA deployPattern)
                    | (COMMA deployPattern COMMA excludePattern)
                    | (COMMA excludePattern COMMA deployPattern)
                     )?
                     (COMMA MERGE)?')';

remoteHostParam : REMOTE_HOST_PARAM EQUALS remoteHost ;
remoteHost : host ;
remoteUserParam : REMOTE_USER_PARAM EQUALS remoteUser ;
remoteUser : namingChars+;
remoteUserPassParam : REMOTE_USER_PASS_PARAM EQUALS remoteUserPassword;
remoteUserPassword : (namingChars | '-' | '_' | '!' | SEMICOLON | ':' | '^' | '#' | '@' | '%'
                    | '^' | '&' | '(' | ')' | '[' | ']' | EQUALS | DOT)+;


deployTo : DEPLOY_TO '(' (pathFrom COMMA)? pathForDeployTo (
                    (COMMA excludePattern)
                    | (COMMA deployPattern)
                    | (COMMA deployPattern COMMA excludePattern)
                    | (COMMA excludePattern COMMA deployPattern)
                     )?
                     (COMMA MERGE)?')';
excludePattern : 'exclude' EQUALS pattern ('|' pattern)*;
deployPattern : 'pattern' EQUALS pattern ('|' pattern)*;
pathForDeployTo : pathForDeploy;
pathFrom : 'from' EQUALS pathForDeploy;

applyConfiguration : APPLY_CONFIGURATION '(' repoPath (COMMA configurationBranch)? (COMMA pathFrom)? (COMMA configurationPath)? COMMA deployPattern (COMMA excludePattern)? ')';
configurationBranch : BRANCH EQUALS configBranchName;
configBranchName : namingChars+;
configurationPath : CONF_PATH EQUALS confPath;
confPath : pathChars+ ;

cloneGitToTmp : OPEN_GIT_REPO_LOCALLY '(' (repoPath  (COMMA repoAliasName)?)? ')';
closeGitRepo : CLOSE_GIT_REPO '(' repoAliasName? ')';
repoPath: (pathChars | DOT)+ ;
pathForDeploy : pathChars+ ;
pattern : (namingChars | '*' | '^' | '\\' | '$' | DOT ) +;
branchName : namingChars+ ;
startSystemService : START_SYSTEM_SERVICE '(' serviceName ')';
stopSystemService : STOP_SYSTEM_SERVICE '(' serviceName ')';
startSystemServiceRemote : START_SYSTEM_SERVICE_REMOTE '(' variableName COMMA serviceName ')';
stopSystemServiceRemote : STOP_SYSTEM_SERVICE_REMOTE '(' variableName COMMA serviceName ')';
serviceName : namingChars+;
repoAliasName : namingChars+ ;
namingChars: NUM | CHARS | '-' | '_' ;
pathChars : namingChars | '/' ;
MERGE : 'merge';
DOT : '.';
EQUALS : '=';
GRADLE : 'gradle';
MAVEN : 'maven';
JAVA17 : 'java17';
NEXT : 'next';
PYTHON39 : 'python39';
INSTALL : 'install';
NPM : 'npm';

LANGUAGE : 'language';
COMMA : ',';
SEMICOLON : ';';
BUILD_PROJECT: 'buildProject';
START_SYSTEM_SERVICE : 'startSystemService';
STOP_SYSTEM_SERVICE : 'stopSystemService';
START_SYSTEM_SERVICE_REMOTE : 'startSystemServiceRemote';
STOP_SYSTEM_SERVICE_REMOTE : 'stopSystemServiceRemote';
BRANCH : 'branch';
CONF_PATH : 'confPath';
DEPLOY_TO : 'deployTo';
SSH_CREDENTIALS : 'sshCredentials';
APPLY_CONFIGURATION : 'applyConfiguration';
DEPLOY_TO_REMOTE : 'deployToRemote';
REMOTE_HOST_PARAM : 'remoteHost' ;
REMOTE_USER_PARAM : 'remoteUser' ;
REMOTE_USER_PASS_PARAM : 'remoteUserPass' ;
REPO_HOST : 'repoHost';
OPEN_GIT_REPO_LOCALLY: 'openGitRepoLocally';
CLOSE_GIT_REPO: 'closeGitRepo';
NUM : [0-9] ;
CHARS : [a-zA-Z] ;
WS : [ \t\n\r]+ -> skip ;
LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;