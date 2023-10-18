import os
import unittest

from interpreter.DescProcessor import DescProcessor
from interpreter.services.FSService import FSService
from interpreter.TauDeployScriptInterpreter import get_tree_and_parser, start_walking


class InterpreterTest(unittest.TestCase):

    def walk(self, filename, processor):
        data_dir = os.path.join(os.path.dirname(__file__), 'test_data')
        data_file = os.path.join(data_dir, filename)
        tree_and_parser = get_tree_and_parser(data_file)
        parser = tree_and_parser[0]
        if parser.getNumberOfSyntaxErrors() > 0:
            print("syntax errors")
            return
        start_walking(tree_and_parser[1], processor)


    def test_branch(self):
        processor = DescProcessor()
        self.walk('openbranch.desc', processor)
        self.assertEqual('develop', processor._current_branch)

    def test_branch_and_repo_host(self):
        processor = DescProcessor()
        self.walk('openbranch_and_set_repo.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)

    def test_minimal_script(self):
        processor = DescProcessor('tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

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

    def test_minimal_with_deploy(self):
        processor = DescProcessor('tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone_and_deploy.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    def test_minimal_with_deploy_and_exclude(self):
        processor = DescProcessor('tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone_and_deploy_with_exclude.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

    def test_minimal_with_deploy_from(self):
        processor = DescProcessor('tauproject/alcyone-pdm/queue-scripts.git')
        self.walk('minimal_to_clone_and_deploy_from.desc', processor)

        self.assertEqual('develop', processor._current_branch)
        self.assertEqual('git.tauproject.com', processor._repo_host)
        self.assertEqual(0, len(processor.scope_stack))

if __name__ == '__main__':
    unittest.main()
