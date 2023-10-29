import logging

from interpreter.AbstractProcessor import AbstractProcessor
from interpreter.DescParser import DescParser


class Init(AbstractProcessor):

    def exitBranchName(self, ctx: DescParser.BranchNameContext):
        self._current_branch = ctx.getText()
        if self._current_branch.__eq__(self._target_branch):
            logging.info(f"set branch {self._current_branch}")
        else:
            self._current_branch = None
            # raise GitBranchException(
            #     f"branch `{self._current_branch}` does not match to target branch `{self._target_branch}`")

    def exitSetRepoSource(self, ctx: DescParser.SetRepoSourceContext):
        self._repo_host = ctx.host().getText()
        logging.info(f"set repo host to {self._repo_host}")

    def exitStartSystemService(self, ctx: DescParser.StartSystemServiceContext):
        if self._current_branch is not None:
            service_name = ctx.serviceName().getText()
            self._system_service.startService(service_name)
            logging.info(f"service {service_name} has been started")

    def exitStartSystemServiceRemote(self, ctx: DescParser.StartSystemServiceRemoteContext):
        if self._current_branch is not None:
            service_name = ctx.serviceName().getText()
            ssh_cred = ctx.variableName().getText()
            self._system_service.startServiceRemote(self._variables[ssh_cred], service_name)
            logging.info(f"service {service_name} has been started")

    def exitStopSystemService(self, ctx: DescParser.StopSystemServiceContext):
        if self._current_branch is not None:
            service_name = ctx.serviceName().getText()
            self._system_service.stopService(service_name)
            logging.info(f"service {service_name} has been stopped")

    def exitStopSystemServiceRemote(self, ctx: DescParser.StopSystemServiceRemoteContext):
        if self._current_branch is not None:
            service_name = ctx.serviceName().getText()
            ssh_cred = ctx.variableName().getText()
            self._system_service.stopServiceRemote(self._variables[ssh_cred], service_name)
            logging.info(f"service {service_name} has been stopped")

    def enterVariableSet(self, ctx: DescParser.VariableSetContext):
        if self._variables is None:
            self._variables = dict()

        variable_name = ctx.variableName().getText()
        self._variables[variable_name] = dict()

    def exitSshCredentials(self, ctx: DescParser.SshCredentialsContext):
        ssh_remote = ctx.remoteHostParam().remoteHost().getText()
        ssh_user = ctx.remoteUserParam().remoteUser().getText()
        ssh_user_pass = ctx.remoteUserPassParam().remoteUserPassword().getText()
        self._variables['ssh_credentials'] = {'host': ssh_remote, 'user': ssh_user, 'password': ssh_user_pass}

    def exitVariableSet(self, ctx: DescParser.VariableSetContext):
        variable_name = ctx.variableName().getText()
        self._variables[variable_name] = self._variables['ssh_credentials']
        del self._variables['ssh_credentials']




