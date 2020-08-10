from symbol_table import vm_command, command_types, math_commands, two_operands, comparative, location_table


class VMCodewriter:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = open(f'{file_name}', 'w')
        self.class_name = ''
        self.jump_count = 0

    def set_class_name(self: object, class_name: str):
        self.class_name = class_name

    def write_command(self, commands: []):
        # commands = command.split()
        command_type = vm_command.get(commands[0])
        asm_commands = ''
        class_name = self.class_name.name.split('/')[-1]
        class_name = class_name.split('.')[0]
        print(commands)
        if command_type == command_types.C_ARITHMETIC:
            arithmetic_command = commands[0]
            if arithmetic_command in two_operands:
                asm_commands = write_two_operand_command(arithmetic_command)
            elif arithmetic_command in comparative:
                asm_commands = write_comparative(commands[0], self.jump_count)
                self.jump_count += 1
            else:
                asm_commands = write_one_operand_command(commands[0])
        elif command_type == command_types.C_PUSH:
            asm_commands = write_push(commands, class_name)
        elif command_type == command_types.C_POP:
            asm_commands = write_pop(commands, class_name)
        elif command_type == command_types.C_LABEL:
            asm_commands = write_label(commands[1])
        elif command_type == command_types.C_GOTO:
            asm_commands = write_goto(commands[1])
        elif command_type == command_types.C_IF:
            asm_commands = write_if(commands[1])
        elif command_type == command_types.C_FUNCTION:
            if commands[1] == 'Sys.init':
                asm_commands = write_init()
            else:
                asm_commands = write_function(commands[1], int(commands[2]))
        elif command_type == command_types.C_RETURN:
            asm_commands = write_return()
        elif command_type == command_types.C_CALL:
            asm_commands = write_call(commands[1], int(commands[2]))

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


def write_push(commands: [], file_name: str):
    location = ''
    if commands[1] == 'constant':
        location = f'''@{commands[2]}
D=A'''
    elif commands[1] == 'temp' or commands[1] == 'pointer':
        array_num = int(location_table.get(commands[1])) + int(commands[2])
        location = f'''@{array_num}
D=M'''
    elif commands[1] == 'static':
        location = f'''@{file_name}.{commands[2]}
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


def write_pop(commands: [], file_name: str):
    # pop local 0
    # pop that 5
    pop_type = commands[1]
    if pop_type == 'static' or pop_type == 'temp' or pop_type == 'pointer':
        if pop_type == 'static':
            array_num = f'{file_name}.{commands[2]}'
        else:
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
@{location_table.get(commands[1])}
D=M
@{commands[2]}
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

'''


# Writes assembly code that effects the VM initialization, also called bootstrap code. 
# This code must be placed at the beginning of the output file.
def write_init():
    return f'''//init function
@256
D=A
@SP
M=D
// push return address
{write_push(['push', 'constant', '256'], '')}
// Save LCL of the calling function
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save ARG of the calling function
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THIS of the calling function
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THAT of the calling function
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Repostion ARG for current args
@SP
D=M
@5
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
'''


# Writes assembly code that effects the label command.
def write_label(label_name: str):
    return f'''// create label {label_name}
({label_name})

'''


# Writes assembly code that effects the goto command.
def write_goto(label_name: str):
    return f'''// goto {label_name}
@{label_name}
0;JMP

'''


# Writes assembly code that effects the if-goto command.
def write_if(label_name: str):
    return f'''// if goto {label_name}
@SP
AM=M-1
D=M
@{label_name}
D;JNE

'''


# Write assembly code that effects the call command.
def write_call(function_name: str, num_args: int):
    return f'''// Calling function {function_name}
// push return address
{write_push(['push', 'constant', f'{function_name}$return_address'], '')}
// Save LCL of the calling function
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save ARG of the calling function
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THIS of the calling function
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THAT of the calling function
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Repostion ARG for current args
@SP
D=M
@{num_args + 5}
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Transfer control
@{function_name}
0;JMP
//return label
({function_name}$return_address)
'''


# Writes assembly code that effects the return commands
def write_return():
    return f'''// writing return
//setup local as frame as R13
@LCL
D=M
@R13
M=D
//put return address in variable
@5
A=D-A
D=M
@R14
M=D
//Reposition the return value for the caller
@SP
A=M-1
D=M
@ARG
A=M
M=D
//Restore SP of the caller
D=A+1
@SP
M=D
//Restore THAT of the caller
@R13
A=M-1
D=M
@THAT
M=D
//Restore THIS of the caller
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
//Restore ARG of the caller
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
//Restore LCL of the caller
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
//Goto return-address (in the caller's code)
@R14
A=M
0;JMP
'''


# Writes assembly code that effects the function command.
def write_function(function_name: str, num_locals: int):
    return f'''// function {function_name} with {num_locals} locals
({function_name})
@{num_locals}
D=A
@R13
M=D
({function_name}$setup_locals)
@R13
MD=M-1
@{function_name}$locals_done
D;JLT
{write_push(['push', 'constant', '0'], '')}
@{function_name}$setup_locals
D;JMP
({function_name}$locals_done)
'''
