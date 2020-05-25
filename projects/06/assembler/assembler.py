import sys
import assemblyParser
import symbolTable
from pathlib import Path


class assembler():
    def __init__(self, parser):
        self.userCreatedSymbols = {}

    def runPassToStoreLoops(self, parser):
        while parser.hasMoreCommands():
            _cur_command = parser.getCurrentCommand()
            if assemblyParser.commandType(_cur_command) == symbolTable.CommandType.L_COMMAND:
                self.userCreatedSymbols[_cur_command[1:-1]] = parser.getCurrentLine()
            parser.advance()
    
    def runSecondPass(self, parser):

        while parser.hasMoreCommands():
            _cur_command = parser.getCurrentCommand()

            parser.advance()
                



def main():
    file_location = format_filename("Rect.asm")
    # test = '../add/Add.asm' '../{folderName}/{fileName}
    if len(sys.argv) > 1:
        file_location = format_filename(sys.argv[1])

    mod_path = Path(__file__).parent
    # print(mod_path)
    src_path = (mod_path / file_location).resolve()
    parser = assemblyParser.parser(src_path)

    assemblerObj = assembler(parser)

    assemblerObj.runPassToStoreLoops(parser)
    parser.resetParser()
    assemblerObj.runSecondPass(parser)
    # print(sorted(Path(mod_path).glob('*')))
    # p = Path(src_path)
    # print(p)
    # assemblyParser.parser(p)

    # aParser.hasMoreCommands()
    # print(src_path.exists())

    # TODO: parse every .asm file in folder
    #

    # print(os.path.dirname(os.getcwd()))
    # os.chdir(os.path.pardir)
    # os.chdir(os.path.pardir)
    # print(os.getcwd())
    # #os.chdir('/add')
    # dirname = os.path.dirname(__file__)
    # filename = os.path.join(dirname, '..', 'add')

    # print(filename)


def format_filename(file_name: str) -> str:
    str_split = file_name.rsplit('.')
    # print(str_split)
    file_name = file_name.capitalize()
    folder_name = str_split[0].lower()
    return f'../{folder_name}/{file_name}'


if __name__ == "__main__":
    main()