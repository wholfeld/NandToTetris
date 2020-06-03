import sys
from pathlib import Path
from vm_parser import VMParser
from vm_codewriter import VMCodewriter


def format_folder(folder_name: str) -> str:
    folder_name = folder_name.lower()
    return f'../{folder_name}'


def get_vm_list():
    # Open files in folder.
    folder_location = format_folder('StackArithmetic')
    if len(sys.argv) > 1:
        folder_location = format_folder(sys.argv[1])

    mod_path = Path(__file__).parent
    src_path = (mod_path / folder_location).resolve()
    vm_list = list(src_path.glob('*.vm'))
    return vm_list


def open_vm_files(vm_list):
    writer = VMCodewriter('Main.asm')
    # For each file pass to parser.
    for file in vm_list:
        write_asm_file(writer, file)


def write_asm_file(writer, file):
    # Get command and pass to codewriter.
    parser = VMParser(file)
    while parser.has_more_commands():
        command = parser.get_command()
        writer.write_command(command)
        parser.advance()


def main():
    vm_list = get_vm_list()
    open_vm_files(vm_list)


if __name__ == '__main__':
    main()
