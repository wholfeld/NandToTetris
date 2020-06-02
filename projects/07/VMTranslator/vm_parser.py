
class VMTranslator:

    def __init__(self, file):
        pass

    def has_more_commands(self) -> bool:
        pass

    def advance(self):
        pass

    def arg1(self):
        pass

    def arg2(self):
        pass

def command_type(command):
    pass

def remove_whitespace(command: str) -> str:
    no_whitespace_str = command.strip()
    no_whitespace_str = no_whitespace_str.split('/')
    return no_whitespace_str[0].strip()
