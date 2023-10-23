import os
import unittest
from unittest.mock import Mock, call

from interpreter.DescProcessor import DescProcessor
from interpreter.TauDeployScriptInterpreter import TauDeployScriptInterpreter
from interpreter.exceptions.ParseException import ParseException


class InterpreterTest(unittest.TestCase):
    GIT_HOST = 'git.tauproject.com'
    REPO_PATH = 'tauproject/alcyone-pdm/queue-scripts.git'
    TMP_PATH = '/tmp/tauproject/alcyone-pdm'
    TMP_PATH_CONF = '/tmp/tauproject/alcyone-pdm'

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._git_service = Mock()
        self._deploy_service = Mock()
        self._system_service = Mock()
        self._builder_service = Mock()
        self._script_interpreter = TauDeployScriptInterpreter()

    def walk(self, filename, processor):
        data_dir = os.path.join(os.path.dirname(__file__), 'test_data')
        data_file = os.path.join(data_dir, filename)
        tree_and_parser = self._script_interpreter.get_tree_and_parser(data_file)
        parser = tree_and_parser[0]
        # if parser.getNumberOfSyntaxErrors() > 0:
        #     print(self._script_interpreter.error_listener.errors)
        #     return
        self._script_interpreter.start_walking_with_processor(tree_and_parser[1], processor)

    def build_processor(self, branch, repo_path=None):
        repo_path_correct = self.REPO_PATH if repo_path is None else repo_path
        processor = DescProcessor(branch, repo_path=repo_path_correct)
        processor._deploy_service = self._deploy_service
        processor._git_service = self._git_service
        processor._system_service = self._system_service
        processor._builder_service = self._builder_service
        paths = [self.TMP_PATH, self.TMP_PATH_CONF]
        self._git_service.clone.side_effect = paths
        repo_names = ["test-pro", "test-conf"]
        self._git_service.getRepoName.side_effect = repo_names
        return processor

    def test_branch(self):
        processor = self.build_processor("develop")
        self.walk('openbranch.desc', processor)
        self.assertEqual('develop', processor._current_branch)

    def test_branch_and_repo_host(self):
        processor = self.build_processor("develop")
        self.walk('openbranch_and_set_repo.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)

    def test_minimal_script(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)

    def test_minimal_script_with_commented_close(self):
        processor = self.build_processor("develop")
        with self.assertRaises(ParseException):
            self.walk('minimal_to_clone_with_commented_close.desc', processor)

        self.assertIsNone(processor._current_branch)
        self.assertIsNone(processor._repo_host)

    def test_minimal_with_deploy(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone_and_deploy.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        self._deploy_service.deploy.assert_called_with(f"{self.TMP_PATH}/test-pro",
                                                       '/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                                       exclude=None, pattern=None, is_merge=False)

    def test_minimal_with_deploy_and_exclude(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone_and_deploy_with_exclude.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        self._deploy_service.deploy.assert_called_with(f"{self.TMP_PATH}/test-pro",
                                                       '/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                                       exclude=['.git'], pattern=['queue-scripts', 'queue.git'],
                                                       is_merge=False)

    def test_minimal_with_deploy_from(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone_and_deploy_from.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        self._deploy_service.deploy.assert_called_with(f"{self.TMP_PATH}/test-pro/scripts",
                                                       '/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                                       exclude=['.git'], pattern=None, is_merge=False)

    def test_deploy_with_start_stop_service(self):
        processor = self.build_processor("develop")
        self.walk('deploy_with_start_stop.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        self._deploy_service.deploy.assert_called_with(f"{self.TMP_PATH}/test-pro",
                                                       '/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                                       exclude=None, pattern=None, is_merge=False)
        self._system_service.startService.assert_called_once()
        self._system_service.stopService.assert_called_once()

    def test_open_with_start_stop_and_build(self):
        processor = self.build_processor("develop")
        self._git_service.getRepoName.return_value = "test-pro"
        self.walk('open_with_start_stop_and_build.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_not_called()
        self._system_service.startService.assert_called_once()
        self._system_service.stopService.assert_called_once()
        self._builder_service.build.assert_called_once()
        self._builder_service.build.assert_called_with("java17", "gradle", f"{self.TMP_PATH}/test-pro")

    def test_deploy_with_nested_scopes(self):
        processor = self.build_processor("develop")

        self.walk('open_2_scopes.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST),
                                                  call("path/to/config.git", self.GIT_HOST)])
        self._deploy_service.deploy.assert_has_calls(
            [
                call(f"{self.TMP_PATH}/test-pro", "/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy",
                    exclude=None, pattern=None, is_merge=False),
                call(f"{self.TMP_PATH_CONF}/test-conf", "/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy/cfg",
                     exclude=None, pattern=['*.yml'], is_merge=True)
            ])
        self._system_service.startService.assert_called_once()
        self._git_service.removeFolder.assert_has_calls([call(self.TMP_PATH_CONF), call(self.TMP_PATH)])
        self._system_service.stopService.assert_called_once()


if __name__ == '__main__':
    unittest.main()
