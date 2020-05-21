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

    def resetParser(self):
        self.current_location = 0


def getCommandPart(command, command_type):
    if command_type == symbolTable.CommandPart.COMP:
        if command.__contains__('='):
            return command.split('=')[1].split(';')[0]
        else:
            return '0'
    if command_type == symbolTable.CommandPart.DEST:
        if command.__contains__('='):
            return command.split('=')[0]
        else:
            return command.split(';')[0]
    if command_type == symbolTable.CommandPart.JUMP:
        if command.__contains__(';'):
            return command.split(';')[1]
        else:
            return ''


def dest(dest):
    destination = ['0', '0', '0']
    if 'A' in dest:
        destination[0] = '1'
    if 'D' in dest:
        destination[1] = '1'
    if 'M' in dest:
        destination[2] = '1'
    return ''.join(destination)


def comp(comp):
    return symbolTable.instructions_dict.get(comp)


def jump(jump):
    return symbolTable.jump_dict.get(jump)


def symbol(instruction: str):
    return re.split(regex_pattern, instruction)[1]


def commandType(command_string: str):
    if command_string.__contains__('('):
        return symbolTable.CommandType.L_COMMAND
    if command_string.__contains__('@'):
        return symbolTable.CommandType.A_COMMAND
    if command_string.__contains__('='):
        return symbolTable.CommandType.C_COMMAND
