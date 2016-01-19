class InvalidGameCommandError(Exception):
    def __init__(self, commandName, message, inner_exception = None):
        self.commandName = commandName
        self.message = message
        self.inner_exception = inner_exception
