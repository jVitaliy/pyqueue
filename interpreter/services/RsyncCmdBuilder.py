class RsyncCmdBuilder:
    _CD = 'cd'
    _RSYNC = 'rsync'
    _FILES_FROM = '--files-from'
    _FIND = 'find'
    _FIND_NAME_PATTERN_KEY = '-name'
    _RSYNC_EXCLUDE_KEY = '--exclude'

    def __init__(self):
        self._cmd_list = list()
        self._rsync_cmd = list()
        self._dest_ssh_prefix = None
        self._src_path = None

    def cd(self, path):
        self._cmd_list.append(f"cd {path}")
        self._src_path = path
        return self

    def rsync(self, params=None):
        self._rsync_cmd.append(self._RSYNC)
        if params:
            self._rsync_cmd.append(f"-{params}")
        return self

    def dest_ssh(self, host, user):
        self._dest_ssh_prefix = f"{user}@{host}"
        return self

    def pattern(self, patterns):
        if patterns:
            find = list()
            find.append(self._FIND)
            find.append('.')
            names = list(map(lambda p: f"{self._FIND_NAME_PATTERN_KEY} \"{p}\"", patterns))
            names_str = ' -o '.join(names)
            find.append(names_str)
            find.append('>')
            find.append("selected")
            find_cmd = ' '.join(find)
            self._cmd_list.append(find_cmd)
            self._rsync_cmd.append(f"{self._FILES_FROM}=selected")
        return self

    def exclude(self, excludes):
        if excludes:
            excludes = list(map(lambda p: f"{self._RSYNC_EXCLUDE_KEY}={p}", excludes))
            excludes_str = ' '.join(excludes)
            self._rsync_cmd.append(f"{excludes_str}")
        return self

    def dest_folder(self, path):

        if self._dest_ssh_prefix:
            self._rsync_cmd.append(f"-e '\"ssh -o StrictHostKeyChecking=no\"'")
            self._rsync_cmd.append('.')
            self._rsync_cmd.append(f'{self._dest_ssh_prefix}:{path}')
        else:
            self._rsync_cmd.append('.')
            self._rsync_cmd.append(f'{path}')
        self._cmd_list.append(' '.join(self._rsync_cmd))
        return self

    def build(self):
        return " && ".join(self._cmd_list)
