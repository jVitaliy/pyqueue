import fnmatch
import logging
import os
import shutil
from pathlib import Path


class DeployService:

    def _ignore_patterns(self, names, exclude=None, patterns=None):
        ignored_names = set()
        if exclude is not None:
            for pattern in exclude:
                ignored_names.update(fnmatch.filter(names, pattern))
        if patterns is not None:
            all_names = set(names)
            pattern_names = set()
            for pattern in patterns:
                pattern_names.update(fnmatch.filter(all_names, pattern))
            all_names.difference_update(pattern_names)
            ignored_names = ignored_names.union(all_names)
        return ignored_names

    def deploy(self, src_path, dest_path, exclude=None, pattern=None, is_merge=False):
        dest = f"{dest_path}"
        if not is_merge:
            shutil.rmtree(dest, ignore_errors=True)
        src = f"{src_path}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        self.walk_through_tree(src, dest, exclude=exclude, pattern=pattern)
        logging.info(f"deploy from {src} to {dest} with excluding={exclude} and pattern={pattern}")

    def walk_through_tree(self, folder_src, folder_dest, exclude=None, pattern=None):
        for root, dirs, files in os.walk(folder_src, topdown=False):
            dirs_filtered = self.filter_names(dirs, exclude=exclude, pattern=pattern)
            for df in dirs_filtered:
                dirs.remove(df)
            files_filtered = self.filter_names(files, exclude=exclude, pattern=pattern)
            related_path = root.replace(folder_src, "")
            for file in files_filtered:
                os.makedirs(os.path.dirname(f"{folder_dest}{related_path}/"), exist_ok=True)
                shutil.copyfile(f"{root}/{file}", f"{folder_dest}{related_path}/{file}")
                logging.debug(f"copied from {root}/{file} to {folder_dest}{related_path}/{file}")


    def filter_names(self, names, exclude=None, pattern=None):
        names_excluded = self._ignore_patterns(names, exclude=exclude, patterns=pattern)

        names_set = set(names)
        a = names_set.difference(names_excluded)
        return a

