import os
import unittest
from unittest.mock import Mock

from processor.RequestFilesProcessor import RequestFilesProcessor


class InterpreterTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.desc_processor = Mock()
        self.interpreter = Mock()
        self.interpreter.get_tree_and_parser.return_value = [Mock(), Mock()]

    def setUp(self):
        os.environ["PYQUEUE_QUEUE_FOLDER"] = os.path.join(os.path.dirname(__file__), 'test_queue')
        os.environ["PYQUEUE_SCRIPT_FOLDER"] = os.path.join(os.path.dirname(__file__), 'test_scripts')
        os.environ["PYQUEUE_GIT_HOME"] = "/home/git"

    def build_processor(self):
        processor = RequestFilesProcessor()
        processor._desc_interpreter = self.interpreter
        processor._desc_interpreter.get_Processor.return_value = self.desc_processor
        return processor

    def test_empty_queue_folder(self):
        processor = self.build_processor()
        processor.start()
        self.interpreter.start_walking.assert_not_called()

    def test_develop_ui_git_no_script(self):
        script_folder = os.environ["PYQUEUE_SCRIPT_FOLDER"]
        if os.path.exists(f"{script_folder}/ui.desc"):
            os.remove(f"{script_folder}/ui.desc")
        queue_folder = os.environ["PYQUEUE_QUEUE_FOLDER"]
        with open(f"{queue_folder}/develop.ui.git", 'w') as file:
            file.write(f"path:ui.git\n")
            file.write(f"branch:develop\n")

        processor = self.build_processor()
        processor.start()
        self.interpreter.start_walking.assert_not_called()

    def test_develop_ui_git_with_script(self):

        queue_folder = os.environ["PYQUEUE_QUEUE_FOLDER"]
        script_folder = os.environ["PYQUEUE_SCRIPT_FOLDER"]
        if os.path.exists(f"{script_folder}/ui.desc"):
            os.remove(f"{script_folder}/ui.desc")
        with open(f"{queue_folder}/develop.ui.git", 'w') as file:
            file.write(f"path:ui.git\n")
            file.write(f"branch:develop\n")
        script_folder = os.environ["PYQUEUE_SCRIPT_FOLDER"]
        with open(f"{script_folder}/ui.desc", 'w') as file:
            file.write(f"branch(develop);\n")

        processor = self.build_processor()
        processor.start()
        self.interpreter.start_walking.assert_called_once()


    def test_develop_ui_git_queue_with_script(self):

        queue_folder = os.environ["PYQUEUE_QUEUE_FOLDER"]
        script_folder = os.environ["PYQUEUE_SCRIPT_FOLDER"]
        if os.path.exists(f"{script_folder}/ui.desc"):
            os.remove(f"{script_folder}/ui.desc")
        with open(f"{queue_folder}/develop.ui.git.queue", 'w') as file:
            file.write(f"path:ui.git\n")
            file.write(f"branch:develop\n")
        script_folder = os.environ["PYQUEUE_SCRIPT_FOLDER"]
        with open(f"{script_folder}/ui.desc", 'w') as file:
            file.write(f"branch(develop);\n")

        processor = self.build_processor()
        processor.start()
        self.interpreter.start_walking.assert_not_called()

if __name__ == '__main__':
    unittest.main()
