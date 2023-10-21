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
        4,1,33,224,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,0,5,0,54,8,
        0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,69,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,4,4,82,8,4,11,4,
        12,4,83,1,4,1,4,5,4,88,8,4,10,4,12,4,91,9,4,1,4,4,4,94,8,4,11,4,
        12,4,95,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,3,8,117,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,134,8,8,1,8,1,8,1,9,1,9,1,9,1,9,
        5,9,142,8,9,10,9,12,9,145,9,9,1,10,1,10,1,10,1,10,5,10,151,8,10,
        10,10,12,10,154,9,10,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,3,13,166,8,13,3,13,168,8,13,1,13,1,13,1,14,1,14,1,14,3,14,175,
        8,14,1,14,1,14,1,15,4,15,180,8,15,11,15,12,15,181,1,16,1,16,4,16,
        186,8,16,11,16,12,16,187,1,17,1,17,1,17,4,17,193,8,17,11,17,12,17,
        194,1,18,4,18,198,8,18,11,18,12,18,199,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,21,4,21,213,8,21,11,21,12,21,214,1,22,
        4,22,218,8,22,11,22,12,22,219,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,3,1,0,17,
        19,1,0,15,16,2,0,13,14,30,31,229,0,48,1,0,0,0,2,68,1,0,0,0,4,70,
        1,0,0,0,6,75,1,0,0,0,8,89,1,0,0,0,10,97,1,0,0,0,12,104,1,0,0,0,14,
        108,1,0,0,0,16,111,1,0,0,0,18,137,1,0,0,0,20,146,1,0,0,0,22,155,
        1,0,0,0,24,157,1,0,0,0,26,160,1,0,0,0,28,171,1,0,0,0,30,179,1,0,
        0,0,32,185,1,0,0,0,34,192,1,0,0,0,36,197,1,0,0,0,38,201,1,0,0,0,
        40,206,1,0,0,0,42,212,1,0,0,0,44,217,1,0,0,0,46,221,1,0,0,0,48,49,
        3,2,1,0,49,55,5,1,0,0,50,51,3,2,1,0,51,52,5,1,0,0,52,54,1,0,0,0,
        53,50,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,
        0,0,0,57,55,1,0,0,0,58,59,5,0,0,1,59,1,1,0,0,0,60,69,3,4,2,0,61,
        69,3,6,3,0,62,69,3,26,13,0,63,69,3,28,14,0,64,69,3,16,8,0,65,69,
        3,38,19,0,66,69,3,40,20,0,67,69,3,10,5,0,68,60,1,0,0,0,68,61,1,0,
        0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,68,65,1,0,0,0,68,66,
        1,0,0,0,68,67,1,0,0,0,69,3,1,0,0,0,70,71,5,25,0,0,71,72,5,2,0,0,
        72,73,3,36,18,0,73,74,5,3,0,0,74,5,1,0,0,0,75,76,5,27,0,0,76,77,
        5,2,0,0,77,78,3,8,4,0,78,79,5,3,0,0,79,7,1,0,0,0,80,82,3,46,23,0,
        81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,
        0,0,0,85,86,5,4,0,0,86,88,1,0,0,0,87,81,1,0,0,0,88,91,1,0,0,0,89,
        87,1,0,0,0,89,90,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,92,94,3,46,
        23,0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,
        9,1,0,0,0,97,98,5,22,0,0,98,99,5,2,0,0,99,100,3,12,6,0,100,101,5,
        21,0,0,101,102,3,14,7,0,102,103,5,3,0,0,103,11,1,0,0,0,104,105,5,
        20,0,0,105,106,5,5,0,0,106,107,7,0,0,0,107,13,1,0,0,0,108,109,5,
        6,0,0,109,110,7,1,0,0,110,15,1,0,0,0,111,112,5,26,0,0,112,116,5,
        2,0,0,113,114,3,24,12,0,114,115,5,21,0,0,115,117,1,0,0,0,116,113,
        1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,133,3,22,11,0,119,120,
        5,21,0,0,120,134,3,18,9,0,121,122,5,21,0,0,122,134,3,20,10,0,123,
        124,5,21,0,0,124,125,3,20,10,0,125,126,5,21,0,0,126,127,3,18,9,0,
        127,134,1,0,0,0,128,129,5,21,0,0,129,130,3,18,9,0,130,131,5,21,0,
        0,131,132,3,20,10,0,132,134,1,0,0,0,133,119,1,0,0,0,133,121,1,0,
        0,0,133,123,1,0,0,0,133,128,1,0,0,0,133,134,1,0,0,0,134,135,1,0,
        0,0,135,136,5,3,0,0,136,17,1,0,0,0,137,138,5,7,0,0,138,143,3,34,
        17,0,139,140,5,8,0,0,140,142,3,34,17,0,141,139,1,0,0,0,142,145,1,
        0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,19,1,0,0,0,145,143,1,0,
        0,0,146,147,5,9,0,0,147,152,3,34,17,0,148,149,5,8,0,0,149,151,3,
        34,17,0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,
        1,0,0,0,153,21,1,0,0,0,154,152,1,0,0,0,155,156,3,32,16,0,156,23,
        1,0,0,0,157,158,5,10,0,0,158,159,3,32,16,0,159,25,1,0,0,0,160,161,
        5,28,0,0,161,167,5,2,0,0,162,165,3,30,15,0,163,164,5,21,0,0,164,
        166,3,44,22,0,165,163,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,
        162,1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,5,3,0,0,170,
        27,1,0,0,0,171,172,5,29,0,0,172,174,5,2,0,0,173,175,3,44,22,0,174,
        173,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,5,3,0,0,177,
        29,1,0,0,0,178,180,3,46,23,0,179,178,1,0,0,0,180,181,1,0,0,0,181,
        179,1,0,0,0,181,182,1,0,0,0,182,31,1,0,0,0,183,186,3,46,23,0,184,
        186,5,11,0,0,185,183,1,0,0,0,185,184,1,0,0,0,186,187,1,0,0,0,187,
        185,1,0,0,0,187,188,1,0,0,0,188,33,1,0,0,0,189,193,3,46,23,0,190,
        193,5,12,0,0,191,193,5,4,0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,
        191,1,0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,
        35,1,0,0,0,196,198,3,46,23,0,197,196,1,0,0,0,198,199,1,0,0,0,199,
        197,1,0,0,0,199,200,1,0,0,0,200,37,1,0,0,0,201,202,5,23,0,0,202,
        203,5,2,0,0,203,204,3,42,21,0,204,205,5,3,0,0,205,39,1,0,0,0,206,
        207,5,24,0,0,207,208,5,2,0,0,208,209,3,42,21,0,209,210,5,3,0,0,210,
        41,1,0,0,0,211,213,3,46,23,0,212,211,1,0,0,0,213,214,1,0,0,0,214,
        212,1,0,0,0,214,215,1,0,0,0,215,43,1,0,0,0,216,218,3,46,23,0,217,
        216,1,0,0,0,218,219,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,
        45,1,0,0,0,221,222,7,2,0,0,222,47,1,0,0,0,20,55,68,83,89,95,116,
        133,143,152,165,167,174,181,185,187,192,194,199,214,219
    ]

