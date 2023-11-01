class TarCmdBuilder:
    _CD = 'cd'
    _TAR = 'tar'
    _FIND = 'find'
    _FIND_NAME_PATTERN_KEY = '-name'
    _TAR_EXCLUDE_KEY = '--exclude'
    _TAR_ARCH = '-zcf'
    _TAR_UNARCH = '-zxf'

    def __init__(self):
        self._cmd_list = list()
        self._tar_cmd = list()
        self._find_cmd = list()
        self._project_name = None
        self._src_path = None

    def cd(self, path):
        self._cmd_list.append(f"cd {path}")
        self._src_path = path
        return self

    def tar(self, project_name):
        self._tar_cmd.append(self._TAR)
        self._project_name = project_name
        return self

    def pattern(self, patterns):
        if patterns:
            self._find_cmd.append(self._FIND)
            self._find_cmd.append('.')
            names = list(map(lambda p: f"{self._FIND_NAME_PATTERN_KEY} \"{p}\"", patterns))
            names_str = ' -o '.join(names)
            self._find_cmd.append(names_str)
        return self

    def exclude(self, excludes):
        if excludes:
            excludes = list(map(lambda p: f"{self._TAR_EXCLUDE_KEY}='{p}'", excludes))
            excludes_str = ' '.join(excludes)
            self._tar_cmd.append(f"{excludes_str}")
        return self

    def archive(self):
        if self._tar_cmd:
            self._tar_cmd.append(f"--warning=no-file-changed")
            self._tar_cmd.append(self._TAR_ARCH)
            self._tar_cmd.append(f"{self._project_name}.tar")
            if self._find_cmd:
                find_cmd = ' '.join(self._find_cmd)
                self._tar_cmd.append(f"`{find_cmd}`")
            else:
                self._tar_cmd.append(f".")

        return self

    def unarchive(self):
        if self._tar_cmd:
            self._tar_cmd.append(f"--warning=no-file-changed")
            self._tar_cmd.append(self._TAR_UNARCH)
            self._tar_cmd.append(f"{self._project_name}.tar")
        return self

    def build(self):
        if self._tar_cmd:
            self._cmd_list.append(' '.join(self._tar_cmd))
        return " && ".join(self._cmd_list)
