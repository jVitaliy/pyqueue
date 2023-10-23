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


    # Enter a parse tree produced by DescParser#buildProject.
    def enterBuildProject(self, ctx:DescParser.BuildProjectContext):
        pass

    # Exit a parse tree produced by DescParser#buildProject.
    def exitBuildProject(self, ctx:DescParser.BuildProjectContext):
        pass


    # Enter a parse tree produced by DescParser#projectLanguage.
    def enterProjectLanguage(self, ctx:DescParser.ProjectLanguageContext):
        pass

    # Exit a parse tree produced by DescParser#projectLanguage.
    def exitProjectLanguage(self, ctx:DescParser.ProjectLanguageContext):
        pass


    # Enter a parse tree produced by DescParser#builderType.
    def enterBuilderType(self, ctx:DescParser.BuilderTypeContext):
        pass

    # Exit a parse tree produced by DescParser#builderType.
    def exitBuilderType(self, ctx:DescParser.BuilderTypeContext):
        pass


    # Enter a parse tree produced by DescParser#buildFolder.
    def enterBuildFolder(self, ctx:DescParser.BuildFolderContext):
        pass

    # Exit a parse tree produced by DescParser#buildFolder.
    def exitBuildFolder(self, ctx:DescParser.BuildFolderContext):
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