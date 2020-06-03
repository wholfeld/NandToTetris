import sys
import assembly_parser
import symbol_table
import binary_generator
from pathlib import Path


class Assembler():
    def __init__(self, parser):
        self.user_created_symbols = {}
        self.new_symbol_index = 16

    def run_pass_to_store_symbols(self, parser):
        while parser.has_more_commands():
            _cur_command = parser.get_current_command()
            if assembly_parser.command_type(_cur_command) == symbol_table.CommandType.L_COMMAND:
                self.user_created_symbols[_cur_command[1:-1]] = parser.get_current_line()
            parser.advance()

    def run_second_pass(self, parser, file_name):
        f_name = str(file_name).replace('asm', 'hack')
        f = open(f'{f_name}', 'w')
        while parser.has_more_commands():
            cur_command = parser.get_current_command()
            if assembly_parser.command_type(cur_command) == symbol_table.CommandType.C_COMMAND:
                f.write(binary_generator.get_instruction_binary(cur_command) + '\n')
            elif assembly_parser.command_type(cur_command) == symbol_table.CommandType.A_COMMAND:
                a = cur_command[1:]
                if a[0:1].isdigit():
                    f.write(binary_generator.get_address(a) + '\n')
                else:
                    s = symbol_table.symbols_dict.get(a)
                    if s:
                        f.write(binary_generator.get_address(s) + '\n')
                    elif self.user_created_symbols.get(a):
                        f.write(binary_generator.get_address(self.user_created_symbols.get(a)) + '\n')
                    else:
                        f.write(binary_generator.get_address(self.new_symbol_index) + '\n')
                        self.user_created_symbols.update({a: self.new_symbol_index})
                        self.new_symbol_index += 1
            parser.advance()
        f.close()

    def get_symbol_address(symbol):
        pass


def main():
    folder_location = format_folder("max")
    if len(sys.argv) > 1:
        folder_location = format_folder(sys.argv[1])

    mod_path = Path(__file__).parent
    # print(mod_path)
    src_path = (mod_path / folder_location).resolve()
    asm_list = list(src_path.glob('*.asm'))

    for file in asm_list:
        parser = assembly_parser.Parser(file)

        assembler_obj = Assembler(parser)

        assembler_obj.run_pass_to_store_symbols(parser)
        parser.reset_parser()
        assembler_obj.run_second_pass(parser, file)


def format_folder(folder_name: str) -> str:
    folder_name = folder_name.lower()
    return f'../{folder_name}'


if __name__ == "__main__":
    main()