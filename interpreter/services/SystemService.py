from interpreter.exceptions.SystemServiceException import SystemServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd


class SystemService(AbstractExternalShellCmd):

    def startService(self, service_name):
        self.shell_command = f"sudo /usr/bin/systemctl start {service_name}"
        self.execute()
        if self.returncode > 0:
            raise SystemServiceException(self.error)

    def stopService(self, service_name):
        self.shell_command = f"sudo /usr/bin/systemctl stop {service_name}"
        self.execute()
        if self.returncode > 0:
            raise SystemServiceException(self.error)
