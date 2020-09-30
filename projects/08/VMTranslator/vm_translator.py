import sys
from pathlib import Path
from vm_parser import VMParser
from vm_codewriter import VMCodewriter


def format_folder(folder_name: str) -> str:
    # folder_name = folder_name.lower()
    return f'../{folder_name}'


def get_files_location() -> str:
    # Open files in folder.
    folder_location = format_folder('FunctionCalls/NestedCall')
    print(sys.argv)
    if len(sys.argv) > 1:
        folder_location = format_folder(sys.argv[1])

    mod_path = Path(__file__).parent
    src_path = (mod_path / folder_location).resolve()
    return src_path


def get_vm_list(src_path) -> list:
    vm_list = list(src_path.glob('*.vm'))
    return vm_list


def open_vm_files(vm_list, src_path):
    asm_name = src_path.name + '.asm'
    file_name = (src_path / asm_name).resolve()
    writer = VMCodewriter(file_name)
    # For each file pass to parser.
    sorted_vm_list = []
    for i in range(len(vm_list)):
        if 'Sys.vm' in vm_list[i].name:
            sorted_vm_list.append(vm_list[i])

    for i in range(len(vm_list)):
        if 'Sys.vm' not in vm_list[i].name:
            sorted_vm_list.append(vm_list[i])

    for file in sorted_vm_list:
        write_asm_file(writer, file)

    writer.close()


def write_asm_file(writer, file):
    # Get command and pass to codewriter.
    parser = VMParser(file)
    writer.set_class_name(file)
    while parser.has_more_commands():
        command = parser.get_command()
        writer.write_command(command)
        parser.advance()


def main():
    src_path = get_files_location()
    vm_list = get_vm_list(src_path)
    open_vm_files(vm_list, src_path)


if __name__ == '__main__':
    main()
