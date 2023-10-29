import subprocess


class AbstractExternalShellCmd:

    def __init__(self):
        # self.shell_command = None
        self.output = None
        self.error = None
        self.returncode = None

    def execute(self, command, working_folder=None):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_folder)
        self.output = result.stdout
        self.error = result.stderr
        self.returncode = result.returncode

        # print("Output:", self.output)
        # print("Error:", self.error)
        # print("Return Code:", self.returncode)
