import os
import unittest

from interpreter.DescProcessor import DescProcessor
from interpreter.services.FSService import FSService
from interpreter.TauDeployScriptInterpreter import TauDeployScriptInterpreter


class InterpreterTest(unittest.TestCase):

    def walk(self, filename, processor):
        data_dir = os.path.join(os.path.dirname(__file__), 'integration_test_data')
        data_file = os.path.join(data_dir, filename)
        interpreter = TauDeployScriptInterpreter()
        tree_and_parser = interpreter.get_tree_and_parser(data_file)
        parser = tree_and_parser[0]
        if parser.getNumberOfSyntaxErrors() > 0:
            print("syntax errors")
            return
        interpreter.start_walking_with_processor(tree_and_parser[1], processor)

    @unittest.skip("skip due to not ready infrastructure")
    # TODO fix DescProcessor
    def test_minimal_script(self):
        processor = DescProcessor('tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skip("skip due to not ready infrastructure")
    # TODO fix DescProcessor
    def test_minimal_script_with_commented_close(self):
        processor = DescProcessor('tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone_with_commented_close.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(1, len(processor.scope_stack))
        fsService = FSService()
        self.assertEqual(1, len(processor.scope_stack))
        last_repo = processor.scope_stack.pop()
        self.assertEqual('tauproject/alcyone-pdm/queue-scripts.git', last_repo['path'])
        fsService.deleteTemp(last_repo['tmp_folder'])

    @unittest.skip("skip due to not ready infrastructure")
    def test_minimal_with_deploy(self):
        processor = DescProcessor('develop', 'tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone_and_deploy.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skip("skip due to not ready infrastructure")
    def test_minimal_with_deploy_and_exclude(self):
        processor = DescProcessor('develop', 'tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone_and_deploy_with_exclude.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    # @unittest.skip("skip due to not ready infrastructure")
    # def test_minimal_with_deploy_from(self):
    #     processor = DescProcessor('develop', 'tauproject/alcyone-pdm/queue-scripts.git')
    #     self.walk('minimal_to_clone_and_deploy_from.desc', processor)
    #
    #     self.assertEqual('develop', processor._current_branch)
    #     self.assertEqual('git.tauproject.com', processor._repo_host)
    #     self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(True, "skip due to not ready infrastructure")
    def test_deploy_merge(self):
        processor = DescProcessor('develop', 'tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('deploy_with_merge.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(True, "skip due to not ready infrastructure")
    def test_api_build_deploy_merge(self):
        processor = DescProcessor('develop', 'tauproject/tauproject-api.git')
        self.walk('api_deploy_with_config.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(True, "skip due to not ready infrastructure")
    def test_desc_with_exclude(self):
        processor = DescProcessor('master', 'tauproject/alcyone-pdm/pyqueue.git')
        self.walk('desc_with_exclude.desc', processor)

        self.assertEqual('master', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(True, "skip due to not ready infrastructure")
    def test_remote_deploy(self):
        processor = DescProcessor('master', 'tauproject/alcyone-pdm/pyqueue.git')
        self.walk('remote_deploy_real.desc', processor)

        self.assertEqual('master', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(True, "skip due to not ready infrastructure")
    def test_remote_deploy(self):
        processor = DescProcessor('production', 'tauproject/ui.git')
        self.walk('ui_deployremote.desc', processor)

        self.assertEqual('production', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(True, "skip due to not ready infrastructure")
    def test_remote_deploy(self):
        processor = DescProcessor('develop', 'tauproject/ui.git')
        self.walk('test_apply_config_simple.desc', processor)

        # self.assertEqual('production', processor._current_branch)
        # self.assertEqual('git.tauproject.com', processor._repo_host)
        # self.assertEqual(0, len(processor.scope_stack))

    @unittest.skipIf(False, "skip due to not ready infrastructure")
    def test_python_build(self):
        processor = DescProcessor('master', 'tauproject/alcyone-pdm/pyqueue.git')
        self.walk('test_python_build.desc', processor)


if __name__ == '__main__':
    unittest.main()
