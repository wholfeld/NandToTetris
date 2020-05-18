class parser:

    def __init__(self, file):
        print(file)
        self.file = file
        with file.open() as f:
            for x in f:
                # pass
                print(x)

    def hasMoreCommands(self) -> bool:
        print('hi')
        return True
