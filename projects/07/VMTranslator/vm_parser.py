from symbol_table import vm_command


class VMParser:

    def __init__(self, file):
        self.file = file
        self.position = 0
        self.commands_array = []
        with file.open() as f:
            for l in f:
                clean_command = remove_whitespace(l)
                if len(clean_command) > 0:
                    self.commands_array.append(clean_command)

    def has_more_commands(self) -> bool:
        return self.position < len(self.commands_array)

    def advance(self):
        self.position += 1

    def get_command(self):
        return self.commands_array[self.position].split()

    def arg1(self):
        pass

    def arg2(self):
        pass


def command_type(command):
    commands = command.split()
    return vm_command.get(commands[0])


def remove_whitespace(command: str) -> str:
    no_whitespace_str = command.strip()
    no_whitespace_str = no_whitespace_str.split('/')
    return no_whitespace_str[0].strip()
