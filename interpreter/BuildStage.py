from interpreter.DescParser import DescParser
from interpreter.PreBuildStage import PreBuildStage


class BuildStage(PreBuildStage):

    def enterBuildProject(self, ctx:DescParser.BuildProjectContext):
        self._builder_data = dict()

    def exitProjectLanguage(self, ctx:DescParser.ProjectLanguageContext):
        if ctx.JAVA17() is not None:
            self._builder_data['language'] = "java17"
        elif ctx.NEXT() is not None:
            self._builder_data['language'] = "next"
        elif ctx.PYTHON39() is not None:
            self._builder_data['language'] = "python39"

    def exitBuilderType(self, ctx:DescParser.BuilderTypeContext):
        if ctx.MAVEN() is not None:
            self._builder_data['builder'] = "maven"
        elif ctx.GRADLE() is not None:
            self._builder_data['builder'] = "gradle"

    def exitBuildProject(self, ctx:DescParser.BuildProjectContext):
        current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        if 'language' in self._builder_data.keys() and 'builder' in self._builder_data.keys():
            self._builder_service.build(self._builder_data['language'], self._builder_data['builder'],
                                        current_repo_data['tmp_folder'])
