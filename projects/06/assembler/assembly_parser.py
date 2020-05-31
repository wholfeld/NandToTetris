import re
import symbol_table

delimiters = "@", "//", "=", ";", "(", ")", " ",
regex_pattern = '|'.join(map(re.escape, delimiters))


class Parser:

    def __init__(self, file):
        print(file)
        self.file = file
        self.commands = []
        self.current_location = 0
        self.current_line = 1
        self.current_command = ''
        with file.open() as f:
            for x in f:

                no_whitespace_str = x.strip()
                for char in no_whitespace_str:
                    if char == "/":
                        break
                    if char == "@" or char == "=" or char == ";" or char == "(":
                        no_comments = no_whitespace_str.split('/')
                        c = no_comments[0].strip()
                        self.commands.append(c)
        self.current_command = self.commands[0]

    def has_more_commands(self) -> bool:
        return self.current_location < len(self.commands)

    def advance(self):
        self.current_location += 1
        if self.has_more_commands():
            self.current_command = self.commands[self.current_location]
            if command_type(self.current_command) != symbol_table.CommandType.L_COMMAND:
                self.current_line += 1

    def get_current_command(self):
        return self.current_command

    def get_current_line(self):
        return self.current_location

    def reset_parser(self):
        self.current_location = 0
        self.current_command = self.commands[0]


def get_command_part(command, command_type):
    if command_type == symbol_table.CommandPart.COMP:
        if command.__contains__('='):
            return command.split('=')[1].split(';')[0]
        else:
            return '0'
    if command_type == symbol_table.CommandPart.DEST:
        if command.__contains__('='):
            return command.split('=')[0]
        else:
            return command.split(';')[0]
    if command_type == symbol_table.CommandPart.JUMP:
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
    return symbol_table.instructions_dict.get(comp)


def jump(jump):
    return symbol_table.jump_dict.get(jump)


def symbol(instruction: str):
    return re.split(regex_pattern, instruction)[1]


def command_type(command_string: str):
    if command_string.__contains__('('):
        return symbol_table.CommandType.L_COMMAND
    if command_string.__contains__('@'):
        return symbol_table.CommandType.A_COMMAND
    if command_string.__contains__('=') or command_string.__contains__(';'):
        return symbol_table.CommandType.C_COMMAND
