import fnmatch
import os
import shutil


class DeployService:
    def __init__(self, exclude=None, pattern=None):
        self._excluded = exclude
        self._patterns = pattern

    def _ignore_patterns(self, path, names):
        # print(path)
        ignored_names = set()
        if self._excluded is not None:
            for pattern in self._excluded:
                ignored_names.update(fnmatch.filter(names, pattern))

        if self._patterns is not None:
            all_names = set(names)
            pattern_names = set()
            for pattern in self._patterns:
                pattern_names.update(fnmatch.filter(names, pattern))
            # print(f"pattern_names={pattern_names}")
            all_differenced = all_names.difference(pattern_names)
            # print(f"all_differenced={all_differenced}")
            # ignored_names.update(all_differenced)
            # new_set = ignored_names.union(all_differenced)
            # ignored_names.union(all_differenced)
            # print(ignored_names)
            # print(f"new_set={new_set}")
            ignored_names = ignored_names.union(all_differenced)
        # print(ignored_names)
        return ignored_names

    def deploy(self, src_path, dest_path):
        shutil.rmtree(dest_path, ignore_errors=True)
        shutil.copytree(src_path, dest_path, ignore=self._ignore_patterns, dirs_exist_ok=True)
        # for root, dirs, files in os.walk(src_path):
        #     for f in files:
        #         if filter_func(f):
        #             path = os.path.join(root, f)
        # shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
