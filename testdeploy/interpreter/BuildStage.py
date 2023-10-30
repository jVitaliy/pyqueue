from interpreter.DescParser import DescParser
from interpreter.PreBuildStage import PreBuildStage


class BuildStage(PreBuildStage):
    _LANGUAGE = 'language'
    _BUILDER = 'builder'

    def enterBuildProject(self, ctx: DescParser.BuildProjectContext):
        self._builder_data = dict()

    def exitJavaBuild(self, ctx: DescParser.JavaBuildContext):
        self._builder_data[self._LANGUAGE] = ctx.JAVA17().getText()
        self._builder_data[self._BUILDER] = ctx.GRADLE().getText() if ctx.MAVEN() is None else ctx.MAVEN().getText()

    def exitNextBuild(self, ctx: DescParser.NextBuildContext):
        self._builder_data[self._LANGUAGE] = ctx.NEXT().getText()
        self._builder_data[self._BUILDER] = ctx.NPM().getText()

    def exitPythonBuild(self, ctx: DescParser.PythonBuildContext):
        self._builder_data[self._LANGUAGE] = ctx.PYTHON39().getText()
        self._builder_data[self._BUILDER] = ctx.INSTALL().getText()


    def exitBuildProject(self, ctx: DescParser.BuildProjectContext):
        if self._current_branch is None:
            return
        current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        repo_name = current_repo_data['project_name']
        folder = f"{current_repo_data['tmp_folder']}/{repo_name}" if ctx.buildDir() is None \
            else ctx.buildDir().buildFolder().getText()
        if self._LANGUAGE in self._builder_data.keys() and self._BUILDER in self._builder_data.keys():
            self._builder_service.build(self._builder_data[self._LANGUAGE], self._builder_data[self._BUILDER], folder)
