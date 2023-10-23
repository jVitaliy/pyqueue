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
        4,1,36,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,94,8,2,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,4,5,107,8,5,11,5,12,5,108,1,5,
        1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,5,4,5,119,8,5,11,5,12,5,120,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,130,8,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,9,1,9,4,9,143,8,9,11,9,12,9,144,1,10,1,10,1,10,1,10,
        1,10,3,10,152,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,169,8,10,1,10,1,10,3,10,173,8,
        10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,181,8,11,10,11,12,11,184,9,
        11,1,12,1,12,1,12,1,12,5,12,190,8,12,10,12,12,12,193,9,12,1,13,1,
        13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,205,8,15,3,15,207,
        8,15,1,15,1,15,1,16,1,16,1,16,3,16,214,8,16,1,16,1,16,1,17,1,17,
        4,17,220,8,17,11,17,12,17,221,1,18,4,18,225,8,18,11,18,12,18,226,
        1,19,1,19,1,19,4,19,232,8,19,11,19,12,19,233,1,20,4,20,237,8,20,
        11,20,12,20,238,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,23,4,23,252,8,23,11,23,12,23,253,1,24,4,24,257,8,24,11,24,12,24,
        258,1,25,1,25,1,26,1,26,3,26,265,8,26,1,26,0,0,27,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,3,
        1,0,18,20,2,0,16,17,21,21,2,0,11,12,33,34,271,0,54,1,0,0,0,2,68,
        1,0,0,0,4,93,1,0,0,0,6,95,1,0,0,0,8,100,1,0,0,0,10,114,1,0,0,0,12,
        122,1,0,0,0,14,133,1,0,0,0,16,137,1,0,0,0,18,140,1,0,0,0,20,146,
        1,0,0,0,22,176,1,0,0,0,24,185,1,0,0,0,26,194,1,0,0,0,28,196,1,0,
        0,0,30,199,1,0,0,0,32,210,1,0,0,0,34,219,1,0,0,0,36,224,1,0,0,0,
        38,231,1,0,0,0,40,236,1,0,0,0,42,240,1,0,0,0,44,245,1,0,0,0,46,251,
        1,0,0,0,48,256,1,0,0,0,50,260,1,0,0,0,52,264,1,0,0,0,54,55,3,6,3,
        0,55,56,5,24,0,0,56,57,1,0,0,0,57,58,3,8,4,0,58,59,5,24,0,0,59,63,
        1,0,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,
        63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,
        0,0,68,69,3,30,15,0,69,70,5,24,0,0,70,74,1,0,0,0,71,73,3,4,2,0,72,
        71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,
        0,76,74,1,0,0,0,77,78,3,32,16,0,78,79,5,24,0,0,79,3,1,0,0,0,80,81,
        3,20,10,0,81,82,5,24,0,0,82,94,1,0,0,0,83,84,3,42,21,0,84,85,5,24,
        0,0,85,94,1,0,0,0,86,87,3,44,22,0,87,88,5,24,0,0,88,94,1,0,0,0,89,
        90,3,12,6,0,90,91,5,24,0,0,91,94,1,0,0,0,92,94,3,2,1,0,93,80,1,0,
        0,0,93,83,1,0,0,0,93,86,1,0,0,0,93,89,1,0,0,0,93,92,1,0,0,0,94,5,
        1,0,0,0,95,96,5,28,0,0,96,97,5,1,0,0,97,98,3,40,20,0,98,99,5,2,0,
        0,99,7,1,0,0,0,100,101,5,30,0,0,101,102,5,1,0,0,102,103,3,10,5,0,
        103,104,5,2,0,0,104,9,1,0,0,0,105,107,3,50,25,0,106,105,1,0,0,0,
        107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,
        110,111,5,15,0,0,111,113,1,0,0,0,112,106,1,0,0,0,113,116,1,0,0,0,
        114,112,1,0,0,0,114,115,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,
        117,119,3,50,25,0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,
        0,120,121,1,0,0,0,121,11,1,0,0,0,122,123,5,25,0,0,123,124,5,1,0,
        0,124,125,3,14,7,0,125,126,5,23,0,0,126,129,3,16,8,0,127,128,5,23,
        0,0,128,130,3,18,9,0,129,127,1,0,0,0,129,130,1,0,0,0,130,131,1,0,
        0,0,131,132,5,2,0,0,132,13,1,0,0,0,133,134,5,22,0,0,134,135,5,3,
        0,0,135,136,7,0,0,0,136,15,1,0,0,0,137,138,5,4,0,0,138,139,7,1,0,
        0,139,17,1,0,0,0,140,142,5,5,0,0,141,143,3,52,26,0,142,141,1,0,0,
        0,143,144,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,19,1,0,0,0,
        146,147,5,29,0,0,147,151,5,1,0,0,148,149,3,28,14,0,149,150,5,23,
        0,0,150,152,1,0,0,0,151,148,1,0,0,0,151,152,1,0,0,0,152,153,1,0,
        0,0,153,168,3,26,13,0,154,155,5,23,0,0,155,169,3,22,11,0,156,157,
        5,23,0,0,157,169,3,24,12,0,158,159,5,23,0,0,159,160,3,24,12,0,160,
        161,5,23,0,0,161,162,3,22,11,0,162,169,1,0,0,0,163,164,5,23,0,0,
        164,165,3,22,11,0,165,166,5,23,0,0,166,167,3,24,12,0,167,169,1,0,
        0,0,168,154,1,0,0,0,168,156,1,0,0,0,168,158,1,0,0,0,168,163,1,0,
        0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,171,5,23,0,0,171,173,5,14,
        0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,5,2,
        0,0,175,21,1,0,0,0,176,177,5,6,0,0,177,182,3,38,19,0,178,179,5,7,
        0,0,179,181,3,38,19,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,1,
        0,0,0,182,183,1,0,0,0,183,23,1,0,0,0,184,182,1,0,0,0,185,186,5,8,
        0,0,186,191,3,38,19,0,187,188,5,7,0,0,188,190,3,38,19,0,189,187,
        1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,25,1,
        0,0,0,193,191,1,0,0,0,194,195,3,36,18,0,195,27,1,0,0,0,196,197,5,
        9,0,0,197,198,3,36,18,0,198,29,1,0,0,0,199,200,5,31,0,0,200,206,
        5,1,0,0,201,204,3,34,17,0,202,203,5,23,0,0,203,205,3,48,24,0,204,
        202,1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,201,1,0,0,0,206,
        207,1,0,0,0,207,208,1,0,0,0,208,209,5,2,0,0,209,31,1,0,0,0,210,211,
        5,32,0,0,211,213,5,1,0,0,212,214,3,48,24,0,213,212,1,0,0,0,213,214,
        1,0,0,0,214,215,1,0,0,0,215,216,5,2,0,0,216,33,1,0,0,0,217,220,3,
        52,26,0,218,220,5,15,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,221,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,35,1,0,0,0,223,225,3,
        52,26,0,224,223,1,0,0,0,225,226,1,0,0,0,226,224,1,0,0,0,226,227,
        1,0,0,0,227,37,1,0,0,0,228,232,3,50,25,0,229,232,5,10,0,0,230,232,
        5,15,0,0,231,228,1,0,0,0,231,229,1,0,0,0,231,230,1,0,0,0,232,233,
        1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,39,1,0,0,0,235,237,3,
        50,25,0,236,235,1,0,0,0,237,238,1,0,0,0,238,236,1,0,0,0,238,239,
        1,0,0,0,239,41,1,0,0,0,240,241,5,26,0,0,241,242,5,1,0,0,242,243,
        3,46,23,0,243,244,5,2,0,0,244,43,1,0,0,0,245,246,5,27,0,0,246,247,
        5,1,0,0,247,248,3,46,23,0,248,249,5,2,0,0,249,45,1,0,0,0,250,252,
        3,50,25,0,251,250,1,0,0,0,252,253,1,0,0,0,253,251,1,0,0,0,253,254,
        1,0,0,0,254,47,1,0,0,0,255,257,3,50,25,0,256,255,1,0,0,0,257,258,
        1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,49,1,0,0,0,260,261,7,
        2,0,0,261,51,1,0,0,0,262,265,3,50,25,0,263,265,5,13,0,0,264,262,
        1,0,0,0,264,263,1,0,0,0,265,53,1,0,0,0,25,63,74,93,108,114,120,129,
        144,151,168,172,182,191,204,206,213,219,221,226,231,233,238,253,
        258,264
    ]

