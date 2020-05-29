import sys
import assembly_parser
import symbol_table
import binary_generator
from pathlib import Path


class Assembler():
    def __init__(self, parser):
        self.user_created_symbols = {}
        self.symbolIndex = 16

    def run_pass_to_store_symbols(self, parser):
        while parser.has_more_commands():
            _cur_command = parser.get_current_command()
            if assembly_parser.command_type(_cur_command) == symbol_table.CommandType.L_COMMAND:
                self.user_created_symbols[_cur_command[1:-1]] = parser.get_current_line()
            parser.advance()
        i = 1

    def run_second_pass(self, parser):
        while parser.has_more_commands():
            _cur_command = parser.get_current_command()
            if assembly_parser.command_type(_cur_command) == symbol_table.CommandType.C_COMMAND:
                pass
            parser.advance()

    def get_symbol_address(symbol):
        pass


def main():
    binary_generator.writeAddress(9)
    file_location = format_filename("Rect.asm")
    # test = '../add/Add.asm' '../{folderName}/{fileName}
    if len(sys.argv) > 1:
        file_location = format_filename(sys.argv[1])

    mod_path = Path(__file__).parent
    # print(mod_path)
    src_path = (mod_path / file_location).resolve()
    parser = assembly_parser.Parser(src_path)

    assembler_obj = Assembler(parser)

    assembler_obj.run_pass_to_store_symbols(parser)
    parser.reset_parser()
    assembler_obj.run_second_pass(parser)


def format_filename(file_name: str) -> str:
    str_split = file_name.rsplit('.')
    file_name = file_name.capitalize()
    folder_name = str_split[0].lower()
    return f'../{folder_name}/{file_name}'


if __name__ == "__main__":
    main()