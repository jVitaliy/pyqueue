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
        4,1,22,180,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,5,0,
        42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,
        2,1,2,1,2,1,2,1,2,3,2,61,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,86,
        8,3,10,3,12,3,89,9,3,1,4,1,4,1,4,1,4,5,4,95,8,4,10,4,12,4,98,9,4,
        1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,
        4,9,116,8,9,11,9,12,9,117,1,9,1,9,5,9,122,8,9,10,9,12,9,125,9,9,
        1,9,4,9,128,8,9,11,9,12,9,129,1,10,1,10,1,10,1,10,1,10,3,10,137,
        8,10,3,10,139,8,10,1,10,1,10,1,11,1,11,1,11,3,11,146,8,11,1,11,1,
        11,1,12,4,12,151,8,12,11,12,12,12,152,1,13,1,13,4,13,157,8,13,11,
        13,12,13,158,1,14,1,14,1,14,4,14,164,8,14,11,14,12,14,165,1,15,4,
        15,169,8,15,11,15,12,15,170,1,16,4,16,174,8,16,11,16,12,16,175,1,
        17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,0,1,2,0,12,13,19,20,187,0,36,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,
        0,6,81,1,0,0,0,8,90,1,0,0,0,10,99,1,0,0,0,12,101,1,0,0,0,14,104,
        1,0,0,0,16,109,1,0,0,0,18,123,1,0,0,0,20,131,1,0,0,0,22,142,1,0,
        0,0,24,150,1,0,0,0,26,156,1,0,0,0,28,163,1,0,0,0,30,168,1,0,0,0,
        32,173,1,0,0,0,34,177,1,0,0,0,36,37,3,2,1,0,37,43,5,1,0,0,38,39,
        3,2,1,0,39,40,5,1,0,0,40,42,1,0,0,0,41,38,1,0,0,0,42,45,1,0,0,0,
        43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,
        0,0,1,47,1,1,0,0,0,48,54,3,14,7,0,49,54,3,16,8,0,50,54,3,20,10,0,
        51,54,3,22,11,0,52,54,3,4,2,0,53,48,1,0,0,0,53,49,1,0,0,0,53,50,
        1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,0,55,56,5,15,0,0,
        56,60,5,2,0,0,57,58,3,12,6,0,58,59,5,3,0,0,59,61,1,0,0,0,60,57,1,
        0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,77,3,10,5,0,63,64,5,3,0,0,64,
        78,3,6,3,0,65,66,5,3,0,0,66,78,3,8,4,0,67,68,5,3,0,0,68,69,3,8,4,
        0,69,70,5,3,0,0,70,71,3,6,3,0,71,78,1,0,0,0,72,73,5,3,0,0,73,74,
        3,6,3,0,74,75,5,3,0,0,75,76,3,8,4,0,76,78,1,0,0,0,77,63,1,0,0,0,
        77,65,1,0,0,0,77,67,1,0,0,0,77,72,1,0,0,0,77,78,1,0,0,0,78,79,1,
        0,0,0,79,80,5,4,0,0,80,5,1,0,0,0,81,82,5,5,0,0,82,87,3,28,14,0,83,
        84,5,6,0,0,84,86,3,28,14,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,
        0,0,87,88,1,0,0,0,88,7,1,0,0,0,89,87,1,0,0,0,90,91,5,7,0,0,91,96,
        3,28,14,0,92,93,5,6,0,0,93,95,3,28,14,0,94,92,1,0,0,0,95,98,1,0,
        0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,96,1,0,0,0,99,100,
        3,26,13,0,100,11,1,0,0,0,101,102,5,8,0,0,102,103,3,26,13,0,103,13,
        1,0,0,0,104,105,5,14,0,0,105,106,5,2,0,0,106,107,3,30,15,0,107,108,
        5,4,0,0,108,15,1,0,0,0,109,110,5,16,0,0,110,111,5,2,0,0,111,112,
        3,18,9,0,112,113,5,4,0,0,113,17,1,0,0,0,114,116,3,34,17,0,115,114,
        1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,119,
        1,0,0,0,119,120,5,9,0,0,120,122,1,0,0,0,121,115,1,0,0,0,122,125,
        1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,127,1,0,0,0,125,123,
        1,0,0,0,126,128,3,34,17,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,
        1,0,0,0,129,130,1,0,0,0,130,19,1,0,0,0,131,132,5,17,0,0,132,138,
        5,2,0,0,133,136,3,24,12,0,134,135,5,3,0,0,135,137,3,32,16,0,136,
        134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,133,1,0,0,0,138,
        139,1,0,0,0,139,140,1,0,0,0,140,141,5,4,0,0,141,21,1,0,0,0,142,143,
        5,18,0,0,143,145,5,2,0,0,144,146,3,32,16,0,145,144,1,0,0,0,145,146,
        1,0,0,0,146,147,1,0,0,0,147,148,5,4,0,0,148,23,1,0,0,0,149,151,3,
        34,17,0,150,149,1,0,0,0,151,152,1,0,0,0,152,150,1,0,0,0,152,153,
        1,0,0,0,153,25,1,0,0,0,154,157,3,34,17,0,155,157,5,10,0,0,156,154,
        1,0,0,0,156,155,1,0,0,0,157,158,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,27,1,0,0,0,160,164,3,34,17,0,161,164,5,11,0,0,162,164,
        5,9,0,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,0,0,164,165,
        1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,29,1,0,0,0,167,169,3,
        34,17,0,168,167,1,0,0,0,169,170,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,31,1,0,0,0,172,174,3,34,17,0,173,172,1,0,0,0,174,175,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,33,1,0,0,0,177,178,7,
        0,0,0,178,35,1,0,0,0,19,43,53,60,77,87,96,117,123,129,136,138,145,
        152,156,158,163,165,170,175
    ]

