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
        4,1,24,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,2,3,2,69,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,86,8,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,94,8,3,10,3,12,3,97,9,3,1,4,
        1,4,1,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,5,1,5,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,4,9,124,8,9,11,9,12,9,
        125,1,9,1,9,5,9,130,8,9,10,9,12,9,133,9,9,1,9,4,9,136,8,9,11,9,12,
        9,137,1,10,1,10,1,10,1,10,1,10,3,10,145,8,10,3,10,147,8,10,1,10,
        1,10,1,11,1,11,1,11,3,11,154,8,11,1,11,1,11,1,12,4,12,159,8,12,11,
        12,12,12,160,1,13,1,13,4,13,165,8,13,11,13,12,13,166,1,14,1,14,1,
        14,4,14,172,8,14,11,14,12,14,173,1,15,4,15,177,8,15,11,15,12,15,
        178,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,4,18,190,8,18,11,
        18,12,18,191,1,19,4,19,195,8,19,11,19,12,19,196,1,20,1,20,1,20,0,
        0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,
        1,2,0,14,15,21,22,208,0,42,1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,0,6,89,
        1,0,0,0,8,98,1,0,0,0,10,107,1,0,0,0,12,109,1,0,0,0,14,112,1,0,0,
        0,16,117,1,0,0,0,18,131,1,0,0,0,20,139,1,0,0,0,22,150,1,0,0,0,24,
        158,1,0,0,0,26,164,1,0,0,0,28,171,1,0,0,0,30,176,1,0,0,0,32,180,
        1,0,0,0,34,184,1,0,0,0,36,189,1,0,0,0,38,194,1,0,0,0,40,198,1,0,
        0,0,42,43,3,2,1,0,43,49,5,1,0,0,44,45,3,2,1,0,45,46,5,1,0,0,46,48,
        1,0,0,0,47,44,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,62,3,14,
        7,0,55,62,3,16,8,0,56,62,3,20,10,0,57,62,3,22,11,0,58,62,3,4,2,0,
        59,62,3,32,16,0,60,62,3,34,17,0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,
        1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,
        62,3,1,0,0,0,63,64,5,17,0,0,64,68,5,2,0,0,65,66,3,12,6,0,66,67,5,
        3,0,0,67,69,1,0,0,0,68,65,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,
        85,3,10,5,0,71,72,5,3,0,0,72,86,3,6,3,0,73,74,5,3,0,0,74,86,3,8,
        4,0,75,76,5,3,0,0,76,77,3,8,4,0,77,78,5,3,0,0,78,79,3,6,3,0,79,86,
        1,0,0,0,80,81,5,3,0,0,81,82,3,6,3,0,82,83,5,3,0,0,83,84,3,8,4,0,
        84,86,1,0,0,0,85,71,1,0,0,0,85,73,1,0,0,0,85,75,1,0,0,0,85,80,1,
        0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,4,0,0,88,5,1,0,0,0,89,
        90,5,5,0,0,90,95,3,28,14,0,91,92,5,6,0,0,92,94,3,28,14,0,93,91,1,
        0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,7,1,0,0,0,97,
        95,1,0,0,0,98,99,5,7,0,0,99,104,3,28,14,0,100,101,5,6,0,0,101,103,
        3,28,14,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,9,1,0,0,0,106,104,1,0,0,0,107,108,3,26,13,0,108,11,1,
        0,0,0,109,110,5,8,0,0,110,111,3,26,13,0,111,13,1,0,0,0,112,113,5,
        16,0,0,113,114,5,2,0,0,114,115,3,30,15,0,115,116,5,4,0,0,116,15,
        1,0,0,0,117,118,5,18,0,0,118,119,5,2,0,0,119,120,3,18,9,0,120,121,
        5,4,0,0,121,17,1,0,0,0,122,124,3,40,20,0,123,122,1,0,0,0,124,125,
        1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,128,
        5,9,0,0,128,130,1,0,0,0,129,123,1,0,0,0,130,133,1,0,0,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,134,136,
        3,40,20,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,0,0,137,138,
        1,0,0,0,138,19,1,0,0,0,139,140,5,19,0,0,140,146,5,2,0,0,141,144,
        3,24,12,0,142,143,5,3,0,0,143,145,3,38,19,0,144,142,1,0,0,0,144,
        145,1,0,0,0,145,147,1,0,0,0,146,141,1,0,0,0,146,147,1,0,0,0,147,
        148,1,0,0,0,148,149,5,4,0,0,149,21,1,0,0,0,150,151,5,20,0,0,151,
        153,5,2,0,0,152,154,3,38,19,0,153,152,1,0,0,0,153,154,1,0,0,0,154,
        155,1,0,0,0,155,156,5,4,0,0,156,23,1,0,0,0,157,159,3,40,20,0,158,
        157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,
        25,1,0,0,0,162,165,3,40,20,0,163,165,5,10,0,0,164,162,1,0,0,0,164,
        163,1,0,0,0,165,166,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,
        27,1,0,0,0,168,172,3,40,20,0,169,172,5,11,0,0,170,172,5,9,0,0,171,
        168,1,0,0,0,171,169,1,0,0,0,171,170,1,0,0,0,172,173,1,0,0,0,173,
        171,1,0,0,0,173,174,1,0,0,0,174,29,1,0,0,0,175,177,3,40,20,0,176,
        175,1,0,0,0,177,178,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        31,1,0,0,0,180,181,5,12,0,0,181,182,3,36,18,0,182,183,5,4,0,0,183,
        33,1,0,0,0,184,185,5,13,0,0,185,186,3,36,18,0,186,187,5,4,0,0,187,
        35,1,0,0,0,188,190,3,40,20,0,189,188,1,0,0,0,190,191,1,0,0,0,191,
        189,1,0,0,0,191,192,1,0,0,0,192,37,1,0,0,0,193,195,3,40,20,0,194,
        193,1,0,0,0,195,196,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,
        39,1,0,0,0,198,199,7,0,0,0,199,41,1,0,0,0,20,49,61,68,85,95,104,
        125,131,137,144,146,153,160,164,166,171,173,178,191,196
    ]

