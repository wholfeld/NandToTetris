class parser:

    def __init__(self, file):
        print(file)
        self.file = file
        self.commands = []
        with file.open() as f:
            for x in f:
                # pass
                self.commands.append(x)
        y = 1

    def hasMoreCommands(self) -> bool:
        print('hi')
        return True
