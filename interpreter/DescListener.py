# Generated from interpreter/Desc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DescParser import DescParser
else:
    from DescParser import DescParser

# This class defines a complete listener for a parse tree produced by DescParser.
class DescListener(ParseTreeListener):

    # Enter a parse tree produced by DescParser#script.
    def enterScript(self, ctx:DescParser.ScriptContext):
        pass

    # Exit a parse tree produced by DescParser#script.
    def exitScript(self, ctx:DescParser.ScriptContext):
        pass


    # Enter a parse tree produced by DescParser#gitRepoScope.
    def enterGitRepoScope(self, ctx:DescParser.GitRepoScopeContext):
        pass

    # Exit a parse tree produced by DescParser#gitRepoScope.
    def exitGitRepoScope(self, ctx:DescParser.GitRepoScopeContext):
        pass


    # Enter a parse tree produced by DescParser#scopeCmds.
    def enterScopeCmds(self, ctx:DescParser.ScopeCmdsContext):
        pass

    # Exit a parse tree produced by DescParser#scopeCmds.
    def exitScopeCmds(self, ctx:DescParser.ScopeCmdsContext):
        pass


    # Enter a parse tree produced by DescParser#setBranch.
    def enterSetBranch(self, ctx:DescParser.SetBranchContext):
        pass

    # Exit a parse tree produced by DescParser#setBranch.
    def exitSetBranch(self, ctx:DescParser.SetBranchContext):
        pass


    # Enter a parse tree produced by DescParser#setRepoSource.
    def enterSetRepoSource(self, ctx:DescParser.SetRepoSourceContext):
        pass

    # Exit a parse tree produced by DescParser#setRepoSource.
    def exitSetRepoSource(self, ctx:DescParser.SetRepoSourceContext):
        pass


    # Enter a parse tree produced by DescParser#host.
    def enterHost(self, ctx:DescParser.HostContext):
        pass

    # Exit a parse tree produced by DescParser#host.
    def exitHost(self, ctx:DescParser.HostContext):
        pass


    # Enter a parse tree produced by DescParser#variableSet.
    def enterVariableSet(self, ctx:DescParser.VariableSetContext):
        pass

    # Exit a parse tree produced by DescParser#variableSet.
    def exitVariableSet(self, ctx:DescParser.VariableSetContext):
        pass


    # Enter a parse tree produced by DescParser#variableName.
    def enterVariableName(self, ctx:DescParser.VariableNameContext):
        pass

    # Exit a parse tree produced by DescParser#variableName.
    def exitVariableName(self, ctx:DescParser.VariableNameContext):
        pass


    # Enter a parse tree produced by DescParser#function.
    def enterFunction(self, ctx:DescParser.FunctionContext):
        pass

    # Exit a parse tree produced by DescParser#function.
    def exitFunction(self, ctx:DescParser.FunctionContext):
        pass


    # Enter a parse tree produced by DescParser#sshCredentials.
    def enterSshCredentials(self, ctx:DescParser.SshCredentialsContext):
        pass

    # Exit a parse tree produced by DescParser#sshCredentials.
    def exitSshCredentials(self, ctx:DescParser.SshCredentialsContext):
        pass


    # Enter a parse tree produced by DescParser#buildProject.
    def enterBuildProject(self, ctx:DescParser.BuildProjectContext):
        pass

    # Exit a parse tree produced by DescParser#buildProject.
    def exitBuildProject(self, ctx:DescParser.BuildProjectContext):
        pass


    # Enter a parse tree produced by DescParser#javaBuild.
    def enterJavaBuild(self, ctx:DescParser.JavaBuildContext):
        pass

    # Exit a parse tree produced by DescParser#javaBuild.
    def exitJavaBuild(self, ctx:DescParser.JavaBuildContext):
        pass


    # Enter a parse tree produced by DescParser#nextBuild.
    def enterNextBuild(self, ctx:DescParser.NextBuildContext):
        pass

    # Exit a parse tree produced by DescParser#nextBuild.
    def exitNextBuild(self, ctx:DescParser.NextBuildContext):
        pass


    # Enter a parse tree produced by DescParser#pythonBuild.
    def enterPythonBuild(self, ctx:DescParser.PythonBuildContext):
        pass

    # Exit a parse tree produced by DescParser#pythonBuild.
    def exitPythonBuild(self, ctx:DescParser.PythonBuildContext):
        pass


    # Enter a parse tree produced by DescParser#buildDir.
    def enterBuildDir(self, ctx:DescParser.BuildDirContext):
        pass

    # Exit a parse tree produced by DescParser#buildDir.
    def exitBuildDir(self, ctx:DescParser.BuildDirContext):
        pass


    # Enter a parse tree produced by DescParser#buildFolder.
    def enterBuildFolder(self, ctx:DescParser.BuildFolderContext):
        pass

    # Exit a parse tree produced by DescParser#buildFolder.
    def exitBuildFolder(self, ctx:DescParser.BuildFolderContext):
        pass


    # Enter a parse tree produced by DescParser#deployToRemote.
    def enterDeployToRemote(self, ctx:DescParser.DeployToRemoteContext):
        pass

    # Exit a parse tree produced by DescParser#deployToRemote.
    def exitDeployToRemote(self, ctx:DescParser.DeployToRemoteContext):
        pass


    # Enter a parse tree produced by DescParser#remoteHostParam.
    def enterRemoteHostParam(self, ctx:DescParser.RemoteHostParamContext):
        pass

    # Exit a parse tree produced by DescParser#remoteHostParam.
    def exitRemoteHostParam(self, ctx:DescParser.RemoteHostParamContext):
        pass


    # Enter a parse tree produced by DescParser#remoteHost.
    def enterRemoteHost(self, ctx:DescParser.RemoteHostContext):
        pass

    # Exit a parse tree produced by DescParser#remoteHost.
    def exitRemoteHost(self, ctx:DescParser.RemoteHostContext):
        pass


    # Enter a parse tree produced by DescParser#remoteUserParam.
    def enterRemoteUserParam(self, ctx:DescParser.RemoteUserParamContext):
        pass

    # Exit a parse tree produced by DescParser#remoteUserParam.
    def exitRemoteUserParam(self, ctx:DescParser.RemoteUserParamContext):
        pass


    # Enter a parse tree produced by DescParser#remoteUser.
    def enterRemoteUser(self, ctx:DescParser.RemoteUserContext):
        pass

    # Exit a parse tree produced by DescParser#remoteUser.
    def exitRemoteUser(self, ctx:DescParser.RemoteUserContext):
        pass


    # Enter a parse tree produced by DescParser#remoteUserPassParam.
    def enterRemoteUserPassParam(self, ctx:DescParser.RemoteUserPassParamContext):
        pass

    # Exit a parse tree produced by DescParser#remoteUserPassParam.
    def exitRemoteUserPassParam(self, ctx:DescParser.RemoteUserPassParamContext):
        pass


    # Enter a parse tree produced by DescParser#remoteUserPassword.
    def enterRemoteUserPassword(self, ctx:DescParser.RemoteUserPasswordContext):
        pass

    # Exit a parse tree produced by DescParser#remoteUserPassword.
    def exitRemoteUserPassword(self, ctx:DescParser.RemoteUserPasswordContext):
        pass


    # Enter a parse tree produced by DescParser#deployTo.
    def enterDeployTo(self, ctx:DescParser.DeployToContext):
        pass

    # Exit a parse tree produced by DescParser#deployTo.
    def exitDeployTo(self, ctx:DescParser.DeployToContext):
        pass


    # Enter a parse tree produced by DescParser#excludePattern.
    def enterExcludePattern(self, ctx:DescParser.ExcludePatternContext):
        pass

    # Exit a parse tree produced by DescParser#excludePattern.
    def exitExcludePattern(self, ctx:DescParser.ExcludePatternContext):
        pass


    # Enter a parse tree produced by DescParser#deployPattern.
    def enterDeployPattern(self, ctx:DescParser.DeployPatternContext):
        pass

    # Exit a parse tree produced by DescParser#deployPattern.
    def exitDeployPattern(self, ctx:DescParser.DeployPatternContext):
        pass


    # Enter a parse tree produced by DescParser#pathForDeployTo.
    def enterPathForDeployTo(self, ctx:DescParser.PathForDeployToContext):
        pass

    # Exit a parse tree produced by DescParser#pathForDeployTo.
    def exitPathForDeployTo(self, ctx:DescParser.PathForDeployToContext):
        pass


    # Enter a parse tree produced by DescParser#pathFrom.
    def enterPathFrom(self, ctx:DescParser.PathFromContext):
        pass

    # Exit a parse tree produced by DescParser#pathFrom.
    def exitPathFrom(self, ctx:DescParser.PathFromContext):
        pass


    # Enter a parse tree produced by DescParser#applyConfiguration.
    def enterApplyConfiguration(self, ctx:DescParser.ApplyConfigurationContext):
        pass

    # Exit a parse tree produced by DescParser#applyConfiguration.
    def exitApplyConfiguration(self, ctx:DescParser.ApplyConfigurationContext):
        pass


    # Enter a parse tree produced by DescParser#configurationBranch.
    def enterConfigurationBranch(self, ctx:DescParser.ConfigurationBranchContext):
        pass

    # Exit a parse tree produced by DescParser#configurationBranch.
    def exitConfigurationBranch(self, ctx:DescParser.ConfigurationBranchContext):
        pass


    # Enter a parse tree produced by DescParser#configBranchName.
    def enterConfigBranchName(self, ctx:DescParser.ConfigBranchNameContext):
        pass

    # Exit a parse tree produced by DescParser#configBranchName.
    def exitConfigBranchName(self, ctx:DescParser.ConfigBranchNameContext):
        pass


    # Enter a parse tree produced by DescParser#configurationPath.
    def enterConfigurationPath(self, ctx:DescParser.ConfigurationPathContext):
        pass

    # Exit a parse tree produced by DescParser#configurationPath.
    def exitConfigurationPath(self, ctx:DescParser.ConfigurationPathContext):
        pass


    # Enter a parse tree produced by DescParser#confPath.
    def enterConfPath(self, ctx:DescParser.ConfPathContext):
        pass

    # Exit a parse tree produced by DescParser#confPath.
    def exitConfPath(self, ctx:DescParser.ConfPathContext):
        pass


    # Enter a parse tree produced by DescParser#cloneGitToTmp.
    def enterCloneGitToTmp(self, ctx:DescParser.CloneGitToTmpContext):
        pass

    # Exit a parse tree produced by DescParser#cloneGitToTmp.
    def exitCloneGitToTmp(self, ctx:DescParser.CloneGitToTmpContext):
        pass


    # Enter a parse tree produced by DescParser#closeGitRepo.
    def enterCloseGitRepo(self, ctx:DescParser.CloseGitRepoContext):
        pass

    # Exit a parse tree produced by DescParser#closeGitRepo.
    def exitCloseGitRepo(self, ctx:DescParser.CloseGitRepoContext):
        pass


    # Enter a parse tree produced by DescParser#repoPath.
    def enterRepoPath(self, ctx:DescParser.RepoPathContext):
        pass

    # Exit a parse tree produced by DescParser#repoPath.
    def exitRepoPath(self, ctx:DescParser.RepoPathContext):
        pass


    # Enter a parse tree produced by DescParser#pathForDeploy.
    def enterPathForDeploy(self, ctx:DescParser.PathForDeployContext):
        pass

    # Exit a parse tree produced by DescParser#pathForDeploy.
    def exitPathForDeploy(self, ctx:DescParser.PathForDeployContext):
        pass


    # Enter a parse tree produced by DescParser#pattern.
    def enterPattern(self, ctx:DescParser.PatternContext):
        pass

    # Exit a parse tree produced by DescParser#pattern.
    def exitPattern(self, ctx:DescParser.PatternContext):
        pass


    # Enter a parse tree produced by DescParser#branchName.
    def enterBranchName(self, ctx:DescParser.BranchNameContext):
        pass

    # Exit a parse tree produced by DescParser#branchName.
    def exitBranchName(self, ctx:DescParser.BranchNameContext):
        pass


    # Enter a parse tree produced by DescParser#startSystemService.
    def enterStartSystemService(self, ctx:DescParser.StartSystemServiceContext):
        pass

    # Exit a parse tree produced by DescParser#startSystemService.
    def exitStartSystemService(self, ctx:DescParser.StartSystemServiceContext):
        pass


    # Enter a parse tree produced by DescParser#stopSystemService.
    def enterStopSystemService(self, ctx:DescParser.StopSystemServiceContext):
        pass

    # Exit a parse tree produced by DescParser#stopSystemService.
    def exitStopSystemService(self, ctx:DescParser.StopSystemServiceContext):
        pass


    # Enter a parse tree produced by DescParser#startSystemServiceRemote.
    def enterStartSystemServiceRemote(self, ctx:DescParser.StartSystemServiceRemoteContext):
        pass

    # Exit a parse tree produced by DescParser#startSystemServiceRemote.
    def exitStartSystemServiceRemote(self, ctx:DescParser.StartSystemServiceRemoteContext):
        pass


    # Enter a parse tree produced by DescParser#stopSystemServiceRemote.
    def enterStopSystemServiceRemote(self, ctx:DescParser.StopSystemServiceRemoteContext):
        pass

    # Exit a parse tree produced by DescParser#stopSystemServiceRemote.
    def exitStopSystemServiceRemote(self, ctx:DescParser.StopSystemServiceRemoteContext):
        pass


    # Enter a parse tree produced by DescParser#serviceName.
    def enterServiceName(self, ctx:DescParser.ServiceNameContext):
        pass

    # Exit a parse tree produced by DescParser#serviceName.
    def exitServiceName(self, ctx:DescParser.ServiceNameContext):
        pass


    # Enter a parse tree produced by DescParser#repoAliasName.
    def enterRepoAliasName(self, ctx:DescParser.RepoAliasNameContext):
        pass

    # Exit a parse tree produced by DescParser#repoAliasName.
    def exitRepoAliasName(self, ctx:DescParser.RepoAliasNameContext):
        pass


    # Enter a parse tree produced by DescParser#namingChars.
    def enterNamingChars(self, ctx:DescParser.NamingCharsContext):
        pass

    # Exit a parse tree produced by DescParser#namingChars.
    def exitNamingChars(self, ctx:DescParser.NamingCharsContext):
        pass


    # Enter a parse tree produced by DescParser#pathChars.
    def enterPathChars(self, ctx:DescParser.PathCharsContext):
        pass

    # Exit a parse tree produced by DescParser#pathChars.
    def exitPathChars(self, ctx:DescParser.PathCharsContext):
        pass



del DescParser