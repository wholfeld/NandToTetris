import symbol_table

class BinaryGenerator():
    def __init__(self):
        self.openfile = 1


def get_address(address: str) -> str:
    address_int = int(address.replace('@', ''))
    bin_string = '{:016b}'.format(address_int)
    return bin_string


def get_instruction_binary(instruction: str) -> str:
    binary_start = '111'
    binary_comp = get_computation(instruction)
    binary_dest = get_destination(instruction)
    binary_jump = get_jump(instruction)
    return binary_start + binary_comp + binary_dest + binary_jump


def get_destination(instruction_asm: str) -> str:
    dest_str = ''
    if '=' in instruction_asm:
        dest_str = instruction_asm.split('=')[0]
    destination = ['0', '0', '0']
    if 'A' in dest_str:
        destination[0] = '1'
    if 'D' in dest_str:
        destination[1] = '1'
    if 'M' in dest_str:
        destination[2] = '1'
    return ''.join(destination)


def get_computation(instruction_asm: str) -> str:
    comp = instruction_asm.split(';')[0]
    binary = ''
    if '=' in comp:
        comp = comp.split('=')[1]
    if 'M' in comp:
        binary = '1'
    else:
        binary = '0'
    comp = comp.replace('M', 'A')
    binary2 = symbol_table.instructions_dict.get(comp)
    binary = binary + binary2
    return binary


def get_jump(instruction_asm: str) -> str:
    if ';' in instruction_asm:
        jump_asm = instruction_asm.split(';')[1]
        return symbol_table.jump_dict.get(jump_asm)
    else:
        return '000'

