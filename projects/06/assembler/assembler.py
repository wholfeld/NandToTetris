
import sys
import assemblyParser
from pathlib import Path


def main():
    print(sys.argv[1])
    # print(Path.cwd())
    mod_path = Path(__file__).parent
    test = '../add/Add.asm'
    print(mod_path)
    src_path = (mod_path / test).resolve()
    print(src_path)
    # print(src_path.exists())
    print(sorted(Path(mod_path).glob('*')))
    p = Path(src_path)
    print(p)
    assemblyParser.parser(p)
    # aParser.hasMoreCommands()

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


if __name__ == "__main__":
    main()