class DescParser ( Parser ):

    grammarFileName = "Desc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'.'", "'='", "'type='", 
                     "'exclude='", "'|'", "'pattern='", "'from='", "'/'", 
                     "'*'", "'-'", "'_'", "'gradle'", "'maven'", "'java17'", 
                     "'next'", "'python39'", "'language'", "','", "'buildProject'", 
                     "'startSystemService'", "'stopSystemService'", "'branch'", 
                     "'deployTo'", "'repoHost'", "'openGitRepoLocally'", 
                     "'closeGitRepo'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "GRADLE", "MAVEN", 
                      "JAVA17", "NEXT", "PYTHON39", "LANGUAGE", "COMMA", 
                      "BUILD_PROJECT", "START_SYSTEM_SERVICE", "STOP_SYSTEM_SERVICE", 
                      "BRANCH", "DEPLOY_TO", "REPO_HOST", "OPEN_GIT_REPO_LOCALLY", 
                      "CLOSE_GIT_REPO", "NUM", "CHARS", "WS", "LINE_COMMENT" ]

    RULE_script = 0
    RULE_cmd = 1
    RULE_setBranch = 2
    RULE_setRepoSource = 3
    RULE_host = 4
    RULE_buildProject = 5
    RULE_projectLanguage = 6
    RULE_builderType = 7
    RULE_deployTo = 8
    RULE_excludePattern = 9
    RULE_deployPattern = 10
    RULE_pathForDeployTo = 11
    RULE_pathFrom = 12
    RULE_cloneGitToTmp = 13
    RULE_closeGitRepo = 14
    RULE_repoPath = 15
    RULE_pathForDeploy = 16
    RULE_pattern = 17
    RULE_branchName = 18
    RULE_startSystemService = 19
    RULE_stopSystemService = 20
    RULE_serviceName = 21
    RULE_repoAliasName = 22
    RULE_namingChars = 23

    ruleNames =  [ "script", "cmd", "setBranch", "setRepoSource", "host", 
                   "buildProject", "projectLanguage", "builderType", "deployTo", 
                   "excludePattern", "deployPattern", "pathForDeployTo", 
                   "pathFrom", "cloneGitToTmp", "closeGitRepo", "repoPath", 
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
    GRADLE=15
    MAVEN=16
    JAVA17=17
    NEXT=18
    PYTHON39=19
    LANGUAGE=20
    COMMA=21
    BUILD_PROJECT=22
    START_SYSTEM_SERVICE=23
    STOP_SYSTEM_SERVICE=24
    BRANCH=25
    DEPLOY_TO=26
    REPO_HOST=27
    OPEN_GIT_REPO_LOCALLY=28
    CLOSE_GIT_REPO=29
    NUM=30
    CHARS=31
    WS=32
    LINE_COMMENT=33

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
            self.state = 48
            self.cmd()
            self.state = 49
            self.match(DescParser.T__0)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1069547520) != 0):
                self.state = 50
                self.cmd()
                self.state = 51
                self.match(DescParser.T__0)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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


        def buildProject(self):
            return self.getTypedRuleContext(DescParser.BuildProjectContext,0)


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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.setBranch()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.setRepoSource()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.cloneGitToTmp()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.closeGitRepo()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.deployTo()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.startSystemService()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.stopSystemService()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 8)
                self.state = 67
                self.buildProject()
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
        self.enterRule(localctx, 4, self.RULE_setBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(DescParser.BRANCH)
            self.state = 71
            self.match(DescParser.T__1)
            self.state = 72
            self.branchName()
            self.state = 73
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 6, self.RULE_setRepoSource)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(DescParser.REPO_HOST)
            self.state = 76
            self.match(DescParser.T__1)
            self.state = 77
            self.host()
            self.state = 78
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 8, self.RULE_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 80
                        self.namingChars()
                        self.state = 83 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
                            break

                    self.state = 85
                    self.match(DescParser.T__3) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.namingChars()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
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


        def COMMA(self):
            return self.getToken(DescParser.COMMA, 0)

        def builderType(self):
            return self.getTypedRuleContext(DescParser.BuilderTypeContext,0)


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
        self.enterRule(localctx, 10, self.RULE_buildProject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(DescParser.BUILD_PROJECT)
            self.state = 98
            self.match(DescParser.T__1)
            self.state = 99
            self.projectLanguage()
            self.state = 100
            self.match(DescParser.COMMA)
            self.state = 101
            self.builderType()
            self.state = 102
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 12, self.RULE_projectLanguage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(DescParser.LANGUAGE)
            self.state = 105
            self.match(DescParser.T__4)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_builderType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(DescParser.T__5)
            self.state = 109
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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
        self.enterRule(localctx, 16, self.RULE_deployTo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(DescParser.DEPLOY_TO)
            self.state = 112
            self.match(DescParser.T__1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 113
                self.pathFrom()
                self.state = 114
                self.match(DescParser.COMMA)


            self.state = 118
            self.pathForDeployTo()
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 119
                self.match(DescParser.COMMA)
                self.state = 120
                self.excludePattern()

            elif la_ == 2:
                self.state = 121
                self.match(DescParser.COMMA)
                self.state = 122
                self.deployPattern()

            elif la_ == 3:
                self.state = 123
                self.match(DescParser.COMMA)
                self.state = 124
                self.deployPattern()
                self.state = 125
                self.match(DescParser.COMMA)
                self.state = 126
                self.excludePattern()

            elif la_ == 4:
                self.state = 128
                self.match(DescParser.COMMA)
                self.state = 129
                self.excludePattern()
                self.state = 130
                self.match(DescParser.COMMA)
                self.state = 131
                self.deployPattern()


            self.state = 135
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 18, self.RULE_excludePattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(DescParser.T__6)
            self.state = 138
            self.pattern()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 139
                self.match(DescParser.T__7)
                self.state = 140
                self.pattern()
                self.state = 145
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
        self.enterRule(localctx, 20, self.RULE_deployPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(DescParser.T__8)
            self.state = 147
            self.pattern()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 148
                self.match(DescParser.T__7)
                self.state = 149
                self.pattern()
                self.state = 154
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
        self.enterRule(localctx, 22, self.RULE_pathForDeployTo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
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
        self.enterRule(localctx, 24, self.RULE_pathFrom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(DescParser.T__9)
            self.state = 158
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
        self.enterRule(localctx, 26, self.RULE_cloneGitToTmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(DescParser.OPEN_GIT_REPO_LOCALLY)
            self.state = 161
            self.match(DescParser.T__1)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0):
                self.state = 162
                self.repoPath()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 163
                    self.match(DescParser.COMMA)
                    self.state = 164
                    self.repoAliasName()




            self.state = 169
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 28, self.RULE_closeGitRepo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(DescParser.CLOSE_GIT_REPO)
            self.state = 172
            self.match(DescParser.T__1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0):
                self.state = 173
                self.repoAliasName()


            self.state = 176
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 30, self.RULE_repoPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.namingChars()
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_pathForDeploy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 185
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13, 14, 30, 31]:
                    self.state = 183
                    self.namingChars()
                    pass
                elif token in [11]:
                    self.state = 184
                    self.match(DescParser.T__10)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 187 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221252096) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13, 14, 30, 31]:
                    self.state = 189
                    self.namingChars()
                    pass
                elif token in [12]:
                    self.state = 190
                    self.match(DescParser.T__11)
                    pass
                elif token in [4]:
                    self.state = 191
                    self.match(DescParser.T__3)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 194 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221254160) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_branchName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 196
                self.namingChars()
                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_startSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(DescParser.START_SYSTEM_SERVICE)
            self.state = 202
            self.match(DescParser.T__1)
            self.state = 203
            self.serviceName()
            self.state = 204
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 40, self.RULE_stopSystemService)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(DescParser.STOP_SYSTEM_SERVICE)
            self.state = 207
            self.match(DescParser.T__1)
            self.state = 208
            self.serviceName()
            self.state = 209
            self.match(DescParser.T__2)
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
        self.enterRule(localctx, 42, self.RULE_serviceName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 211
                self.namingChars()
                self.state = 214 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_repoAliasName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 216
                self.namingChars()
                self.state = 219 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
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
        self.enterRule(localctx, 46, self.RULE_namingChars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3221250048) != 0)):
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





