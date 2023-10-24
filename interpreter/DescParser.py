# Generated from interpreter/Desc.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,274,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,96,8,2,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,4,5,109,8,5,11,5,12,
        5,110,1,5,1,5,5,5,115,8,5,10,5,12,5,118,9,5,1,5,4,5,121,8,5,11,5,
        12,5,122,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,132,8,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,4,10,147,8,10,11,10,12,10,148,
        1,11,1,11,1,11,1,11,1,11,3,11,156,8,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,173,8,11,
        1,11,1,11,3,11,177,8,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,185,8,
        12,10,12,12,12,188,9,12,1,13,1,13,1,13,1,13,5,13,194,8,13,10,13,
        12,13,197,9,13,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        3,16,209,8,16,3,16,211,8,16,1,16,1,16,1,17,1,17,1,17,3,17,218,8,
        17,1,17,1,17,1,18,1,18,4,18,224,8,18,11,18,12,18,225,1,19,4,19,229,
        8,19,11,19,12,19,230,1,20,1,20,1,20,1,20,1,20,1,20,4,20,239,8,20,
        11,20,12,20,240,1,21,4,21,244,8,21,11,21,12,21,245,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,4,24,259,8,24,11,24,12,24,
        260,1,25,4,25,264,8,25,11,25,12,25,265,1,26,1,26,1,27,1,27,3,27,
        272,8,27,1,27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,0,3,1,0,21,23,2,0,19,20,24,24,
        2,0,14,15,36,37,280,0,56,1,0,0,0,2,70,1,0,0,0,4,95,1,0,0,0,6,97,
        1,0,0,0,8,102,1,0,0,0,10,116,1,0,0,0,12,124,1,0,0,0,14,135,1,0,0,
        0,16,139,1,0,0,0,18,142,1,0,0,0,20,146,1,0,0,0,22,150,1,0,0,0,24,
        180,1,0,0,0,26,189,1,0,0,0,28,198,1,0,0,0,30,200,1,0,0,0,32,203,
        1,0,0,0,34,214,1,0,0,0,36,223,1,0,0,0,38,228,1,0,0,0,40,238,1,0,
        0,0,42,243,1,0,0,0,44,247,1,0,0,0,46,252,1,0,0,0,48,258,1,0,0,0,
        50,263,1,0,0,0,52,267,1,0,0,0,54,271,1,0,0,0,56,57,3,6,3,0,57,58,
        5,27,0,0,58,59,1,0,0,0,59,60,3,8,4,0,60,61,5,27,0,0,61,65,1,0,0,
        0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,
        1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,
        71,3,32,16,0,71,72,5,27,0,0,72,76,1,0,0,0,73,75,3,4,2,0,74,73,1,
        0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,
        76,1,0,0,0,79,80,3,34,17,0,80,81,5,27,0,0,81,3,1,0,0,0,82,83,3,22,
        11,0,83,84,5,27,0,0,84,96,1,0,0,0,85,86,3,44,22,0,86,87,5,27,0,0,
        87,96,1,0,0,0,88,89,3,46,23,0,89,90,5,27,0,0,90,96,1,0,0,0,91,92,
        3,12,6,0,92,93,5,27,0,0,93,96,1,0,0,0,94,96,3,2,1,0,95,82,1,0,0,
        0,95,85,1,0,0,0,95,88,1,0,0,0,95,91,1,0,0,0,95,94,1,0,0,0,96,5,1,
        0,0,0,97,98,5,31,0,0,98,99,5,1,0,0,99,100,3,42,21,0,100,101,5,2,
        0,0,101,7,1,0,0,0,102,103,5,33,0,0,103,104,5,1,0,0,104,105,3,10,
        5,0,105,106,5,2,0,0,106,9,1,0,0,0,107,109,3,52,26,0,108,107,1,0,
        0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,112,1,0,
        0,0,112,113,5,18,0,0,113,115,1,0,0,0,114,108,1,0,0,0,115,118,1,0,
        0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,120,1,0,0,0,118,116,1,0,
        0,0,119,121,3,52,26,0,120,119,1,0,0,0,121,122,1,0,0,0,122,120,1,
        0,0,0,122,123,1,0,0,0,123,11,1,0,0,0,124,125,5,28,0,0,125,126,5,
        1,0,0,126,127,3,14,7,0,127,128,5,26,0,0,128,131,3,16,8,0,129,130,
        5,26,0,0,130,132,3,18,9,0,131,129,1,0,0,0,131,132,1,0,0,0,132,133,
        1,0,0,0,133,134,5,2,0,0,134,13,1,0,0,0,135,136,5,25,0,0,136,137,
        5,3,0,0,137,138,7,0,0,0,138,15,1,0,0,0,139,140,5,4,0,0,140,141,7,
        1,0,0,141,17,1,0,0,0,142,143,5,5,0,0,143,144,3,20,10,0,144,19,1,
        0,0,0,145,147,3,54,27,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,21,1,0,0,0,150,151,5,32,0,0,151,155,
        5,1,0,0,152,153,3,30,15,0,153,154,5,26,0,0,154,156,1,0,0,0,155,152,
        1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,172,3,28,14,0,158,159,
        5,26,0,0,159,173,3,24,12,0,160,161,5,26,0,0,161,173,3,26,13,0,162,
        163,5,26,0,0,163,164,3,26,13,0,164,165,5,26,0,0,165,166,3,24,12,
        0,166,173,1,0,0,0,167,168,5,26,0,0,168,169,3,24,12,0,169,170,5,26,
        0,0,170,171,3,26,13,0,171,173,1,0,0,0,172,158,1,0,0,0,172,160,1,
        0,0,0,172,162,1,0,0,0,172,167,1,0,0,0,172,173,1,0,0,0,173,176,1,
        0,0,0,174,175,5,26,0,0,175,177,5,17,0,0,176,174,1,0,0,0,176,177,
        1,0,0,0,177,178,1,0,0,0,178,179,5,2,0,0,179,23,1,0,0,0,180,181,5,
        6,0,0,181,186,3,40,20,0,182,183,5,7,0,0,183,185,3,40,20,0,184,182,
        1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,25,1,
        0,0,0,188,186,1,0,0,0,189,190,5,8,0,0,190,195,3,40,20,0,191,192,
        5,7,0,0,192,194,3,40,20,0,193,191,1,0,0,0,194,197,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,27,1,0,0,0,197,195,1,0,0,0,198,199,3,
        38,19,0,199,29,1,0,0,0,200,201,5,9,0,0,201,202,3,38,19,0,202,31,
        1,0,0,0,203,204,5,34,0,0,204,210,5,1,0,0,205,208,3,36,18,0,206,207,
        5,26,0,0,207,209,3,50,25,0,208,206,1,0,0,0,208,209,1,0,0,0,209,211,
        1,0,0,0,210,205,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,213,
        5,2,0,0,213,33,1,0,0,0,214,215,5,35,0,0,215,217,5,1,0,0,216,218,
        3,50,25,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,219,220,
        5,2,0,0,220,35,1,0,0,0,221,224,3,54,27,0,222,224,5,18,0,0,223,221,
        1,0,0,0,223,222,1,0,0,0,224,225,1,0,0,0,225,223,1,0,0,0,225,226,
        1,0,0,0,226,37,1,0,0,0,227,229,3,54,27,0,228,227,1,0,0,0,229,230,
        1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,39,1,0,0,0,232,239,3,
        52,26,0,233,239,5,10,0,0,234,239,5,11,0,0,235,239,5,12,0,0,236,239,
        5,13,0,0,237,239,5,18,0,0,238,232,1,0,0,0,238,233,1,0,0,0,238,234,
        1,0,0,0,238,235,1,0,0,0,238,236,1,0,0,0,238,237,1,0,0,0,239,240,
        1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,41,1,0,0,0,242,244,3,
        52,26,0,243,242,1,0,0,0,244,245,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,43,1,0,0,0,247,248,5,29,0,0,248,249,5,1,0,0,249,250,
        3,48,24,0,250,251,5,2,0,0,251,45,1,0,0,0,252,253,5,30,0,0,253,254,
        5,1,0,0,254,255,3,48,24,0,255,256,5,2,0,0,256,47,1,0,0,0,257,259,
        3,52,26,0,258,257,1,0,0,0,259,260,1,0,0,0,260,258,1,0,0,0,260,261,
        1,0,0,0,261,49,1,0,0,0,262,264,3,52,26,0,263,262,1,0,0,0,264,265,
        1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,51,1,0,0,0,267,268,7,
        2,0,0,268,53,1,0,0,0,269,272,3,52,26,0,270,272,5,16,0,0,271,269,
        1,0,0,0,271,270,1,0,0,0,272,55,1,0,0,0,25,65,76,95,110,116,122,131,
        148,155,172,176,186,195,208,210,217,223,225,230,238,240,245,260,
        265,271
    ]

