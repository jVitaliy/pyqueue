import logging

from interpreter.exceptions.BuildServiceException import BuildServiceException
from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd


class BuilderService(AbstractExternalShellCmd):
    JAVA17 = 'java17'
    MAVEN = 'maven'
    GRADLE = 'gradle'
    NEXT = 'next'
    NPM = 'npm'
    PYTHON39 = 'python39'
    INSTALL = 'install'

    def build(self, language, builder, folder):

        if language == self.JAVA17 and builder == self.GRADLE:
            self.java17GradleBuild(folder)
        elif language == self.NEXT and builder == self.NPM:
            self.nextNpmBuild(folder)
        elif language == self.PYTHON39 and builder == self.INSTALL:
            self.python39Install(folder)

    def java17GradleBuild(self, folder):
        self.execute(f"{folder}/gradlew build", working_folder=folder)
        if self.returncode > 0:
            raise BuildServiceException(f"{self.JAVA17}/{self.GRADLE} error - {self.error}")
        logging.info(f"build {self.JAVA17}/{self.GRADLE} succeeded")

    def nextNpmBuild(self, folder):
        self.execute("/usr/bin/npm install", working_folder=folder)
        self.execute("/usr/bin/npm run build", working_folder=folder)
        self.execute("/usr/bin/chmod 0775 .next", working_folder=folder)
        self.execute("/usr/bin/chmod 0775 node_modules", working_folder=folder)
        if self.returncode > 0:
            raise BuildServiceException(f"{self.NEXT}/{self.NPM} error - {self.error}")
        logging.info(f"build {self.NEXT}/{self.NPM} succeeded")

    def python39Install(self, folder):
        self.execute("/usr/bin/python3.9 -m venv venv", working_folder=folder)
        logging.info(f"{self.output}")
        self.execute('source "$(pwd)/venv/bin/activate" && "$(pwd)/venv/bin/pip3.9" install -r requirements.txt && deactivate', working_folder=folder)
        logging.info(f"{self.output}")
        if self.returncode > 0:
            raise BuildServiceException(f"{self.PYTHON39}/{self.INSTALL} error - {self.error}")
        logging.info(f"build {self.PYTHON39}/{self.INSTALL} succeeded")

