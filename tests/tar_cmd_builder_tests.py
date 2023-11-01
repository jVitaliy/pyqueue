import unittest

from interpreter.services.RsyncCmdBuilder import RsyncCmdBuilder
from interpreter.services.TarCmdBuilder import TarCmdBuilder


class InterpreterTest(unittest.TestCase):

    def test_simple_cd(self):
        cmd_str = TarCmdBuilder().cd("/path/to").build()
        self.assertEqual("cd /path/to", cmd_str)

    def test_cd_and_tar(self):
        cmd_str = TarCmdBuilder().cd("/path/to").tar("project_name").pattern(['*.git']).archive().build()
        self.assertEqual("cd /path/to && tar --warning=no-file-changed -zcf project_name.tar `find . -name \"*.git\"`", cmd_str)

    def test_cd_and_tar_pattern_exclude(self):
        cmd_str = (TarCmdBuilder().cd("/path/to").tar('project_name').pattern(['.git', '*.yml']).exclude(['*.desc', '*.conf'])
                   .archive().build())
        self.assertEqual("cd /path/to && tar --exclude='*.desc' --exclude='*.conf' "
                         "--warning=no-file-changed -zcf project_name.tar `find . -name \".git\" -o -name \"*.yml\"`", cmd_str)

    def test_cd_and_tar_dest(self):
        cmd_str = (TarCmdBuilder().cd("/path/to").tar('project_name').archive().build())
        self.assertEqual(f"cd /path/to && tar --warning=no-file-changed -zcf project_name.tar .", cmd_str)

    def test_cd_and_untar_dest(self):
        cmd_str = (TarCmdBuilder().cd("/path/to").tar('project_name').unarchive().build())
        self.assertEqual(f"cd /path/to && tar --warning=no-file-changed -zxf project_name.tar", cmd_str)


if __name__ == '__main__':
    unittest.main()
