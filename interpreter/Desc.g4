grammar Desc;
script : ((setBranch SEMICOLON) (setRepoSource SEMICOLON)? gitRepoScope*)+ EOF;
gitRepoScope : (cloneGitToTmp SEMICOLON)  scopeCmds* (closeGitRepo SEMICOLON);
scopeCmds : (deployTo SEMICOLON)
    | (startSystemService SEMICOLON)
    | (stopSystemService SEMICOLON)
    | (buildProject SEMICOLON)
    | (deployToRemote SEMICOLON)
    | gitRepoScope
    ;

setBranch : BRANCH '(' branchName ')';
setRepoSource : REPO_HOST '(' host ')';
host : (namingChars+ DOT)* namingChars+;

buildProject : BUILD_PROJECT '(' projectLanguage COMMA builderType (COMMA buildDir)?')';
projectLanguage : LANGUAGE EQUALS (JAVA17 | NEXT | PYTHON39);
builderType : 'type' EQUALS (MAVEN | GRADLE | NPM);
buildDir : 'dir' EQUALS buildFolder;
buildFolder : pathChars+;
deployToRemote : DEPLOY_TO_REMOTE '(' remoteHostParam COMMA remoteUserParam COMMA (remoteUserPassParam COMMA)? (pathFrom COMMA)? pathForDeployTo (
                    (COMMA excludePattern)
                    | (COMMA deployPattern)
                    | (COMMA deployPattern ',' excludePattern)
                    | (COMMA excludePattern ',' deployPattern)
                     )?
                     (COMMA MERGE)?')';

remoteHostParam : REMOTE_HOST_PARAM EQUALS remoteHost ;
remoteHost : host ;
remoteUserParam : REMOTE_USER_PARAM EQUALS remoteUser ;
remoteUser : namingChars+;
remoteUserPassParam : REMOTE_USER_PASS_PARAM EQUALS remoteUserPassword;
remoteUserPassword : (namingChars | '-' | '_' | '!' | ';' | ':' | '^' | '#' | '@' | '%'
                    | '^' | '&' | '(' | ')' | '[' | ']' | EQUALS | DOT)+;


deployTo : DEPLOY_TO '(' (pathFrom ',')? pathForDeployTo (
                    (COMMA excludePattern)
                    | (COMMA deployPattern)
                    | (COMMA deployPattern ',' excludePattern)
                    | (COMMA excludePattern ',' deployPattern)
                     )?
                     (COMMA MERGE)?')';
excludePattern : 'exclude' EQUALS pattern ('|' pattern)*;
deployPattern : 'pattern' EQUALS pattern ('|' pattern)*;
pathForDeployTo : pathForDeploy;
pathFrom : 'from' EQUALS pathForDeploy;


cloneGitToTmp : OPEN_GIT_REPO_LOCALLY '(' (repoPath  (COMMA repoAliasName)?)? ')';
closeGitRepo : CLOSE_GIT_REPO '(' repoAliasName? ')';
repoPath: (pathChars | DOT)+ ;
pathForDeploy : pathChars+ ;
pattern : (namingChars | '*' | '^' | '\\' | '$' | DOT ) +;
branchName : namingChars+ ;
startSystemService : START_SYSTEM_SERVICE '(' serviceName ')';
stopSystemService : STOP_SYSTEM_SERVICE '(' serviceName ')';
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
NPM : 'npm';

LANGUAGE : 'language';
COMMA : ',';
SEMICOLON : ';';
BUILD_PROJECT: 'buildProject';
START_SYSTEM_SERVICE : 'startSystemService';
STOP_SYSTEM_SERVICE : 'stopSystemService';
BRANCH : 'branch';
DEPLOY_TO : 'deployTo';
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