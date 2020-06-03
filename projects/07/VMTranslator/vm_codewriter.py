from symbol_table import vm_command, command_types

class VMCodewriter:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def set_file_name(self: object, file_name: str):
        pass

    def write_command(self: object, command: str):
        commands = command.split()
        command_type = vm_command.get(commands[0])
        asm_commands = ''
        
        if command_type == command_types.C_ARITHMETIC:
            asm_commands = write_arithmetic(commands)

        if command_type == command_types.C_PUSH or \
           command_type == command_types.C_POP:
            asm_commands = write_push_pop(commands)
        
        # write asm_commands to file



def write_arithmetic(commands: []):
    pass


def write_push_pop(command: str):
    pass
