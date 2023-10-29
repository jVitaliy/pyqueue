import logging

import paramiko

from interpreter.exceptions.SystemServiceException import SystemServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd


class SystemService(AbstractExternalShellCmd):

    def startService(self, service_name):
        self.execute(f"sudo /usr/bin/systemctl start {service_name}")
        if self.returncode > 0:
            raise SystemServiceException(self.error)

    def stopService(self, service_name):
        self.execute(f"sudo /usr/bin/systemctl stop {service_name}")
        if self.returncode > 0:
            raise SystemServiceException(self.error)

    def sshClientInit(self, credentials):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(credentials['host'], username=credentials['user'], password=credentials['password'])
        return client

    def startServiceRemote(self, credentials, service_name):
        client = self.sshClientInit(credentials)
        try:
            stdin, stdout, stderr = client.exec_command(f"sudo /usr/bin/systemctl start {service_name}")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                logging.error(stderr.read().decode())
                stdin.close()
                stdout.close()
                stderr.close()
                raise SystemServiceException(self.error)
            stdin.close()
            stdout.close()
            stderr.close()
        finally:
            client.close()

    def stopServiceRemote(self, credentials, service_name):
        client = self.sshClientInit(credentials)
        try:
            stdin, stdout, stderr = client.exec_command(f"sudo /usr/bin/systemctl stop {service_name}")
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                logging.error(stderr.read().decode())
                err = SystemServiceException(stderr.read().decode())
                stdin.close()
                stdout.close()
                stderr.close()
                raise err
            stdin.close()
            stdout.close()
            stderr.close()
        finally:
            client.close()
