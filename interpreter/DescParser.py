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
        4,1,39,280,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,3,0,63,8,0,1,0,5,0,66,8,0,10,0,
        12,0,69,9,0,4,0,71,8,0,11,0,12,0,72,1,0,1,0,1,1,1,1,1,1,1,1,5,1,
        81,8,1,10,1,12,1,84,9,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,102,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,5,4,5,115,8,5,11,5,12,5,116,1,5,1,5,5,5,121,8,5,10,
        5,12,5,124,9,5,1,5,4,5,127,8,5,11,5,12,5,128,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,138,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,10,4,10,153,8,10,11,10,12,10,154,1,11,1,11,1,11,1,11,1,11,
        3,11,162,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,179,8,11,1,11,1,11,3,11,183,8,11,1,
        11,1,11,1,12,1,12,1,12,1,12,5,12,191,8,12,10,12,12,12,194,9,12,1,
        13,1,13,1,13,1,13,5,13,200,8,13,10,13,12,13,203,9,13,1,14,1,14,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,215,8,16,3,16,217,8,16,
        1,16,1,16,1,17,1,17,1,17,3,17,224,8,17,1,17,1,17,1,18,1,18,4,18,
        230,8,18,11,18,12,18,231,1,19,4,19,235,8,19,11,19,12,19,236,1,20,
        1,20,1,20,1,20,1,20,1,20,4,20,245,8,20,11,20,12,20,246,1,21,4,21,
        250,8,21,11,21,12,21,251,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,24,4,24,265,8,24,11,24,12,24,266,1,25,4,25,270,8,25,
        11,25,12,25,271,1,26,1,26,1,27,1,27,3,27,278,8,27,1,27,0,0,28,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,0,3,1,0,21,23,2,0,19,20,24,24,2,0,14,15,36,37,288,0,
        70,1,0,0,0,2,76,1,0,0,0,4,101,1,0,0,0,6,103,1,0,0,0,8,108,1,0,0,
        0,10,122,1,0,0,0,12,130,1,0,0,0,14,141,1,0,0,0,16,145,1,0,0,0,18,
        148,1,0,0,0,20,152,1,0,0,0,22,156,1,0,0,0,24,186,1,0,0,0,26,195,
        1,0,0,0,28,204,1,0,0,0,30,206,1,0,0,0,32,209,1,0,0,0,34,220,1,0,
        0,0,36,229,1,0,0,0,38,234,1,0,0,0,40,244,1,0,0,0,42,249,1,0,0,0,
        44,253,1,0,0,0,46,258,1,0,0,0,48,264,1,0,0,0,50,269,1,0,0,0,52,273,
        1,0,0,0,54,277,1,0,0,0,56,57,3,6,3,0,57,58,5,27,0,0,58,62,1,0,0,
        0,59,60,3,8,4,0,60,61,5,27,0,0,61,63,1,0,0,0,62,59,1,0,0,0,62,63,
        1,0,0,0,63,67,1,0,0,0,64,66,3,2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,
        67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,70,56,1,
        0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,
        75,5,0,0,1,75,1,1,0,0,0,76,77,3,32,16,0,77,78,5,27,0,0,78,82,1,0,
        0,0,79,81,3,4,2,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,
        1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,3,34,17,0,86,87,5,27,0,
        0,87,3,1,0,0,0,88,89,3,22,11,0,89,90,5,27,0,0,90,102,1,0,0,0,91,
        92,3,44,22,0,92,93,5,27,0,0,93,102,1,0,0,0,94,95,3,46,23,0,95,96,
        5,27,0,0,96,102,1,0,0,0,97,98,3,12,6,0,98,99,5,27,0,0,99,102,1,0,
        0,0,100,102,3,2,1,0,101,88,1,0,0,0,101,91,1,0,0,0,101,94,1,0,0,0,
        101,97,1,0,0,0,101,100,1,0,0,0,102,5,1,0,0,0,103,104,5,31,0,0,104,
        105,5,1,0,0,105,106,3,42,21,0,106,107,5,2,0,0,107,7,1,0,0,0,108,
        109,5,33,0,0,109,110,5,1,0,0,110,111,3,10,5,0,111,112,5,2,0,0,112,
        9,1,0,0,0,113,115,3,52,26,0,114,113,1,0,0,0,115,116,1,0,0,0,116,
        114,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,18,0,0,119,
        121,1,0,0,0,120,114,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,125,127,3,52,26,0,126,
        125,1,0,0,0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,
        11,1,0,0,0,130,131,5,28,0,0,131,132,5,1,0,0,132,133,3,14,7,0,133,
        134,5,26,0,0,134,137,3,16,8,0,135,136,5,26,0,0,136,138,3,18,9,0,
        137,135,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,5,2,0,0,
        140,13,1,0,0,0,141,142,5,25,0,0,142,143,5,3,0,0,143,144,7,0,0,0,
        144,15,1,0,0,0,145,146,5,4,0,0,146,147,7,1,0,0,147,17,1,0,0,0,148,
        149,5,5,0,0,149,150,3,20,10,0,150,19,1,0,0,0,151,153,3,54,27,0,152,
        151,1,0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,
        21,1,0,0,0,156,157,5,32,0,0,157,161,5,1,0,0,158,159,3,30,15,0,159,
        160,5,26,0,0,160,162,1,0,0,0,161,158,1,0,0,0,161,162,1,0,0,0,162,
        163,1,0,0,0,163,178,3,28,14,0,164,165,5,26,0,0,165,179,3,24,12,0,
        166,167,5,26,0,0,167,179,3,26,13,0,168,169,5,26,0,0,169,170,3,26,
        13,0,170,171,5,26,0,0,171,172,3,24,12,0,172,179,1,0,0,0,173,174,
        5,26,0,0,174,175,3,24,12,0,175,176,5,26,0,0,176,177,3,26,13,0,177,
        179,1,0,0,0,178,164,1,0,0,0,178,166,1,0,0,0,178,168,1,0,0,0,178,
        173,1,0,0,0,178,179,1,0,0,0,179,182,1,0,0,0,180,181,5,26,0,0,181,
        183,5,17,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,
        185,5,2,0,0,185,23,1,0,0,0,186,187,5,6,0,0,187,192,3,40,20,0,188,
        189,5,7,0,0,189,191,3,40,20,0,190,188,1,0,0,0,191,194,1,0,0,0,192,
        190,1,0,0,0,192,193,1,0,0,0,193,25,1,0,0,0,194,192,1,0,0,0,195,196,
        5,8,0,0,196,201,3,40,20,0,197,198,5,7,0,0,198,200,3,40,20,0,199,
        197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,
        27,1,0,0,0,203,201,1,0,0,0,204,205,3,38,19,0,205,29,1,0,0,0,206,
        207,5,9,0,0,207,208,3,38,19,0,208,31,1,0,0,0,209,210,5,34,0,0,210,
        216,5,1,0,0,211,214,3,36,18,0,212,213,5,26,0,0,213,215,3,50,25,0,
        214,212,1,0,0,0,214,215,1,0,0,0,215,217,1,0,0,0,216,211,1,0,0,0,
        216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,2,0,0,219,33,1,0,0,0,220,
        221,5,35,0,0,221,223,5,1,0,0,222,224,3,50,25,0,223,222,1,0,0,0,223,
        224,1,0,0,0,224,225,1,0,0,0,225,226,5,2,0,0,226,35,1,0,0,0,227,230,
        3,54,27,0,228,230,5,18,0,0,229,227,1,0,0,0,229,228,1,0,0,0,230,231,
        1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,37,1,0,0,0,233,235,3,
        54,27,0,234,233,1,0,0,0,235,236,1,0,0,0,236,234,1,0,0,0,236,237,
        1,0,0,0,237,39,1,0,0,0,238,245,3,52,26,0,239,245,5,10,0,0,240,245,
        5,11,0,0,241,245,5,12,0,0,242,245,5,13,0,0,243,245,5,18,0,0,244,
        238,1,0,0,0,244,239,1,0,0,0,244,240,1,0,0,0,244,241,1,0,0,0,244,
        242,1,0,0,0,244,243,1,0,0,0,245,246,1,0,0,0,246,244,1,0,0,0,246,
        247,1,0,0,0,247,41,1,0,0,0,248,250,3,52,26,0,249,248,1,0,0,0,250,
        251,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,43,1,0,0,0,253,254,
        5,29,0,0,254,255,5,1,0,0,255,256,3,48,24,0,256,257,5,2,0,0,257,45,
        1,0,0,0,258,259,5,30,0,0,259,260,5,1,0,0,260,261,3,48,24,0,261,262,
        5,2,0,0,262,47,1,0,0,0,263,265,3,52,26,0,264,263,1,0,0,0,265,266,
        1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,49,1,0,0,0,268,270,3,
        52,26,0,269,268,1,0,0,0,270,271,1,0,0,0,271,269,1,0,0,0,271,272,
        1,0,0,0,272,51,1,0,0,0,273,274,7,2,0,0,274,53,1,0,0,0,275,278,3,
        52,26,0,276,278,5,16,0,0,277,275,1,0,0,0,277,276,1,0,0,0,278,55,
        1,0,0,0,27,62,67,72,82,101,116,122,128,137,154,161,178,182,192,201,
        214,216,223,229,231,236,244,246,251,266,271,277
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

        def setBranch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.SetBranchContext)
            else:
                return self.getTypedRuleContext(DescParser.SetBranchContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(DescParser.SEMICOLON)
            else:
                return self.getToken(DescParser.SEMICOLON, i)

        def setRepoSource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.SetRepoSourceContext)
            else:
                return self.getTypedRuleContext(DescParser.SetRepoSourceContext,i)


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
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.setBranch()
                self.state = 57
                self.match(DescParser.SEMICOLON)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 59
                    self.setRepoSource()
                    self.state = 60
                    self.match(DescParser.SEMICOLON)


                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 64
                    self.gitRepoScope()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 74
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
            self.state = 76
            self.cloneGitToTmp()
            self.state = 77
            self.match(DescParser.SEMICOLON)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 23353884672) != 0):
                self.state = 79
                self.scopeCmds()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.closeGitRepo()
            self.state = 86
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
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.deployTo()
                self.state = 89
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.startSystemService()
                self.state = 92
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.stopSystemService()
                self.state = 95
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.buildProject()
                self.state = 98
                self.match(DescParser.SEMICOLON)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
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
            self.state = 103
            self.match(DescParser.BRANCH)
            self.state = 104
            self.match(DescParser.T__0)
            self.state = 105
            self.branchName()
            self.state = 106
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
            self.state = 108
            self.match(DescParser.REPO_HOST)
            self.state = 109
            self.match(DescParser.T__0)
            self.state = 110
            self.host()
            self.state = 111
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
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 113
                        self.namingChars()
                        self.state = 116 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0)):
                            break

                    self.state = 118
                    self.match(DescParser.DOT) 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.namingChars()
                self.state = 128 
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
            self.state = 130
            self.match(DescParser.BUILD_PROJECT)
            self.state = 131
            self.match(DescParser.T__0)
            self.state = 132
            self.projectLanguage()
            self.state = 133
            self.match(DescParser.COMMA)
            self.state = 134
            self.builderType()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 135
                self.match(DescParser.COMMA)
                self.state = 136
                self.buildDir()


            self.state = 139
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
            self.state = 141
            self.match(DescParser.LANGUAGE)
            self.state = 142
            self.match(DescParser.T__2)
            self.state = 143
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
            self.state = 145
            self.match(DescParser.T__3)
            self.state = 146
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
            self.state = 148
            self.match(DescParser.T__4)
            self.state = 149
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
            self.state = 152 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 151
                self.pathChars()
                self.state = 154 
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
            self.state = 156
            self.match(DescParser.DEPLOY_TO)
            self.state = 157
            self.match(DescParser.T__0)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 158
                self.pathFrom()
                self.state = 159
                self.match(DescParser.COMMA)


            self.state = 163
            self.pathForDeployTo()
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(DescParser.COMMA)
                self.state = 165
                self.excludePattern()

            elif la_ == 2:
                self.state = 166
                self.match(DescParser.COMMA)
                self.state = 167
                self.deployPattern()

            elif la_ == 3:
                self.state = 168
                self.match(DescParser.COMMA)
                self.state = 169
                self.deployPattern()
                self.state = 170
                self.match(DescParser.COMMA)
                self.state = 171
                self.excludePattern()

            elif la_ == 4:
                self.state = 173
                self.match(DescParser.COMMA)
                self.state = 174
                self.excludePattern()
                self.state = 175
                self.match(DescParser.COMMA)
                self.state = 176
                self.deployPattern()


            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 180
                self.match(DescParser.COMMA)
                self.state = 181
                self.match(DescParser.MERGE)


            self.state = 184
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
            self.state = 186
            self.match(DescParser.T__5)
            self.state = 187
            self.pattern()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 188
                self.match(DescParser.T__6)
                self.state = 189
                self.pattern()
                self.state = 194
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
            self.state = 195
            self.match(DescParser.T__7)
            self.state = 196
            self.pattern()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 197
                self.match(DescParser.T__6)
                self.state = 198
                self.pattern()
                self.state = 203
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
            self.state = 204
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
            self.state = 206
            self.match(DescParser.T__8)
            self.state = 207
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
            self.state = 209
            self.match(DescParser.OPEN_GIT_REPO_LOCALLY)
            self.state = 210
            self.match(DescParser.T__0)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 206158807040) != 0):
                self.state = 211
                self.repoPath()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 212
                    self.match(DescParser.COMMA)
                    self.state = 213
                    self.repoAliasName()




            self.state = 218
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
            self.state = 220
            self.match(DescParser.CLOSE_GIT_REPO)
            self.state = 221
            self.match(DescParser.T__0)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 206158479360) != 0):
                self.state = 222
                self.repoAliasName()


            self.state = 225
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
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14, 15, 16, 36, 37]:
                    self.state = 227
                    self.pathChars()
                    pass
                elif token in [18]:
                    self.state = 228
                    self.match(DescParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 231 
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
            self.state = 234 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 233
                self.pathChars()
                self.state = 236 
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
            self.state = 244 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 244
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14, 15, 36, 37]:
                    self.state = 238
                    self.namingChars()
                    pass
                elif token in [10]:
                    self.state = 239
                    self.match(DescParser.T__9)
                    pass
                elif token in [11]:
                    self.state = 240
                    self.match(DescParser.T__10)
                    pass
                elif token in [12]:
                    self.state = 241
                    self.match(DescParser.T__11)
                    pass
                elif token in [13]:
                    self.state = 242
                    self.match(DescParser.T__12)
                    pass
                elif token in [18]:
                    self.state = 243
                    self.match(DescParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 246 
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
            self.state = 249 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 248
                self.namingChars()
                self.state = 251 
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
            self.state = 253
            self.match(DescParser.START_SYSTEM_SERVICE)
            self.state = 254
            self.match(DescParser.T__0)
            self.state = 255
            self.serviceName()
            self.state = 256
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
            self.state = 258
            self.match(DescParser.STOP_SYSTEM_SERVICE)
            self.state = 259
            self.match(DescParser.T__0)
            self.state = 260
            self.serviceName()
            self.state = 261
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
            self.state = 264 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 263
                self.namingChars()
                self.state = 266 
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
            self.state = 269 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 268
                self.namingChars()
                self.state = 271 
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
            self.state = 273
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
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.namingChars()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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