class DescParser ( Parser ):

    grammarFileName = "Desc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'type='", "'dir='", 
                     "'exclude='", "'|'", "'pattern='", "'from='", "'*'", 
                     "'-'", "'_'", "'/'", "'merge'", "'.'", "'gradle'", 
                     "'maven'", "'java17'", "'next'", "'python39'", "'npm'", 
                     "'language'", "','", "';'", "'buildProject'", "'startSystemService'", 
                     "'stopSystemService'", "'branch'", "'deployTo'", "'repoHost'", 
                     "'openGitRepoLocally'", "'closeGitRepo'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MERGE", "DOT", "GRADLE", 
                      "MAVEN", "JAVA17", "NEXT", "PYTHON39", "NPM", "LANGUAGE", 
                      "COMMA", "SEMICOLON", "BUILD_PROJECT", "START_SYSTEM_SERVICE", 
                      "STOP_SYSTEM_SERVICE", "BRANCH", "DEPLOY_TO", "REPO_HOST", 
                      "OPEN_GIT_REPO_LOCALLY", "CLOSE_GIT_REPO", "NUM", 
                      "CHARS", "WS", "LINE_COMMENT" ]

    RULE_script = 0
    RULE_gitRepoScope = 1
    RULE_scopeCmds = 2
    RULE_setBranch = 3
    RULE_setRepoSource = 4
    RULE_host = 5
    RULE_buildProject = 6
    RULE_projectLanguage = 7
    RULE_builderType = 8
    RULE_buildFolder = 9
    RULE_deployTo = 10
    RULE_excludePattern = 11
    RULE_deployPattern = 12
    RULE_pathForDeployTo = 13
    RULE_pathFrom = 14
    RULE_cloneGitToTmp = 15
    RULE_closeGitRepo = 16
    RULE_repoPath = 17
    RULE_pathForDeploy = 18
    RULE_pattern = 19
    RULE_branchName = 20
    RULE_startSystemService = 21
    RULE_stopSystemService = 22
    RULE_serviceName = 23
    RULE_repoAliasName = 24
    RULE_namingChars = 25
    RULE_pathChars = 26

    ruleNames =  [ "script", "gitRepoScope", "scopeCmds", "setBranch", "setRepoSource", 
                   "host", "buildProject", "projectLanguage", "builderType", 
                   "buildFolder", "deployTo", "excludePattern", "deployPattern", 
                   "pathForDeployTo", "pathFrom", "cloneGitToTmp", "closeGitRepo", 
                   "repoPath", "pathForDeploy", "pattern", "branchName", 
                   "startSystemService", "stopSystemService", "serviceName", 
                   "repoAliasName", "namingChars", "pathChars" ]

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
    MERGE=14
    DOT=15
    GRADLE=16
    MAVEN=17
    JAVA17=18
    NEXT=19
    PYTHON39=20
    NPM=21
    LANGUAGE=22
    COMMA=23
    SEMICOLON=24
    BUILD_PROJECT=25
    START_SYSTEM_SERVICE=26
    STOP_SYSTEM_SERVICE=27
    BRANCH=28
    DEPLOY_TO=29
    REPO_HOST=30
    OPEN_GIT_REPO_LOCALLY=31
    CLOSE_GIT_REPO=32
    NUM=33
    CHARS=34
    WS=35
    LINE_COMMENT=36

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
            self.state = 54
            self.setBranch()
            self.state = 55
            self.match(DescParser.SEMICOLON)

            self.state = 57
            self.setRepoSource()
            self.state = 58
            self.match(DescParser.SEMICOLON)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 60
                self.gitRepoScope()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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
            self.state = 68
            self.cloneGitToTmp()
            self.state = 69
            self.match(DescParser.SEMICOLON)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2919235584) != 0):
                self.state = 71
                self.scopeCmds()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.closeGitRepo()
            self.state = 78
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
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.deployTo()
                self.state = 81
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.startSystemService()
                self.state = 84
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.stopSystemService()
                self.state = 87
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.buildProject()
                self.state = 90
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
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
            self.state = 95
            self.match(DescParser.BRANCH)
            self.state = 96
            self.match(DescParser.T__0)
            self.state = 97
            self.branchName()
            self.state = 98
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
            self.state = 100
            self.match(DescParser.REPO_HOST)
            self.state = 101
            self.match(DescParser.T__0)
            self.state = 102
            self.host()
            self.state = 103
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
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 106 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 105
                        self.namingChars()
                        self.state = 108 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0)):
                            break

                    self.state = 110
                    self.match(DescParser.DOT) 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.namingChars()
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0)):
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


        def buildFolder(self):
            return self.getTypedRuleContext(DescParser.BuildFolderContext,0)


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
            self.state = 122
            self.match(DescParser.BUILD_PROJECT)
            self.state = 123
            self.match(DescParser.T__0)
            self.state = 124
            self.projectLanguage()
            self.state = 125
            self.match(DescParser.COMMA)
            self.state = 126
            self.builderType()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 127
                self.match(DescParser.COMMA)
                self.state = 128
                self.buildFolder()


            self.state = 131
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
            self.state = 133
            self.match(DescParser.LANGUAGE)
            self.state = 134
            self.match(DescParser.T__2)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
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
            self.state = 137
            self.match(DescParser.T__3)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2293760) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_buildFolder)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(DescParser.T__4)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 141
                self.pathChars()
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769818112) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_deployTo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(DescParser.DEPLOY_TO)
            self.state = 147
            self.match(DescParser.T__0)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 148
                self.pathFrom()
                self.state = 149
                self.match(DescParser.COMMA)


            self.state = 153
            self.pathForDeployTo()
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 154
                self.match(DescParser.COMMA)
                self.state = 155
                self.excludePattern()

            elif la_ == 2:
                self.state = 156
                self.match(DescParser.COMMA)
                self.state = 157
                self.deployPattern()

            elif la_ == 3:
                self.state = 158
                self.match(DescParser.COMMA)
                self.state = 159
                self.deployPattern()
                self.state = 160
                self.match(DescParser.COMMA)
                self.state = 161
                self.excludePattern()

            elif la_ == 4:
                self.state = 163
                self.match(DescParser.COMMA)
                self.state = 164
                self.excludePattern()
                self.state = 165
                self.match(DescParser.COMMA)
                self.state = 166
                self.deployPattern()


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 170
                self.match(DescParser.COMMA)
                self.state = 171
                self.match(DescParser.MERGE)


            self.state = 174
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
        self.enterRule(localctx, 22, self.RULE_excludePattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(DescParser.T__5)
            self.state = 177
            self.pattern()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 178
                self.match(DescParser.T__6)
                self.state = 179
                self.pattern()
                self.state = 184
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
        self.enterRule(localctx, 24, self.RULE_deployPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(DescParser.T__7)
            self.state = 186
            self.pattern()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 187
                self.match(DescParser.T__6)
                self.state = 188
                self.pattern()
                self.state = 193
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
        self.enterRule(localctx, 26, self.RULE_pathForDeployTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 28, self.RULE_pathFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(DescParser.T__8)
            self.state = 197
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
        self.enterRule(localctx, 30, self.RULE_cloneGitToTmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(DescParser.OPEN_GIT_REPO_LOCALLY)
            self.state = 200
            self.match(DescParser.T__0)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 25769850880) != 0):
                self.state = 201
                self.repoPath()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 202
                    self.match(DescParser.COMMA)
                    self.state = 203
                    self.repoAliasName()




            self.state = 208
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
        self.enterRule(localctx, 32, self.RULE_closeGitRepo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(DescParser.CLOSE_GIT_REPO)
            self.state = 211
            self.match(DescParser.T__0)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0):
                self.state = 212
                self.repoAliasName()


            self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_repoPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 219
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13, 33, 34]:
                    self.state = 217
                    self.pathChars()
                    pass
                elif token in [15]:
                    self.state = 218
                    self.match(DescParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769850880) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_pathForDeploy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 223
                self.pathChars()
                self.state = 226 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769818112) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 231
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 33, 34]:
                    self.state = 228
                    self.namingChars()
                    pass
                elif token in [10]:
                    self.state = 229
                    self.match(DescParser.T__9)
                    pass
                elif token in [15]:
                    self.state = 230
                    self.match(DescParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 233 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769843712) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_branchName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 235
                self.namingChars()
                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0)):
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
        self.enterRule(localctx, 42, self.RULE_startSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(DescParser.START_SYSTEM_SERVICE)
            self.state = 241
            self.match(DescParser.T__0)
            self.state = 242
            self.serviceName()
            self.state = 243
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
        self.enterRule(localctx, 44, self.RULE_stopSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(DescParser.STOP_SYSTEM_SERVICE)
            self.state = 246
            self.match(DescParser.T__0)
            self.state = 247
            self.serviceName()
            self.state = 248
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
        self.enterRule(localctx, 46, self.RULE_serviceName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 250
                self.namingChars()
                self.state = 253 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0)):
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
        self.enterRule(localctx, 48, self.RULE_repoAliasName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 255
                self.namingChars()
                self.state = 258 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0)):
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
        self.enterRule(localctx, 50, self.RULE_namingChars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25769809920) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_pathChars)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.namingChars()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(DescParser.T__12)
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





