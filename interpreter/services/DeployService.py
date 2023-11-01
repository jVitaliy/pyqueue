import logging
import shutil
from pathlib import Path

import paramiko

from interpreter.exceptions.BuildServiceException import BuildServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd
from interpreter.services.DeployParameters import DeployParameters
from interpreter.services.RsyncCmdBuilder import RsyncCmdBuilder
from interpreter.services.TarCmdBuilder import TarCmdBuilder


class DeployService(AbstractExternalShellCmd):

    def deploy(self, deploy_param: DeployParameters):
        dest = f"{deploy_param.dest_path}"
        if not deploy_param.is_merge:
            shutil.rmtree(dest, ignore_errors=True)
        src = f"{deploy_param.src_path}"
        Path(dest).mkdir(parents=True, exist_ok=True)

        cd_rsync = RsyncCmdBuilder().cd(src).rsync('lr').pattern(deploy_param.pattern).exclude(deploy_param.exclude).dest_folder(dest).build()
        self.execute(cd_rsync)
        if self.returncode > 0:
            logging.error(f"{cd_rsync}: {self.error}")
            raise BuildServiceException(f"{cd_rsync}: {self.error}")
        else:
            logging.info(f"rsync command {cd_rsync}")
        logging.info(f"deploy from {src} to {dest} with excluding={deploy_param.exclude} and pattern={deploy_param.pattern}")

    def execute_remote(self, client, cmd, normal_msg):
        stdin, stdout, stderr = client.exec_command(cmd)
        exit_status = stdout.channel.recv_exit_status()
        if exit_status != 0:
            logging.error(stderr.read().decode())
            raise BuildServiceException(stderr.read().decode())
        else:
            logging.info(f"{normal_msg} : {stdout.read().decode()}")
        stdin.close()
        stdout.close()
        stderr.close()

    def create_client(self, ssh_cred):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        # client.load_host_keys('~/.ssh/known_hosts')

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # client.set_missing_host_key_policy(AutoAddPolicy())

        client.connect(ssh_cred['host'], username=ssh_cred['user'], key_filename=ssh_cred['key'])
        return client

    def deploy_to_remote(self, ssh_cred, deploy_param: DeployParameters):
        dest = f"{deploy_param.dest_path}"
        logging.info(f"try to open ssh connection with {ssh_cred['host']} {ssh_cred['user']}")
        client = self.create_client(ssh_cred)
        try:
            if not deploy_param.is_merge:
                self.execute_remote(client, f"rm -rd {dest}", f"remove folder <{dest}> on {ssh_cred['host']}")

            src = f"{deploy_param.src_path}"
            self.execute_remote(client, f"mkdir -p {dest}", f"make folder <{dest}> on {ssh_cred['host']}")
            # sftp = client.open_sftp()
            cd_rsync = (RsyncCmdBuilder().cd(src).rsync('lr').pattern(deploy_param.pattern).exclude(deploy_param.exclude)
                        .dest_ssh(ssh_cred['host'], ssh_cred['user']).dest_folder(dest).build())
            logging.info(f"rsync cmd = {cd_rsync}")
            self.execute(cd_rsync)
            if self.returncode > 0:
                logging.error(f"{self.error}")
            # self.walk_through_tree(src, dest, self.remote_copier, exclude=exclude, pattern=pattern, ssh_client=client,
            #                        sftp=sftp)
            logging.info(f"deploy from {src} to {dest} with excluding={deploy_param.exclude} and pattern={deploy_param.pattern}")
        finally:
            client.close()

    def deploy_archived_to_remote(self, ssh_cred, deploy_param: DeployParameters):
        if deploy_param.exclude:
            deploy_param.exclude.append(f"{deploy_param.project_name}.tar")

        tar_cmd = (TarCmdBuilder()
                   .cd(deploy_param.src_path)
                   .tar(deploy_param.project_name)
                   .pattern(deploy_param.pattern)
                   .exclude(deploy_param.exclude)
                   .archive()
                   .build())
        self.execute(tar_cmd)
        if self.returncode > 0:
            logging.error(f"{self.error}")
        logging.info(f"archiving with {tar_cmd}")
        remote_param = DeployParameters(src_path=deploy_param.src_path, dest_path=deploy_param.dest_path,
                                        project_name=deploy_param.project_name, exclude=None,
                                        pattern=[f"{deploy_param.project_name}.tar"], is_merge=True)
        self.deploy_to_remote(ssh_cred, remote_param)

        untar_cmd = (TarCmdBuilder()
                     .cd(deploy_param.dest_path)
                     .tar(deploy_param.project_name)
                     .pattern([f"{deploy_param.project_name}.tar"])
                     .exclude(None)
                     .unarchive()
                     .build())
        logging.info(f"archiving with {untar_cmd}")
        client = self.create_client(ssh_cred)

        try:
            self.execute_remote(client, untar_cmd, "untar on remote machine")
            self.execute_remote(client, f"rm {deploy_param.dest_path}/{deploy_param.project_name}.tar",
                                f"remove tar {deploy_param.project_name}.tar")
        finally:
            client.close()

