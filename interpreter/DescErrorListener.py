from antlr4.error import ErrorListener


class DescErrorListener(ErrorListener.ErrorListener):
    def __init__(self):
        self.errors = list()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line ({line},{column}): {msg}")
