import sys
from pathlib import Path
from jack_parser import JackParser
from jack_tokenizer import JackTokenizer
from jack_compiler import JackCompiler
from xml_parser import XMLParser


def get_files_location() -> str:
    # Open files in folder.
    folder_location = format_folder('SquareWarrick')
    if len(sys.argv) > 1:
        folder_location = format_folder(sys.argv[1])

    mod_path = Path(__file__).parent
    src_path = (mod_path / folder_location).resolve()
    return src_path


def format_folder(folder_name: str) -> str:
    return f'../{folder_name}'


def get_jack_list(src_path) -> list:
    jack_list = list(src_path.glob('*.jack'))
    return jack_list


def get_tokens_list(src_path) -> list:
    xml_list = list(src_path.glob('*T.xml'))
    return xml_list


def open_jack_files(jack_list, src_path):
    # xml_name = src_path.name + '.xml'
    # file_name = (src_path / xml_name).resolve()
    # writer = JackParser(file_name)

    # For each file pass to parser.
    # sorted_jack_list = []
    # for i in range(len(jack_list)):
    #     if 'Main.jack' in jack_list[i].name:
    #         sorted_jack_list.append(jack_list[i])

    for file in jack_list:
        write_token_xml_file(file)


def open_xml_files(xml_tokens_list, stc_path):
    for file in xml_tokens_list:
        write_xml_file(file)


def write_token_xml_file(file):
    # Get command and pass to codewriter.
    parser = JackParser(file)
    file_name = str(file).replace('.jack', 'T.xml')
    writer = JackTokenizer(file_name)
    # writer.set_class_name(file)
    while parser.has_more_tokens():
        token = parser.advance()
        writer.write_command(token)

    writer.done()

    writer.close()


def write_xml_file(file):
    file_name = str(file).replace('T.xml', '.xml')
    parser = XMLParser(file)
    JackCompiler(parser, file_name)


def main():
    src_path = get_files_location()
    # jack_list = get_jack_list(src_path)
    # open_jack_files(jack_list, src_path)
    tokens_list = get_tokens_list(src_path)
    open_xml_files(tokens_list, src_path)


if __name__ == '__main__':
    main()
