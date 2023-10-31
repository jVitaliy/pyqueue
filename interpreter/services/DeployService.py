import fnmatch
import logging
import os
import shutil
from pathlib import Path

import paramiko

from interpreter.exceptions.BuildServiceException import BuildServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd
from interpreter.services.RsyncCmdBuilder import RsyncCmdBuilder


class DeployService(AbstractExternalShellCmd):

    def deploy(self, src_path, dest_path, exclude=None, pattern=None, is_merge=False):
        dest = f"{dest_path}"
        if not is_merge:
            shutil.rmtree(dest, ignore_errors=True)
        src = f"{src_path}"
        Path(dest).mkdir(parents=True, exist_ok=True)

        cd_rsync = RsyncCmdBuilder().cd(src).rsync('lr').pattern(pattern).exclude(exclude).dest_folder(dest).build()
        self.execute(cd_rsync)
        if self.returncode > 0:
            logging.error(f"{cd_rsync}: {self.error}")
            raise BuildServiceException(f"{cd_rsync}: {self.error}")
        else:
            logging.info(f"rsync command {cd_rsync}")
        logging.info(f"deploy from {src} to {dest} with excluding={exclude} and pattern={pattern}")

    def deploy_to_remote(self, ssh_cred, src_path, dest_path, exclude=None, pattern=None, is_merge=False):
        dest = f"{dest_path}"
        logging.info(f"try to open ssh connection with {ssh_cred['host']} {ssh_cred['user']}")
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        # client.load_host_keys('~/.ssh/known_hosts')

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # client.set_missing_host_key_policy(AutoAddPolicy())

        client.connect(ssh_cred['host'], username=ssh_cred['user'], key_filename="/home/vitalii/.ssh/deploy_id_rsa")
        try:
            if not is_merge:

                stdin, stdout, stderr = client.exec_command(f"rm -rd {dest}")
                exit_status = stdout.channel.recv_exit_status()
                if exit_status != 0:
                    logging.error(stderr.read().decode())
                    raise BuildServiceException(stderr.read().decode())
                else:
                    logging.info(f"remove folder <{dest}> on {ssh_cred['host']} : {stderr.read().decode()}")

                stdin.close()
                stdout.close()
                stderr.close()

            src = f"{src_path}"
            # Path(dest).mkdir(parents=True, exist_ok=True)

            stdin, stdout, stderr = client.exec_command(f"mkdir -p {dest}")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                logging.error(stderr.read().decode())
                raise BuildServiceException(stderr.read().decode())
            else:
                logging.info(f"make folder <{dest}> on {ssh_cred['host']} : {stdout.read().decode()}")

            stdin.close()
            stdout.close()
            stderr.close()
            # sftp = client.open_sftp()
            cd_rsync = (RsyncCmdBuilder().cd(src).rsync('lr').pattern(pattern).exclude(exclude)
                        .dest_ssh(ssh_cred['host'], ssh_cred['user']).dest_folder(dest).build())
            logging.info(f"rsync cmd = {cd_rsync}")
            self.execute(cd_rsync)
            if self.returncode > 0:
                logging.error(f"{self.error}")
            # self.walk_through_tree(src, dest, self.remote_copier, exclude=exclude, pattern=pattern, ssh_client=client,
            #                        sftp=sftp)
            logging.info(f"deploy from {src} to {dest} with excluding={exclude} and pattern={pattern}")
        finally:
            client.close()

