grammar Desc;
script : cmd ';'(cmd ';')* EOF;
cmd : setBranch
    | setRepoSource
    | cloneGitToTmp
    | closeGitRepo
    | deployTo
    ;
deployTo : DEPLOY_TO '(' (pathFrom ',')? pathForDeployTo (
                    (',' excludePattern)
                    | (',' deployPattern)
                    | (',' deployPattern ',' excludePattern)
                    | (',' excludePattern ',' deployPattern)
                     )?  ')';
excludePattern : 'exclude=' pattern ('|' pattern)*;
deployPattern : 'pattern=' pattern ('|' pattern)*;
pathForDeployTo : pathForDeploy;
pathFrom : 'from=' pathForDeploy;
setBranch : BRANCH '(' branchName ')';
setRepoSource : REPO_HOST '(' host ')';
host : (namingChars+ '.')* namingChars+;
cloneGitToTmp : OPEN_GIT_REPO_LOCALLY '(' (repoPath  (',' repoAliasName)?)? ')';
closeGitRepo : CLOSE_GIT_REPO '(' repoAliasName? ')';
repoPath: namingChars+ ;
pathForDeploy : ( namingChars | '/')+ ;
pattern : (namingChars | '*' | '.' ) +;
branchName : namingChars+ ;
//expr : atom | ('+' | '-') expr | expr '**' expr | expr ('*' | '/') expr | expr ('+' | '-') expr | '(' expr ')' | atom ;
//atom : INT ;
repoAliasName : namingChars+ ;
namingChars: NUM | CHARS | '-' | '_' ;
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