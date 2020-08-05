from symbol_table import vm_command, command_types, math_commands, two_operands, comparative, location_table


class VMCodewriter:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = open(f'{file_name}', 'w')
        self.jump_count = 0

    def set_file_name(self: object, file_name: str):
        pass

    def write_command(self, commands: []):
        # commands = command.split()
        command_type = vm_command.get(commands[0])
        asm_commands = ''
        if command_type == command_types.C_ARITHMETIC:
            arithmetic_command = commands[0]
            if arithmetic_command in two_operands:
                asm_commands = write_two_operand_command(arithmetic_command)
            elif arithmetic_command in comparative:
                asm_commands = write_comparative(commands[0], self.jump_count)
                self.jump_count += 1
            else:
                asm_commands = write_one_operand_command(commands[0])

        if command_type == command_types.C_PUSH or \
           command_type == command_types.C_POP:
            asm_commands = write_push_pop(commands)

        # write asm_commands to file
        self.file.write(asm_commands)

    def close(self):
        self.file.close()


def write_arithmetic(commands: []):
    arithmetic_command = commands[0]
    if arithmetic_command in two_operands:
        write_two_operand_command(arithmetic_command)
    elif arithmetic_command in comparative:
        write_comparative(commands[0])
    else:
        write_one_operand_command(commands[0])


def write_one_operand_command(command):
    arithmetic_symbol = math_commands[command]
    return f''' // Writing single operand {command}
@SP
A=M-1
M={arithmetic_symbol}M
'''


def write_comparative(command, iteration):
    assembler_command = math_commands[command]
    return f''' // Writing comparative command {command}
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMPTRUE{iteration}
D;{assembler_command}
@SP
A=M
M=0
@END{iteration}
0;JMP
(JUMPTRUE{iteration})
@SP
A=M
M=-1
(END{iteration})
@SP
M=M+1

'''


def write_two_operand_command(arithmetic_command):
    arithmetic_symbol = math_commands[arithmetic_command]
    return f''' // Writing arithmetic command {arithmetic_command}
@SP
A=M-1
D=M
A=A-1
M=M{arithmetic_symbol}D
D=A+1
@SP
M=D

'''


def write_push_pop(commands: []):
    if vm_command.get(commands[0]) == command_types.C_PUSH:
        return write_push(commands)
    else:
        return write_pop(commands)


def write_push(commands: []):
    location = ''
    if commands[1] == 'constant':
        location = f'''@{commands[2]}
D=A'''
    elif commands[1] == 'temp' or commands[1] == 'static' or commands[1] == 'pointer':
        array_num = int(location_table.get(commands[1])) + int(commands[2])
        location = f'''@{array_num}
D=M'''
    else:
        location = f'''@{location_table.get(commands[1])}
D=M
@{commands[2]}
A=D+A
D=M'''

    return f'''// Writing {commands[0]} from {commands[1]} {commands[2]}
{location}
@SP
A=M
M=D
@SP
M=M+1

'''


def write_pop(commands: []):
    # pop local 0
    # pop that 5
    pop_type = commands[1]
    if pop_type == 'static' or pop_type == 'temp' or pop_type == 'pointer':
        array_num = int(location_table.get(commands[1])) + int(commands[2])
        return f'''// Writing {commands[0]} to {commands[1]} {commands[2]}
@SP
AM=M-1
D=M
@{array_num}
M=D

'''
    else:
        return f'''// Writing {commands[0]} to {commands[1]} {commands[2]}
// go to location to deposit
@{location_table.get(commands[1])}
D=M
@{commands[2]}
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

'''
