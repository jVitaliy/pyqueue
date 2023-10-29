import fnmatch
import logging
import os
import shutil
from pathlib import Path

import paramiko


class ConfigService:

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

    def apply(self, repo_host, repo_path, branch, src_path, dest_path, exclude=None, pattern=None, git_service=None):
        tmp_folder = git_service.clone(repo_path, repo_host)
        project_name = git_service.getRepoName(repo_path)
        git_service.checkout(branch, f"{tmp_folder}/{project_name}")
        dest = f"{dest_path}"
        src = f"{tmp_folder}/{project_name}" if src_path is None else f"{tmp_folder}/{project_name}/{src_path}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        self.walk_through_tree(src, dest, self.local_copier, exclude=exclude, pattern=pattern)
        git_service.removeFolder(tmp_folder)
        logging.info(f"deploy from {src} to {dest} with excluding={exclude} and pattern={pattern}")


    def walk_through_tree(self, folder_src, folder_dest, copier, exclude=None, pattern=None, ssh_client=None, sftp=None):
        # print(f"folder_src = {folder_src} / folder_dest = {folder_dest}")
        for root, dirs, files in os.walk(folder_src, topdown=True):
            # print(f"root = {root} / dirs = {dirs}")
            dirs_excluded = self.filter_names(dirs, exclude=exclude, pattern=pattern)
            # print(f"dirs_excluded = {dirs_excluded}")
            for df in dirs_excluded:
                dirs.remove(df)
            files_excluded = self.filter_names(files, exclude=exclude, pattern=pattern)

            files_filtered = set(files).difference(files_excluded)
            # print(f"files_filtered={files_filtered}")
            related_path = root.replace(folder_src, "")
            for file in files_filtered:
                if ssh_client is None:
                    copier(root, file, folder_dest, related_path)
                else:
                    copier(ssh_client, sftp, root, file, folder_dest, related_path)
                logging.debug(f"copied from {root}/{file} to {folder_dest}{related_path}/{file}")

    def local_copier(self, root, file, folder_dest, related_path):
        os.makedirs(os.path.dirname(f"{folder_dest}{related_path}/"), exist_ok=True)
        shutil.copyfile(f"{root}/{file}", f"{folder_dest}{related_path}/{file}")


    def filter_names(self, names, exclude=None, pattern=None):
        names_excluded = self._ignore_patterns(names, exclude=exclude, patterns=pattern)
        # print(f"excluded={names_excluded}")
        # names_set = set(names)
        # a = names_set.difference(names_excluded)
        # print(f"a={a}")
        # return a
        return names_excluded
