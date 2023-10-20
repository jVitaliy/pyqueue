import logging

from interpreter.DescParser import DescParser
from interpreter.AbstractProcessor import AbstractProcessor
from interpreter.exceptions.GitBranchException import GitBranchException


class Init(AbstractProcessor):

    def exitBranchName(self, ctx: DescParser.BranchNameContext):
        self._current_branch = ctx.getText()
        if self._current_branch.__eq__(self._target_branch):
            logging.info(f"set branch {self._current_branch}")
        else:
            raise GitBranchException(
                f"branch {self._current_branch} does not match to target branch {self._target_branch}")

    def exitSetRepoSource(self, ctx: DescParser.SetRepoSourceContext):
        logging.info(f"set repo host to {self._repo_host}")

    def exitHost(self, ctx: DescParser.SetRepoSourceContext):
        self._repo_host = ctx.getText()