import logging

from interpreter.ConfiguringStage import ConfiguringStage
from interpreter.DescParser import DescParser
from interpreter.services.DeployService import DeployService


class DeployingStage(ConfiguringStage):
    def exitPathForDeployTo(self, ctx: DescParser.PathForDeployToContext):
        if self._current_branch is None:
            return

        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path'] = path_from

    def exitPathFrom(self, ctx: DescParser.PathFromContext):
        if self._current_branch is None:
            return

        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path_from'] = path_from

    def enterExcludePattern(self, ctx: DescParser.ExcludePatternContext):
        if self._current_branch is None:
            return

        self._exclude_pattern = list()

    def enterDeployPattern(self, ctx: DescParser.DeployPatternContext):
        if self._current_branch is None:
            return

        self._deploy_pattern = list()

    def exitPattern(self, ctx: DescParser.PatternContext):
        if self._exclude_pattern is not None:
            self._exclude_pattern.append(ctx.getText())
        elif self._deploy_pattern is not None:
            self._deploy_pattern.append(ctx.getText())

    def exitExcludePattern(self, ctx: DescParser.ExcludePatternContext):
        self._deploy_data['excluded'] = self._exclude_pattern
        self._exclude_pattern = None

    def exitDeployPattern(self, ctx: DescParser.DeployPatternContext):
        if self._current_branch is None:
            return

        self._deploy_data['pattern'] = self._deploy_pattern
        self._deploy_pattern = None

    def enterDeployTo(self, ctx: DescParser.DeployToContext):
        if self._current_branch is None:
            return

        self._deploy_data = {}

    def enterDeployToRemote(self, ctx: DescParser.DeployToRemoteContext):
        if self._current_branch is None:
            return
        self._deploy_data = {}

    def exitRemoteHostParam(self, ctx: DescParser.RemoteHostParamContext):
        if self._current_branch is None:
            return
        self._deploy_data['remote_host'] = ctx.remoteHost().getText()

    def exitRemoteUserParam(self, ctx: DescParser.RemoteUserParamContext):
        if self._current_branch is None:
            return
        self._deploy_data['remote_user'] = ctx.remoteUser().getText()

    def exitRemoteUserPassParam(self, ctx: DescParser.RemoteUserPassParamContext):
        if self._current_branch is None:
            return
        self._deploy_data['remote_user_pass'] = ctx.remoteUserPassword().getText()

    def exitDeployTo(self, ctx: DescParser.DeployToContext):
        if self._current_branch is None:
            return

        excluded = self._deploy_data['excluded'] if 'excluded' in self._deploy_data.keys() else None
        pattern = self._deploy_data['pattern'] if 'pattern' in self._deploy_data.keys() else None

        # self._deploy_service = DeployService()
        current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        project_name = current_repo_data["project_name"]
        path_from = f"{current_repo_data['tmp_folder']}/{project_name}" \
            if 'path_from' not in self._deploy_data.keys() \
            else f"{current_repo_data['tmp_folder']}/{project_name}/{self._deploy_data['path_from']}"
        is_merge = False if ctx.MERGE() is None else True
        self._deploy_service.deploy(path_from, self._deploy_data['path'], exclude=excluded, pattern=pattern,
                                    is_merge=is_merge)

    def exitDeployToRemote(self, ctx: DescParser.DeployToRemoteContext):
        if self._current_branch is None:
            return
        excluded = self._deploy_data['excluded'] if 'excluded' in self._deploy_data.keys() else None
        pattern = self._deploy_data['pattern'] if 'pattern' in self._deploy_data.keys() else None

        # self._deploy_service = DeployService()
        current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        project_name = current_repo_data["project_name"]
        path_from = f"{current_repo_data['tmp_folder']}/{project_name}" \
            if 'path_from' not in self._deploy_data.keys() \
            else f"{current_repo_data['tmp_folder']}/{project_name}/{self._deploy_data['path_from']}"
        is_merge = False if ctx.MERGE() is None else True

        self._deploy_service.deploy_to_remote(self._deploy_data['remote_host'], self._deploy_data['remote_user'],
                                              self._deploy_data['remote_user_pass'],
                                              path_from, self._deploy_data['path'], exclude=excluded, pattern=pattern,
                                    is_merge=is_merge)