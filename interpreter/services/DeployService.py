import fnmatch
import shutil


class DeployService:

    def _ignore_patterns(self, names, exclude=None, pattern=None):
        # print(path)
        ignored_names = set()
        if exclude is not None:
            for pattern in exclude:
                ignored_names.update(fnmatch.filter(names, pattern))

        if pattern is not None:
            all_names = set(names)
            pattern_names = set()
            for pattern in pattern:
                pattern_names.update(fnmatch.filter(names, pattern))
            all_differenced = all_names.difference(pattern_names)
            ignored_names = ignored_names.union(all_differenced)
        return ignored_names

    def deploy(self, src_path, dest_path, exclude=None, pattern=None):
        shutil.rmtree(dest_path, ignore_errors=True)
        shutil.copytree(src_path, dest_path, ignore=(self._ignore_patterns, exclude, pattern), dirs_exist_ok=True)
