import sys
from antlr4 import *
from interpreter.DescLexer import DescLexer
from interpreter.DescParser import DescParser
from interpreter.DescProcessor import DescProcessor

class TauDeployScriptInterpreter:

    def get_tree_and_parser(self, filename):
        input_stream = FileStream(filename)
        lexer = DescLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DescParser(stream)
        return [parser, parser.script()]

    def get_processor(self, parser, tree, branch, project_name, repo_path=None):
        if parser.getNumberOfSyntaxErrors() > 0:
            print("syntax errors")
            return None
        else:
            processor = DescProcessor(branch, project_name, repo_path=repo_path)
            walker = ParseTreeWalker()
            walker.walk(processor, tree)
            return processor

    def start_walking_with_processor(self, tree, processor):
        walker = ParseTreeWalker()
        walker.walk(processor, tree)

    def start_walking(self, script_filename, branch, project_name, repo_path=None):
        tree_and_parser = self.get_tree_and_parser(script_filename)
        processor = self.get_processor(tree_and_parser[0], tree_and_parser[1], branch, project_name, repo_path=repo_path)
        self.start_walking_with_processor(tree_and_parser[1], processor)

