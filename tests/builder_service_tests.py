import unittest
from unittest.mock import Mock, call

from interpreter.exceptions.BuildServiceException import BuildServiceException
from interpreter.services.BuilderService import BuilderService


class BuilderServiceTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._builder_service = None

    def setUp(self):
        self._builder_service = BuilderService()
        self._builder_service.execute = Mock()


    def execute_side_effect_no_error(self, *args, **kwargs):
        print(args)
        self._builder_service.returncode = 0
        self._builder_service.error = None

    def execute_error(self, *args, **kwargs):
        self._builder_service.returncode = 1
        self._builder_service.error = "Error msg"

    def test_java17_gradle_error(self):
        self._builder_service.execute.side_effect = self.execute_error
        with self.assertRaises(BuildServiceException):
            self._builder_service.build("java17", "gradle", "test/folder")
        self._builder_service.execute.assert_called_once()
        self._builder_service.execute.assert_called_with('test/folder/gradlew build', working_folder="test/folder")
        self.assertEqual("Error msg", self._builder_service.error)

    def test_java17_gradle_success(self):
        self._builder_service.execute.side_effect = self.execute_side_effect_no_error
        self._builder_service.build("java17", "gradle", "test/folder")
        self._builder_service.execute.assert_called_with('test/folder/gradlew build', working_folder="test/folder")

    def test_next_npm_success(self):
        self._builder_service.execute.side_effect = self.execute_side_effect_no_error
        self._builder_service.build("next", "npm", "test/folder/www")
        self._builder_service.execute.assert_has_calls([call('/usr/bin/npm install', working_folder='test/folder/www'),
                                                        call('/usr/bin/npm run build', working_folder='test/folder/www')])




if __name__ == '__main__':
    unittest.main()
