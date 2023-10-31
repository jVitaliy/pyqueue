import unittest

from interpreter.services.RsyncCmdBuilder import RsyncCmdBuilder


class InterpreterTest(unittest.TestCase):

    def test_simple_cd(self):
        cmd_str = RsyncCmdBuilder().cd("/path/to").build()
        self.assertEqual("cd /path/to", cmd_str)

    def test_cd_and_rsync(self):
        cmd_str = RsyncCmdBuilder().cd("/path/to").rsync('lr').pattern(['*.git']).dest_folder("/dest/folder").build()
        self.assertEqual("cd /path/to && find . -name \"*.git\" > selected && rsync -lr --files-from=selected . /dest/folder", cmd_str)

    def test_cd_and_rsync_pattern_exclude(self):
        cmd_str = (RsyncCmdBuilder().cd("/path/to").rsync('lr').pattern(['.git', '*.yml']).exclude(['*.desc', '*.conf'])
                   .dest_folder("/dest/folder").build())
        self.assertEqual("cd /path/to && find . -name \".git\" -o -name \"*.yml\" > selected && rsync -lr "
                         "--files-from=selected "
                         "--exclude=*.desc --exclude=*.conf . /dest/folder", cmd_str)

    def test_cd_and_rsync_ssh_remote_dest(self):
        cmd_str = (RsyncCmdBuilder().cd("/path/to").rsync('lr').dest_ssh('git.tauproject.com', 'deploy')
                   .dest_folder("/dest/folder").build())
        self.assertEqual("cd /path/to && rsync -lr -e \"ssh -o StrictHostKeyChecking=no\" . deploy@git.tauproject.com:/dest/folder", cmd_str)


if __name__ == '__main__':
    unittest.main()
