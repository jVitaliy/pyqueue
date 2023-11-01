import os
import unittest
from collections import OrderedDict
from unittest.mock import Mock, call

from interpreter.DescProcessor import DescProcessor
from interpreter.TauDeployScriptInterpreter import TauDeployScriptInterpreter
from interpreter.exceptions.ParseException import ParseException
from interpreter.services.DeployParameters import DeployParameters


class InterpreterTest(unittest.TestCase):
    GIT_HOST = 'git.tauproject.com'
    REPO_PATH = 'tauproject/alcyone-pdm/queue-scripts.git'
    TMP_PATH = '/tmp/tauproject/alcyone-pdm'
    TMP_PATH_CONF = '/tmp/tauproject/alcyone-pdm'

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._git_service = Mock()
        self._config_service = Mock()
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
        processor._config_service = self._config_service
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
        self.assertEqual('localhost', processor._repo_host)

    def test_minimal_with_deploy(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone_and_deploy.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        deploy_param1 = DeployParameters(src_path=f"{self.TMP_PATH}/test-pro",
                                         dest_path="/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy",
                                         exclude=None, pattern=None, is_merge=False, project_name="test-pro")
        self._deploy_service.deploy.assert_called_with(deploy_param1)

    def test_minimal_with_deploy_and_exclude(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone_and_deploy_with_exclude.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        deploy_param1 = DeployParameters(src_path=f"{self.TMP_PATH}/test-pro",
                                         dest_path="/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy",
                                         exclude=['.git'], pattern=['queue-scripts', 'queue.git'], is_merge=False,
                                         project_name="test-pro")
        self._deploy_service.deploy.assert_called_with(deploy_param1)

    def test_minimal_with_deploy_from(self):
        processor = self.build_processor("develop")
        self.walk('minimal_to_clone_and_deploy_from.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        deploy_param1 = DeployParameters(src_path=f"{self.TMP_PATH}/test-pro/scripts",
                                         dest_path="/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy",
                                         exclude=['.git'], pattern=None, is_merge=False, project_name="test-pro")
        self._deploy_service.deploy.assert_called_with(deploy_param1)

    def test_deploy_with_start_stop_service(self):
        processor = self.build_processor("develop")
        self.walk('deploy_with_start_stop.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_called_once()
        self._git_service.clone.assert_called_with(self.REPO_PATH, self.GIT_HOST)
        self._deploy_service.deploy.assert_called_once()
        deploy_param1 = DeployParameters(src_path=f"{self.TMP_PATH}/test-pro",
                                         dest_path="/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy",
                                         exclude=None, pattern=None, is_merge=False, project_name="test-pro")
        self._deploy_service.deploy.assert_called_with(deploy_param1)
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
        deploy_param1 = DeployParameters(src_path=f"{self.TMP_PATH}/test-pro",
                                        dest_path="/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy",
                                        exclude=None, pattern=None, is_merge=False, project_name="test-pro")
        deploy_param2 = DeployParameters(src_path=f"{self.TMP_PATH_CONF}/test-conf",
                                        dest_path="/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy/cfg",
                                        exclude=None, pattern=['*.yml'], is_merge=True, project_name="test-conf")
        self._deploy_service.deploy.assert_has_calls([call(deploy_param1),call(deploy_param2)])
        self._system_service.startService.assert_called_once()
        self._git_service.removeFolder.assert_has_calls([call(self.TMP_PATH_CONF), call(self.TMP_PATH)])
        self._system_service.stopService.assert_called_once()

    def test_deploy_with_build_in_deploy_dir(self):
        processor = self.build_processor("develop")

        self.walk('ui_with_build_in_deploy_dir.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual(self.GIT_HOST, processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST),
                                                  call("tauproject/tau-config.git", self.GIT_HOST)])
        deploy_param1 = DeployParameters(src_path=f"{self.TMP_PATH}/test-pro",
                                        dest_path="/var/www/tauproject/develop",
                                        exclude=['.git', '.gitignore'], pattern=None, is_merge=False, project_name="test-pro")
        deploy_param2 = DeployParameters(src_path=f"{self.TMP_PATH_CONF}/test-conf/ui",
                                        dest_path="/var/www/tauproject/develop",
                                        exclude=None, pattern=['.env'], is_merge=True, project_name="test-conf")
        self._deploy_service.deploy.assert_has_calls([call(deploy_param1), call(deploy_param2)])
        self._system_service.startService.assert_called_once()
        self._git_service.removeFolder.assert_has_calls([call(self.TMP_PATH_CONF), call(self.TMP_PATH)])
        self._system_service.stopService.assert_called_once()
        self._builder_service.build.assert_has_calls([call("next", "npm", "/var/www/tauproject/develop")])

    def test_minimal_for_2_branches(self):
        processor = self.build_processor("master")
        self.walk('minimal_for_2_branches.desc', processor)

        # self.assertEqual('develop', processor._current_branch)
        # self.assertEqual('localhost', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, 'git.tauproject.com')])

    def test_remote_deploy(self):
        processor = self.build_processor("master")
        self.walk('remote_deploy.desc', processor)
        self._deploy_service.deploy.assert_not_called()
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST)])
        credentials = {'host': '173.249.48.192', 'user': 'deploy', 'key': '~/.ssh/deploy_id_rsa'}
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro/build/libs',
                                         dest_path='/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                         exclude=None, pattern=['*.jar'], is_merge=False, project_name="test-pro")
        self._deploy_service.deploy_to_remote.assert_has_calls([call(credentials, deploy_param1)])
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, 'git.tauproject.com')])

    def test_remote_deploy_with_2_scopes(self):
        processor = self.build_processor("develop")
        self.walk('open_2_scopes_deployremote.desc', processor)
        self._deploy_service.deploy.assert_not_called()
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST),
                                                  call("tauproject/tau-config.git", self.GIT_HOST)])
        credentials = {'host': '173.249.48.192', 'user': 'deploy', 'key': '~/.ssh/deploy_id_rsa'}
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro',
                                         dest_path='/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                         exclude=['.git'], pattern=None, is_merge=False, project_name="test-pro")
        call1 = call(credentials, deploy_param1)
        deploy_param2 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-conf',
                                         dest_path='/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy/cfg',
                                         exclude=None, pattern=['*.yml'], is_merge=True, project_name="test-conf")
        call2 = call(credentials, deploy_param2)
        self._deploy_service.deploy_to_remote.assert_has_calls([call1, call2])
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, 'git.tauproject.com')])

    def test_remote_deploy_ui(self):
        processor = self.build_processor("production")
        self.walk('ui_deployremote_minimal_no_build.desc', processor)
        self._deploy_service.deploy.assert_not_called()
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, 'localhost'),
                                                  call("tauproject/tau-config.git", 'localhost')])
        credentials = {'host': '173.249.48.192', 'user': 'deploy', 'key': '~/.ssh/deploy_id_rsa'}
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro',
                                         dest_path='/var/www/tauproject',
                                         exclude=['.git', '.gitignore'], pattern=None, is_merge=False,
                                         project_name="test-pro")
        call1 = call(credentials, deploy_param1)
        deploy_param2 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-conf/ui',
                                         dest_path='/var/www/tauproject',
                                         exclude=['.git', '.gitignore'], pattern=['.env'], is_merge=True,
                                         project_name="test-conf")
        call2 = call(credentials, deploy_param2)
        self._deploy_service.deploy_to_remote.assert_has_calls([call1, call2])
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call('tauproject/alcyone-pdm/queue-scripts.git', 'localhost'),
            call('tauproject/tau-config.git', 'localhost')])

    def test_remote_deploy_ui_start_stop_remote(self):
        processor = self.build_processor("production")
        self.walk('ui_deployremote_start_stop_remote.desc', processor)
        self._deploy_service.deploy.assert_not_called()
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, 'localhost'),
                                                  call("tauproject/tau-config.git", 'localhost')])
        credentials = {'host': '173.249.48.192', 'user': 'deploy', 'key': '~/.ssh/deploy_id_rsa'}
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro',
                                         dest_path='/var/www/tauproject',
                                         exclude=['.git', '.gitignore'], pattern=None, is_merge=False,
                                         project_name="test-pro")
        call1 = call(credentials, deploy_param1)
        deploy_param2 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-conf/ui',
                                         dest_path='/var/www/tauproject',
                                         exclude=['.git', '.gitignore'], pattern=['.env'], is_merge=True,
                                         project_name="test-conf")
        call2 = call(credentials, deploy_param2)
        self._deploy_service.deploy_to_remote.assert_has_calls([call1, call2])
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call('tauproject/alcyone-pdm/queue-scripts.git', 'localhost'),
            call('tauproject/tau-config.git', 'localhost')])
        # credentials = OrderedDict({'host': '173.249.48.192', 'user': 'deploy', 'password': 'e_4F1KzUjc-1tR6e'})
        call3 = call(credentials, 'www-service')
        self._system_service.stopServiceRemote.assert_has_calls([call3])
        self._system_service.startServiceRemote.assert_has_calls([call3])

    def test_apply_config(self):
        processor = self.build_processor("develop")
        self.walk('apply_config_simple.desc', processor)
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro',
                                        dest_path='/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                        exclude=None, pattern=None, is_merge=False, project_name="test-pro")
        calls = self._deploy_service.deploy.call_args
        param = calls[0][0]
        self.assertEqual(param, deploy_param1)
        self._deploy_service.deploy.assert_has_calls([call(deploy_param1)])
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST)])
        self._system_service.stopService.assert_has_calls([call("www-service")])
        self._system_service.startService.assert_has_calls([call("www-service")])
        self._deploy_service.deploy_to_remote.assert_not_called()
        self.assertEqual(0, len(processor.scope_stack))
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST)])
        self._config_service.apply.assert_has_calls([call( self.GIT_HOST, "tauproject/config.git", "prod", "devel",
                                                          '/tmp/tauproject/alcyone-pdm/test-pro',
                                                          exclude=None, pattern=['application.yml'],
                                                          git_service=self._git_service)])

    def test_script_for_2_branches_and_build_and_deploy(self):
        processor = self.build_processor("staging")
        self.walk('script_for_2_branches_with_build_and_deploy.desc', processor)
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, 'localhost')])
        self._config_service.apply.assert_has_calls([call( 'localhost', "tauproject/tau-config.git", "develop", "backend/staging",
                                                          '/tmp/tauproject/alcyone-pdm/test-pro',
                                                          exclude=None, pattern=['*.yml'],
                                                          git_service=self._git_service)])
        self._system_service.stopService.assert_has_calls([call("tauproject-staging-api")])
        self._system_service.startService.assert_has_calls([call("tauproject-staging-api")])
        self._builder_service.build.assert_has_calls([call("java17", "gradle", "/tmp/tauproject/alcyone-pdm/test-pro")])
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro/build/libs',
                                         dest_path='/usr/local/tauproject/backend/staging',
                                         exclude=None, pattern=['*.jar'], is_merge=False, project_name="test-pro")
        self._deploy_service.deploy.assert_has_calls([call(deploy_param1)])

    def test_script_for_deploy_remote_with_archiving(self):
        processor = self.build_processor("staging")
        self.walk('script_for_deploy_remote_with_archiving.desc', processor)
        self._git_service.clone.assert_has_calls([call(self.REPO_PATH, self.GIT_HOST)])
        credentials = {'host': '173.249.48.192', 'user': 'deploy', 'key': '~/.ssh/deploy_id_rsa'}
        deploy_param1 = DeployParameters(src_path='/tmp/tauproject/alcyone-pdm/test-pro/build/libs',
                                         dest_path='/develop/tauprojects/alcyone/alcyone-pdm/pyqueue/testdeploy',
                                         exclude=None, pattern=['*.jar'], is_merge=False, project_name="test-pro")
        self._deploy_service.deploy_archived_to_remote.assert_has_calls([call(credentials, deploy_param1)])


if __name__ == '__main__':
    unittest.main()
