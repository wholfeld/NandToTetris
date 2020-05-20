import re
import symbolTable

delimiters = "@", "//", "=", ";", "(", ")", " ",
regex_pattern = '|'.join(map(re.escape, delimiters))


class parser:

    def __init__(self, file):
        print(file)
        self.file = file
        self.commands = []
        self.current_location = 0
        self.current_command = ''
        with file.open() as f:
            for x in f:
                # pass

                no_whitespace_str = x.strip()
                for char in no_whitespace_str:
                    if char == "/":
                        break
                    if char == "@" or char == "=" or char == ";":
                        no_comments = no_whitespace_str.split('/')
                        self.commands.append(no_comments[0])
        print(self.commands)

    def hasMoreCommands(self) -> bool:
        return len(self.commands) < self.current_location

    def advance(self):
        self.current_location += 1

    def symbol(self):
        pass

    def dest(self):
        pass

    def comp(self):
        pass

    def jump(self):
        pass

    def resetParser(self):
        self.current_location = 0


def commandType(command_string: str):
    if command_string.__contains__('('):
        return symbolTable.commands.L_COMMAND
    if command_string.__contains__('@'):
        return symbolTable.commands.A_COMMAND
    if command_string.__contains__('='):
        return symbolTable.commands.C_COMMAND