class DescParser ( Parser ):

    grammarFileName = "Desc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'exclude='", 
                     "'|'", "'pattern='", "'from='", "'.'", "'/'", "'*'", 
                     "'-'", "'_'", "'branch'", "'deployTo'", "'repoHost'", 
                     "'openGitRepoLocally'", "'closeGitRepo'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BRANCH", "DEPLOY_TO", "REPO_HOST", 
                      "OPEN_GIT_REPO_LOCALLY", "CLOSE_GIT_REPO", "NUM", 
                      "CHARS", "WS", "LINE_COMMENT" ]

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
    RULE_repoAliasName = 16
    RULE_namingChars = 17

    ruleNames =  [ "script", "cmd", "deployTo", "excludePattern", "deployPattern", 
                   "pathForDeployTo", "pathFrom", "setBranch", "setRepoSource", 
                   "host", "cloneGitToTmp", "closeGitRepo", "repoPath", 
                   "pathForDeploy", "pattern", "branchName", "repoAliasName", 
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
    BRANCH=14
    DEPLOY_TO=15
    REPO_HOST=16
    OPEN_GIT_REPO_LOCALLY=17
    CLOSE_GIT_REPO=18
    NUM=19
    CHARS=20
    WS=21
    LINE_COMMENT=22

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
            self.state = 36
            self.cmd()
            self.state = 37
            self.match(DescParser.T__0)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0):
                self.state = 38
                self.cmd()
                self.state = 39
                self.match(DescParser.T__0)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.setBranch()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.setRepoSource()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.cloneGitToTmp()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.closeGitRepo()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.deployTo()
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
            self.state = 55
            self.match(DescParser.DEPLOY_TO)
            self.state = 56
            self.match(DescParser.T__1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 57
                self.pathFrom()
                self.state = 58
                self.match(DescParser.T__2)


            self.state = 62
            self.pathForDeployTo()
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(DescParser.T__2)
                self.state = 64
                self.excludePattern()

            elif la_ == 2:
                self.state = 65
                self.match(DescParser.T__2)
                self.state = 66
                self.deployPattern()

            elif la_ == 3:
                self.state = 67
                self.match(DescParser.T__2)
                self.state = 68
                self.deployPattern()
                self.state = 69
                self.match(DescParser.T__2)
                self.state = 70
                self.excludePattern()

            elif la_ == 4:
                self.state = 72
                self.match(DescParser.T__2)
                self.state = 73
                self.excludePattern()
                self.state = 74
                self.match(DescParser.T__2)
                self.state = 75
                self.deployPattern()


            self.state = 79
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
            self.state = 81
            self.match(DescParser.T__4)
            self.state = 82
            self.pattern()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 83
                self.match(DescParser.T__5)
                self.state = 84
                self.pattern()
                self.state = 89
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
            self.state = 90
            self.match(DescParser.T__6)
            self.state = 91
            self.pattern()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 92
                self.match(DescParser.T__5)
                self.state = 93
                self.pattern()
                self.state = 98
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
            self.state = 99
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
            self.state = 101
            self.match(DescParser.T__7)
            self.state = 102
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
            self.state = 104
            self.match(DescParser.BRANCH)
            self.state = 105
            self.match(DescParser.T__1)
            self.state = 106
            self.branchName()
            self.state = 107
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
            self.state = 109
            self.match(DescParser.REPO_HOST)
            self.state = 110
            self.match(DescParser.T__1)
            self.state = 111
            self.host()
            self.state = 112
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
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 114
                        self.namingChars()
                        self.state = 117 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0)):
                            break

                    self.state = 119
                    self.match(DescParser.T__8) 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.namingChars()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0)):
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
            self.state = 131
            self.match(DescParser.OPEN_GIT_REPO_LOCALLY)
            self.state = 132
            self.match(DescParser.T__1)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0):
                self.state = 133
                self.repoPath()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 134
                    self.match(DescParser.T__2)
                    self.state = 135
                    self.repoAliasName()




            self.state = 140
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
            self.state = 142
            self.match(DescParser.CLOSE_GIT_REPO)
            self.state = 143
            self.match(DescParser.T__1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0):
                self.state = 144
                self.repoAliasName()


            self.state = 147
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
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 149
                self.namingChars()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0)):
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
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 156
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13, 19, 20]:
                    self.state = 154
                    self.namingChars()
                    pass
                elif token in [10]:
                    self.state = 155
                    self.match(DescParser.T__9)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1586176) != 0)):
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
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 163
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13, 19, 20]:
                    self.state = 160
                    self.namingChars()
                    pass
                elif token in [11]:
                    self.state = 161
                    self.match(DescParser.T__10)
                    pass
                elif token in [9]:
                    self.state = 162
                    self.match(DescParser.T__8)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1587712) != 0)):
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
            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.namingChars()
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_repoAliasName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.namingChars()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_namingChars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1585152) != 0)):
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





