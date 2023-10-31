class RsyncCmdBuilder:
    _CD = 'cd'
    _RSYNC = 'rsync'
    _FILES_FROM = '--files-from'
    _FIND = 'find .'
    _FIND_NAME_PATTERN_KEY = '-name'
    _RSYNC_EXCLUDE_KEY = '--exclude'

    def __init__(self):
        self._cmd_list = list()
        self._rsync_cmd = list()
        self._dest_ssh_prefix = None

    def cd(self, path):
        self._cmd_list.append(f"cd {path}")
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
            names = list(map(lambda p: f"{self._FIND_NAME_PATTERN_KEY} \"{p}\"", patterns))
            names_str = ' -o '.join(names)
            find.append(names_str)
            find_cmd = ' '.join(find)
            self._rsync_cmd.append(f"{self._FILES_FROM}=<({find_cmd})")
        return self

    def exclude(self, excludes):
        if excludes:
            excludes = list(map(lambda p: f"{self._RSYNC_EXCLUDE_KEY}={p}", excludes))
            excludes_str = ' '.join(excludes)
            self._rsync_cmd.append(f"{excludes_str}")
        return self

    def dest_folder(self, path):
        self._rsync_cmd.append('./')
        if self._dest_ssh_prefix:
            self._rsync_cmd.append(f'{self._dest_ssh_prefix}:{path}')
        else:
            self._rsync_cmd.append(f'{path}')
        self._cmd_list.append(' '.join(self._rsync_cmd))
        return self

    def build(self):
        return " && ".join(self._cmd_list)
