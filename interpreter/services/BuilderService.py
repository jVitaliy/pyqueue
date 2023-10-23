import logging

from interpreter.exceptions.BuildServiceException import BuildServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd


class BuilderService(AbstractExternalShellCmd):

    def build(self, language, builder, folder):

        if language == "java17" and builder == "gradle":
            self.java17GradleBuild(folder)
        elif language == "next" and builder == "npm":
            self.nextNpmBuild(folder)

    def java17GradleBuild(self, folder):
        self.shell_command = f"{folder}/gradlew build"
        self.execute(folder)
        if self.returncode > 0:
            raise BuildServiceException(f"Java17/Gradle error - {self.error}")
        logging.info("build Java17/Gradle succeeded")

    def nextNpmBuild(self, folder):
        self.shell_command = "/usr/bin/npm install"
        self.execute(folder)
        self.shell_command = "/usr/bin/npm run build"
        self.execute(folder)
        if self.returncode > 0:
            raise BuildServiceException(f"NEST/npm error - {self.error}")
        logging.info("build NEST/npm succeeded")