class DescParser ( Parser ):

    grammarFileName = "Desc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'type='", "'dir='", 
                     "'exclude='", "'|'", "'pattern='", "'from='", "'*'", 
                     "'^'", "'\\'", "'$'", "'-'", "'_'", "'/'", "'merge'", 
                     "'.'", "'gradle'", "'maven'", "'java17'", "'next'", 
                     "'python39'", "'npm'", "'language'", "','", "';'", 
                     "'buildProject'", "'startSystemService'", "'stopSystemService'", 
                     "'branch'", "'deployTo'", "'repoHost'", "'openGitRepoLocally'", 
                     "'closeGitRepo'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MERGE", "DOT", "GRADLE", "MAVEN", "JAVA17", 
                      "NEXT", "PYTHON39", "NPM", "LANGUAGE", "COMMA", "SEMICOLON", 
                      "BUILD_PROJECT", "START_SYSTEM_SERVICE", "STOP_SYSTEM_SERVICE", 
                      "BRANCH", "DEPLOY_TO", "REPO_HOST", "OPEN_GIT_REPO_LOCALLY", 
                      "CLOSE_GIT_REPO", "NUM", "CHARS", "WS", "LINE_COMMENT" ]

    RULE_script = 0
    RULE_gitRepoScope = 1
    RULE_scopeCmds = 2
    RULE_setBranch = 3
    RULE_setRepoSource = 4
    RULE_host = 5
    RULE_buildProject = 6
    RULE_projectLanguage = 7
    RULE_builderType = 8
    RULE_buildDir = 9
    RULE_buildFolder = 10
    RULE_deployTo = 11
    RULE_excludePattern = 12
    RULE_deployPattern = 13
    RULE_pathForDeployTo = 14
    RULE_pathFrom = 15
    RULE_cloneGitToTmp = 16
    RULE_closeGitRepo = 17
    RULE_repoPath = 18
    RULE_pathForDeploy = 19
    RULE_pattern = 20
    RULE_branchName = 21
    RULE_startSystemService = 22
    RULE_stopSystemService = 23
    RULE_serviceName = 24
    RULE_repoAliasName = 25
    RULE_namingChars = 26
    RULE_pathChars = 27

    ruleNames =  [ "script", "gitRepoScope", "scopeCmds", "setBranch", "setRepoSource", 
                   "host", "buildProject", "projectLanguage", "builderType", 
                   "buildDir", "buildFolder", "deployTo", "excludePattern", 
                   "deployPattern", "pathForDeployTo", "pathFrom", "cloneGitToTmp", 
                   "closeGitRepo", "repoPath", "pathForDeploy", "pattern", 
                   "branchName", "startSystemService", "stopSystemService", 
                   "serviceName", "repoAliasName", "namingChars", "pathChars" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    MERGE=17
    DOT=18
    GRADLE=19
    MAVEN=20
    JAVA17=21
    NEXT=22
    PYTHON39=23
    NPM=24
    LANGUAGE=25
    COMMA=26
    SEMICOLON=27
    BUILD_PROJECT=28
    START_SYSTEM_SERVICE=29
    STOP_SYSTEM_SERVICE=30
    BRANCH=31
    DEPLOY_TO=32
    REPO_HOST=33
    OPEN_GIT_REPO_LOCALLY=34
    CLOSE_GIT_REPO=35
    NUM=36
    CHARS=37
    WS=38
    LINE_COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DescParser.EOF, 0)

        def setBranch(self):
            return self.getTypedRuleContext(DescParser.SetBranchContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.SEMICOLON)
            else:
                return self.getToken(DescParser.SEMICOLON, i)

        def setRepoSource(self):
            return self.getTypedRuleContext(DescParser.SetRepoSourceContext,0)


        def gitRepoScope(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.GitRepoScopeContext)
            else:
                return self.getTypedRuleContext(DescParser.GitRepoScopeContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = DescParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.setBranch()
            self.state = 57
            self.match(DescParser.SEMICOLON)

            self.state = 59
            self.setRepoSource()
            self.state = 60
            self.match(DescParser.SEMICOLON)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 62
                self.gitRepoScope()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(DescParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GitRepoScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cloneGitToTmp(self):
            return self.getTypedRuleContext(DescParser.CloneGitToTmpContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.SEMICOLON)
            else:
                return self.getToken(DescParser.SEMICOLON, i)

        def closeGitRepo(self):
            return self.getTypedRuleContext(DescParser.CloseGitRepoContext,0)


        def scopeCmds(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.ScopeCmdsContext)
            else:
                return self.getTypedRuleContext(DescParser.ScopeCmdsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_gitRepoScope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGitRepoScope" ):
                listener.enterGitRepoScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGitRepoScope" ):
                listener.exitGitRepoScope(self)




    def gitRepoScope(self):

        localctx = DescParser.GitRepoScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_gitRepoScope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.cloneGitToTmp()
            self.state = 71
            self.match(DescParser.SEMICOLON)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 23353884672) != 0):
                self.state = 73
                self.scopeCmds()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.closeGitRepo()
            self.state = 80
            self.match(DescParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeCmdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deployTo(self):
            return self.getTypedRuleContext(DescParser.DeployToContext,0)


        def SEMICOLON(self):
            return self.getToken(DescParser.SEMICOLON, 0)

        def startSystemService(self):
            return self.getTypedRuleContext(DescParser.StartSystemServiceContext,0)


        def stopSystemService(self):
            return self.getTypedRuleContext(DescParser.StopSystemServiceContext,0)


        def buildProject(self):
            return self.getTypedRuleContext(DescParser.BuildProjectContext,0)


        def gitRepoScope(self):
            return self.getTypedRuleContext(DescParser.GitRepoScopeContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_scopeCmds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScopeCmds" ):
                listener.enterScopeCmds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScopeCmds" ):
                listener.exitScopeCmds(self)




    def scopeCmds(self):

        localctx = DescParser.ScopeCmdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_scopeCmds)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.deployTo()
                self.state = 83
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.startSystemService()
                self.state = 86
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.stopSystemService()
                self.state = 89
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.buildProject()
                self.state = 92
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.gitRepoScope()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetBranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRANCH(self):
            return self.getToken(DescParser.BRANCH, 0)

        def branchName(self):
            return self.getTypedRuleContext(DescParser.BranchNameContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_setBranch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetBranch" ):
                listener.enterSetBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetBranch" ):
                listener.exitSetBranch(self)




    def setBranch(self):

        localctx = DescParser.SetBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_setBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(DescParser.BRANCH)
            self.state = 98
            self.match(DescParser.T__0)
            self.state = 99
            self.branchName()
            self.state = 100
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetRepoSourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPO_HOST(self):
            return self.getToken(DescParser.REPO_HOST, 0)

        def host(self):
            return self.getTypedRuleContext(DescParser.HostContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_setRepoSource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetRepoSource" ):
                listener.enterSetRepoSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetRepoSource" ):
                listener.exitSetRepoSource(self)




    def setRepoSource(self):

        localctx = DescParser.SetRepoSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_setRepoSource)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(DescParser.REPO_HOST)
            self.state = 103
            self.match(DescParser.T__0)
            self.state = 104
            self.host()
            self.state = 105
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.DOT)
            else:
                return self.getToken(DescParser.DOT, i)

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHost" ):
                listener.enterHost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHost" ):
                listener.exitHost(self)




    def host(self):

        localctx = DescParser.HostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 107
                        self.namingChars()
                        self.state = 110 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                            break

                    self.state = 112
                    self.match(DescParser.DOT) 
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.namingChars()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuildProjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUILD_PROJECT(self):
            return self.getToken(DescParser.BUILD_PROJECT, 0)

        def projectLanguage(self):
            return self.getTypedRuleContext(DescParser.ProjectLanguageContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.COMMA)
            else:
                return self.getToken(DescParser.COMMA, i)

        def builderType(self):
            return self.getTypedRuleContext(DescParser.BuilderTypeContext,0)


        def buildDir(self):
            return self.getTypedRuleContext(DescParser.BuildDirContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_buildProject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuildProject" ):
                listener.enterBuildProject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuildProject" ):
                listener.exitBuildProject(self)




    def buildProject(self):

        localctx = DescParser.BuildProjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_buildProject)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(DescParser.BUILD_PROJECT)
            self.state = 125
            self.match(DescParser.T__0)
            self.state = 126
            self.projectLanguage()
            self.state = 127
            self.match(DescParser.COMMA)
            self.state = 128
            self.builderType()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 129
                self.match(DescParser.COMMA)
                self.state = 130
                self.buildDir()


            self.state = 133
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProjectLanguageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LANGUAGE(self):
            return self.getToken(DescParser.LANGUAGE, 0)

        def JAVA17(self):
            return self.getToken(DescParser.JAVA17, 0)

        def NEXT(self):
            return self.getToken(DescParser.NEXT, 0)

        def PYTHON39(self):
            return self.getToken(DescParser.PYTHON39, 0)

        def getRuleIndex(self):
            return DescParser.RULE_projectLanguage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProjectLanguage" ):
                listener.enterProjectLanguage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProjectLanguage" ):
                listener.exitProjectLanguage(self)




    def projectLanguage(self):

        localctx = DescParser.ProjectLanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_projectLanguage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(DescParser.LANGUAGE)
            self.state = 136
            self.match(DescParser.T__2)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuilderTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAVEN(self):
            return self.getToken(DescParser.MAVEN, 0)

        def GRADLE(self):
            return self.getToken(DescParser.GRADLE, 0)

        def NPM(self):
            return self.getToken(DescParser.NPM, 0)

        def getRuleIndex(self):
            return DescParser.RULE_builderType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilderType" ):
                listener.enterBuilderType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilderType" ):
                listener.exitBuilderType(self)




    def builderType(self):

        localctx = DescParser.BuilderTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_builderType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(DescParser.T__3)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18350080) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuildDirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def buildFolder(self):
            return self.getTypedRuleContext(DescParser.BuildFolderContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_buildDir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuildDir" ):
                listener.enterBuildDir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuildDir" ):
                listener.exitBuildDir(self)




    def buildDir(self):

        localctx = DescParser.BuildDirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_buildDir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(DescParser.T__4)
            self.state = 143
            self.buildFolder()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuildFolderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.PathCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.PathCharsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_buildFolder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuildFolder" ):
                listener.enterBuildFolder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuildFolder" ):
                listener.exitBuildFolder(self)




    def buildFolder(self):

        localctx = DescParser.BuildFolderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_buildFolder)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.pathChars()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158544896) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeployToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEPLOY_TO(self):
            return self.getToken(DescParser.DEPLOY_TO, 0)

        def pathForDeployTo(self):
            return self.getTypedRuleContext(DescParser.PathForDeployToContext,0)


        def pathFrom(self):
            return self.getTypedRuleContext(DescParser.PathFromContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.COMMA)
            else:
                return self.getToken(DescParser.COMMA, i)

        def MERGE(self):
            return self.getToken(DescParser.MERGE, 0)

        def excludePattern(self):
            return self.getTypedRuleContext(DescParser.ExcludePatternContext,0)


        def deployPattern(self):
            return self.getTypedRuleContext(DescParser.DeployPatternContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_deployTo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeployTo" ):
                listener.enterDeployTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeployTo" ):
                listener.exitDeployTo(self)




    def deployTo(self):

        localctx = DescParser.DeployToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_deployTo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(DescParser.DEPLOY_TO)
            self.state = 151
            self.match(DescParser.T__0)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 152
                self.pathFrom()
                self.state = 153
                self.match(DescParser.COMMA)


            self.state = 157
            self.pathForDeployTo()
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 158
                self.match(DescParser.COMMA)
                self.state = 159
                self.excludePattern()

            elif la_ == 2:
                self.state = 160
                self.match(DescParser.COMMA)
                self.state = 161
                self.deployPattern()

            elif la_ == 3:
                self.state = 162
                self.match(DescParser.COMMA)
                self.state = 163
                self.deployPattern()
                self.state = 164
                self.match(DescParser.COMMA)
                self.state = 165
                self.excludePattern()

            elif la_ == 4:
                self.state = 167
                self.match(DescParser.COMMA)
                self.state = 168
                self.excludePattern()
                self.state = 169
                self.match(DescParser.COMMA)
                self.state = 170
                self.deployPattern()


            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 174
                self.match(DescParser.COMMA)
                self.state = 175
                self.match(DescParser.MERGE)


            self.state = 178
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExcludePatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.PatternContext)
            else:
                return self.getTypedRuleContext(DescParser.PatternContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_excludePattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExcludePattern" ):
                listener.enterExcludePattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExcludePattern" ):
                listener.exitExcludePattern(self)




    def excludePattern(self):

        localctx = DescParser.ExcludePatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_excludePattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(DescParser.T__5)
            self.state = 181
            self.pattern()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 182
                self.match(DescParser.T__6)
                self.state = 183
                self.pattern()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeployPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.PatternContext)
            else:
                return self.getTypedRuleContext(DescParser.PatternContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_deployPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeployPattern" ):
                listener.enterDeployPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeployPattern" ):
                listener.exitDeployPattern(self)




    def deployPattern(self):

        localctx = DescParser.DeployPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_deployPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(DescParser.T__7)
            self.state = 190
            self.pattern()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 191
                self.match(DescParser.T__6)
                self.state = 192
                self.pattern()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathForDeployToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathForDeploy(self):
            return self.getTypedRuleContext(DescParser.PathForDeployContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_pathForDeployTo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathForDeployTo" ):
                listener.enterPathForDeployTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathForDeployTo" ):
                listener.exitPathForDeployTo(self)




    def pathForDeployTo(self):

        localctx = DescParser.PathForDeployToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_pathForDeployTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.pathForDeploy()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathFromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathForDeploy(self):
            return self.getTypedRuleContext(DescParser.PathForDeployContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_pathFrom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathFrom" ):
                listener.enterPathFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathFrom" ):
                listener.exitPathFrom(self)




    def pathFrom(self):

        localctx = DescParser.PathFromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pathFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(DescParser.T__8)
            self.state = 201
            self.pathForDeploy()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloneGitToTmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_GIT_REPO_LOCALLY(self):
            return self.getToken(DescParser.OPEN_GIT_REPO_LOCALLY, 0)

        def repoPath(self):
            return self.getTypedRuleContext(DescParser.RepoPathContext,0)


        def COMMA(self):
            return self.getToken(DescParser.COMMA, 0)

        def repoAliasName(self):
            return self.getTypedRuleContext(DescParser.RepoAliasNameContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_cloneGitToTmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloneGitToTmp" ):
                listener.enterCloneGitToTmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloneGitToTmp" ):
                listener.exitCloneGitToTmp(self)




    def cloneGitToTmp(self):

        localctx = DescParser.CloneGitToTmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cloneGitToTmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(DescParser.OPEN_GIT_REPO_LOCALLY)
            self.state = 204
            self.match(DescParser.T__0)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 206158807040) != 0):
                self.state = 205
                self.repoPath()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 206
                    self.match(DescParser.COMMA)
                    self.state = 207
                    self.repoAliasName()




            self.state = 212
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseGitRepoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE_GIT_REPO(self):
            return self.getToken(DescParser.CLOSE_GIT_REPO, 0)

        def repoAliasName(self):
            return self.getTypedRuleContext(DescParser.RepoAliasNameContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_closeGitRepo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloseGitRepo" ):
                listener.enterCloseGitRepo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloseGitRepo" ):
                listener.exitCloseGitRepo(self)




    def closeGitRepo(self):

        localctx = DescParser.CloseGitRepoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_closeGitRepo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(DescParser.CLOSE_GIT_REPO)
            self.state = 215
            self.match(DescParser.T__0)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0):
                self.state = 216
                self.repoAliasName()


            self.state = 219
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepoPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.PathCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.PathCharsContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.DOT)
            else:
                return self.getToken(DescParser.DOT, i)

        def getRuleIndex(self):
            return DescParser.RULE_repoPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepoPath" ):
                listener.enterRepoPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepoPath" ):
                listener.exitRepoPath(self)




    def repoPath(self):

        localctx = DescParser.RepoPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_repoPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 223
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14, 15, 16, 36, 37]:
                    self.state = 221
                    self.pathChars()
                    pass
                elif token in [18]:
                    self.state = 222
                    self.match(DescParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 225 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158807040) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathForDeployContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.PathCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.PathCharsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_pathForDeploy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathForDeploy" ):
                listener.enterPathForDeploy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathForDeploy" ):
                listener.exitPathForDeploy(self)




    def pathForDeploy(self):

        localctx = DescParser.PathForDeployContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_pathForDeploy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 227
                self.pathChars()
                self.state = 230 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158544896) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.DOT)
            else:
                return self.getToken(DescParser.DOT, i)

        def getRuleIndex(self):
            return DescParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)




    def pattern(self):

        localctx = DescParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 238
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14, 15, 36, 37]:
                    self.state = 232
                    self.namingChars()
                    pass
                elif token in [10]:
                    self.state = 233
                    self.match(DescParser.T__9)
                    pass
                elif token in [11]:
                    self.state = 234
                    self.match(DescParser.T__10)
                    pass
                elif token in [12]:
                    self.state = 235
                    self.match(DescParser.T__11)
                    pass
                elif token in [13]:
                    self.state = 236
                    self.match(DescParser.T__12)
                    pass
                elif token in [18]:
                    self.state = 237
                    self.match(DescParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158756864) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_branchName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranchName" ):
                listener.enterBranchName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranchName" ):
                listener.exitBranchName(self)




    def branchName(self):

        localctx = DescParser.BranchNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_branchName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.namingChars()
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartSystemServiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_SYSTEM_SERVICE(self):
            return self.getToken(DescParser.START_SYSTEM_SERVICE, 0)

        def serviceName(self):
            return self.getTypedRuleContext(DescParser.ServiceNameContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_startSystemService

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartSystemService" ):
                listener.enterStartSystemService(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartSystemService" ):
                listener.exitStartSystemService(self)




    def startSystemService(self):

        localctx = DescParser.StartSystemServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_startSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(DescParser.START_SYSTEM_SERVICE)
            self.state = 248
            self.match(DescParser.T__0)
            self.state = 249
            self.serviceName()
            self.state = 250
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StopSystemServiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOP_SYSTEM_SERVICE(self):
            return self.getToken(DescParser.STOP_SYSTEM_SERVICE, 0)

        def serviceName(self):
            return self.getTypedRuleContext(DescParser.ServiceNameContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_stopSystemService

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStopSystemService" ):
                listener.enterStopSystemService(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStopSystemService" ):
                listener.exitStopSystemService(self)




    def stopSystemService(self):

        localctx = DescParser.StopSystemServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stopSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(DescParser.STOP_SYSTEM_SERVICE)
            self.state = 253
            self.match(DescParser.T__0)
            self.state = 254
            self.serviceName()
            self.state = 255
            self.match(DescParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_serviceName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceName" ):
                listener.enterServiceName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceName" ):
                listener.exitServiceName(self)




    def serviceName(self):

        localctx = DescParser.ServiceNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_serviceName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 257
                self.namingChars()
                self.state = 260 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepoAliasNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


        def getRuleIndex(self):
            return DescParser.RULE_repoAliasName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepoAliasName" ):
                listener.enterRepoAliasName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepoAliasName" ):
                listener.exitRepoAliasName(self)




    def repoAliasName(self):

        localctx = DescParser.RepoAliasNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_repoAliasName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 262
                self.namingChars()
                self.state = 265 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamingCharsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(DescParser.NUM, 0)

        def CHARS(self):
            return self.getToken(DescParser.CHARS, 0)

        def getRuleIndex(self):
            return DescParser.RULE_namingChars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamingChars" ):
                listener.enterNamingChars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamingChars" ):
                listener.exitNamingChars(self)




    def namingChars(self):

        localctx = DescParser.NamingCharsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_namingChars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathCharsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namingChars(self):
            return self.getTypedRuleContext(DescParser.NamingCharsContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_pathChars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathChars" ):
                listener.enterPathChars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathChars" ):
                listener.exitPathChars(self)




    def pathChars(self):

        localctx = DescParser.PathCharsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_pathChars)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.namingChars()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(DescParser.T__15)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





