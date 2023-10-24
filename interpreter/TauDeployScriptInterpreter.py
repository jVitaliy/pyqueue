import logging

from antlr4 import *

from interpreter.DescErrorListener import DescErrorListener
from interpreter.DescLexer import DescLexer
from interpreter.DescParser import DescParser
from interpreter.DescProcessor import DescProcessor
from interpreter.exceptions.ParseException import ParseException


class TauDeployScriptInterpreter:

    def __init__(self):
        self.error_listener = DescErrorListener()

    def get_tree_and_parser(self, filename):
        input_stream = FileStream(filename)
        lexer = DescLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DescParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)
        tree = parser.script()
        if parser.getNumberOfSyntaxErrors() > 0:
            logging.error(self.error_listener.errors)
            # print(parser.())
            # print(self.error_listener.errors)
            raise ParseException(self.error_listener.errors)
        return [parser, tree]

    def get_processor(self, parser, tree, branch, repo_path=None):
        if parser.getNumberOfSyntaxErrors() > 0:
            # logging.error(.getErr())
            # print(parser.())
            # print(self.error_listener.errors)
            raise ParseException(self.error_listener.errors)
            # return None
        else:
            processor = DescProcessor(branch, repo_path=repo_path)
            walker = ParseTreeWalker()
            walker.walk(processor, tree)
            return processor

    def start_walking_with_processor(self, tree, processor):
        walker = ParseTreeWalker()
        walker.walk(processor, tree)

    def start_walking(self, script_filename, branch, repo_path=None):
        tree_and_parser = self.get_tree_and_parser(script_filename)
        self.get_processor(tree_and_parser[0], tree_and_parser[1], branch, repo_path=repo_path)
        # self.start_walking_with_processor(tree_and_parser[1], processor)

