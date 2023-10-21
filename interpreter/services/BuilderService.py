from interpreter.exceptions.BuildServiceException import BuildServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd


class BuilderService(AbstractExternalShellCmd):

    def build(self, language, builder, folder):

        if language == "java17":
            if builder == "gradle":
                self.shell_command = f"{folder}/gradlew build"
                self.execute(folder)
                if self.returncode > 0:
                    raise BuildServiceException(f"{self.error}")
