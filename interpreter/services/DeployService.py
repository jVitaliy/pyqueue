import fnmatch
import logging
import os
import shutil
from pathlib import Path

import paramiko


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
        self.walk_through_tree(src, dest, self.local_copier, exclude=exclude, pattern=pattern)
        logging.info(f"deploy from {src} to {dest} with excluding={exclude} and pattern={pattern}")

    def deploy_to_remote(self, ssh_cred, src_path, dest_path, exclude=None, pattern=None, is_merge=False):
        dest = f"{dest_path}"
        logging.info(f"try to open ssh connection with {ssh_cred['host']} {ssh_cred['user']} {ssh_cred['password']}")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # client.load_system_host_keys()
        # client.load_host_keys('~/.ssh/known_hosts')
        # client.set_missing_host_key_policy(AutoAddPolicy())

        client.connect(ssh_cred['host'], username=ssh_cred['user'], password=ssh_cred['password'])
        try:
            if not is_merge:
                stdin, stdout, stderr = client.exec_command(f"rm -rd {dest}")
                stdin.close()
                stdout.close()
                stderr.close()

            src = f"{src_path}"
            # Path(dest).mkdir(parents=True, exist_ok=True)

            stdin, stdout, stderr = client.exec_command(f"mkdir -p {dest}")
            stdin.close()
            stdout.close()
            stderr.close()
            sftp = client.open_sftp()
            self.walk_through_tree(src, dest, self.remote_copier, exclude=exclude, pattern=pattern, ssh_client=client,
                                   sftp=sftp)
            logging.info(f"deploy from {src} to {dest} with excluding={exclude} and pattern={pattern}")
        finally:
            client.close()

    def walk_through_tree(self, folder_src, folder_dest, copier, exclude=None, pattern=None, ssh_client=None, sftp=None):
        # print(f"folder_src = {folder_src} / folder_dest = {folder_dest}")
        for root, dirs, files in os.walk(folder_src, topdown=True, followlinks=False):
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
        shutil.copymode(f"{root}", f"{folder_dest}{related_path}")
        shutil.copyfile(f"{root}/{file}", f"{folder_dest}{related_path}/{file}", follow_symlinks=False)
        shutil.copymode(f"{root}/{file}", f"{folder_dest}{related_path}/{file}")

    def remote_copier(self, client, sftp, root, file, folder_dest, related_path):
        stdin, stdout, stderr = client.exec_command(f"mkdir -p {folder_dest}{related_path}")
        exit_status = stdout.channel.recv_exit_status()
        if exit_status != 0:
            logging.error(stderr.read().decode())
        sftp.put(f"{root}/{file}", f"{folder_dest}{related_path}/{file}")
        stdin.close()
        stdout.close()
        stderr.close()

    def filter_names(self, names, exclude=None, pattern=None):
        names_excluded = self._ignore_patterns(names, exclude=exclude, patterns=pattern)
        # print(f"excluded={names_excluded}")
        # names_set = set(names)
        # a = names_set.difference(names_excluded)
        # print(f"a={a}")
        # return a
        return names_excluded