class DescParser ( Parser ):

    grammarFileName = "Desc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'exclude='", 
                     "'|'", "'pattern='", "'from='", "'.'", "'/'", "'*'", 
                     "'startSystemService('", "'stopSystemService('", "'-'", 
                     "'_'", "'branch'", "'deployTo'", "'repoHost'", "'openGitRepoLocally'", 
                     "'closeGitRepo'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BRANCH", "DEPLOY_TO", "REPO_HOST", "OPEN_GIT_REPO_LOCALLY", 
                      "CLOSE_GIT_REPO", "NUM", "CHARS", "WS", "LINE_COMMENT" ]

    RULE_script = 0
    RULE_cmd = 1
    RULE_deployTo = 2
    RULE_excludePattern = 3
    RULE_deployPattern = 4
    RULE_pathForDeployTo = 5
    RULE_pathFrom = 6
    RULE_setBranch = 7
    RULE_setRepoSource = 8
    RULE_host = 9
    RULE_cloneGitToTmp = 10
    RULE_closeGitRepo = 11
    RULE_repoPath = 12
    RULE_pathForDeploy = 13
    RULE_pattern = 14
    RULE_branchName = 15
    RULE_startSystemService = 16
    RULE_stopSystemService = 17
    RULE_serviceName = 18
    RULE_repoAliasName = 19
    RULE_namingChars = 20

    ruleNames =  [ "script", "cmd", "deployTo", "excludePattern", "deployPattern", 
                   "pathForDeployTo", "pathFrom", "setBranch", "setRepoSource", 
                   "host", "cloneGitToTmp", "closeGitRepo", "repoPath", 
                   "pathForDeploy", "pattern", "branchName", "startSystemService", 
                   "stopSystemService", "serviceName", "repoAliasName", 
                   "namingChars" ]

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
    BRANCH=16
    DEPLOY_TO=17
    REPO_HOST=18
    OPEN_GIT_REPO_LOCALLY=19
    CLOSE_GIT_REPO=20
    NUM=21
    CHARS=22
    WS=23
    LINE_COMMENT=24

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

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.CmdContext)
            else:
                return self.getTypedRuleContext(DescParser.CmdContext,i)


        def EOF(self):
            return self.getToken(DescParser.EOF, 0)

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
            self.state = 42
            self.cmd()
            self.state = 43
            self.match(DescParser.T__0)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2043904) != 0):
                self.state = 44
                self.cmd()
                self.state = 45
                self.match(DescParser.T__0)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(DescParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def setBranch(self):
            return self.getTypedRuleContext(DescParser.SetBranchContext,0)


        def setRepoSource(self):
            return self.getTypedRuleContext(DescParser.SetRepoSourceContext,0)


        def cloneGitToTmp(self):
            return self.getTypedRuleContext(DescParser.CloneGitToTmpContext,0)


        def closeGitRepo(self):
            return self.getTypedRuleContext(DescParser.CloseGitRepoContext,0)


        def deployTo(self):
            return self.getTypedRuleContext(DescParser.DeployToContext,0)


        def startSystemService(self):
            return self.getTypedRuleContext(DescParser.StartSystemServiceContext,0)


        def stopSystemService(self):
            return self.getTypedRuleContext(DescParser.StopSystemServiceContext,0)


        def getRuleIndex(self):
            return DescParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = DescParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cmd)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.setBranch()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.setRepoSource()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.cloneGitToTmp()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.closeGitRepo()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.deployTo()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.startSystemService()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.stopSystemService()
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
        self.enterRule(localctx, 4, self.RULE_deployTo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(DescParser.DEPLOY_TO)
            self.state = 64
            self.match(DescParser.T__1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 65
                self.pathFrom()
                self.state = 66
                self.match(DescParser.T__2)


            self.state = 70
            self.pathForDeployTo()
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(DescParser.T__2)
                self.state = 72
                self.excludePattern()

            elif la_ == 2:
                self.state = 73
                self.match(DescParser.T__2)
                self.state = 74
                self.deployPattern()

            elif la_ == 3:
                self.state = 75
                self.match(DescParser.T__2)
                self.state = 76
                self.deployPattern()
                self.state = 77
                self.match(DescParser.T__2)
                self.state = 78
                self.excludePattern()

            elif la_ == 4:
                self.state = 80
                self.match(DescParser.T__2)
                self.state = 81
                self.excludePattern()
                self.state = 82
                self.match(DescParser.T__2)
                self.state = 83
                self.deployPattern()


            self.state = 87
            self.match(DescParser.T__3)
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
        self.enterRule(localctx, 6, self.RULE_excludePattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(DescParser.T__4)
            self.state = 90
            self.pattern()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 91
                self.match(DescParser.T__5)
                self.state = 92
                self.pattern()
                self.state = 97
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
        self.enterRule(localctx, 8, self.RULE_deployPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DescParser.T__6)
            self.state = 99
            self.pattern()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 100
                self.match(DescParser.T__5)
                self.state = 101
                self.pattern()
                self.state = 106
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
        self.enterRule(localctx, 10, self.RULE_pathForDeployTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
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
        self.enterRule(localctx, 12, self.RULE_pathFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(DescParser.T__7)
            self.state = 110
            self.pathForDeploy()
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
        self.enterRule(localctx, 14, self.RULE_setBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(DescParser.BRANCH)
            self.state = 113
            self.match(DescParser.T__1)
            self.state = 114
            self.branchName()
            self.state = 115
            self.match(DescParser.T__3)
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
        self.enterRule(localctx, 16, self.RULE_setRepoSource)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(DescParser.REPO_HOST)
            self.state = 118
            self.match(DescParser.T__1)
            self.state = 119
            self.host()
            self.state = 120
            self.match(DescParser.T__3)
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
        self.enterRule(localctx, 18, self.RULE_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 123 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 122
                        self.namingChars()
                        self.state = 125 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
                            break

                    self.state = 127
                    self.match(DescParser.T__8) 
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.namingChars()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
                    break

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
        self.enterRule(localctx, 20, self.RULE_cloneGitToTmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(DescParser.OPEN_GIT_REPO_LOCALLY)
            self.state = 140
            self.match(DescParser.T__1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0):
                self.state = 141
                self.repoPath()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 142
                    self.match(DescParser.T__2)
                    self.state = 143
                    self.repoAliasName()




            self.state = 148
            self.match(DescParser.T__3)
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
        self.enterRule(localctx, 22, self.RULE_closeGitRepo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(DescParser.CLOSE_GIT_REPO)
            self.state = 151
            self.match(DescParser.T__1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0):
                self.state = 152
                self.repoAliasName()


            self.state = 155
            self.match(DescParser.T__3)
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

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


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
        self.enterRule(localctx, 24, self.RULE_repoPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 157
                self.namingChars()
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
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

        def namingChars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DescParser.NamingCharsContext)
            else:
                return self.getTypedRuleContext(DescParser.NamingCharsContext,i)


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
        self.enterRule(localctx, 26, self.RULE_pathForDeploy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 164
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14, 15, 21, 22]:
                    self.state = 162
                    self.namingChars()
                    pass
                elif token in [10]:
                    self.state = 163
                    self.match(DescParser.T__9)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6341632) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14, 15, 21, 22]:
                    self.state = 168
                    self.namingChars()
                    pass
                elif token in [11]:
                    self.state = 169
                    self.match(DescParser.T__10)
                    pass
                elif token in [9]:
                    self.state = 170
                    self.match(DescParser.T__8)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6343168) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_branchName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 175
                self.namingChars()
                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_startSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(DescParser.T__11)
            self.state = 181
            self.serviceName()
            self.state = 182
            self.match(DescParser.T__3)
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
        self.enterRule(localctx, 34, self.RULE_stopSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(DescParser.T__12)
            self.state = 185
            self.serviceName()
            self.state = 186
            self.match(DescParser.T__3)
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
        self.enterRule(localctx, 36, self.RULE_serviceName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.namingChars()
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_repoAliasName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 193
                self.namingChars()
                self.state = 196 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_namingChars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6340608) != 0)):
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





