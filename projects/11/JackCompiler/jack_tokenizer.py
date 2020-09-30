from enum_dictionaries import types_dict


class JackTokenizer:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = open(f'{file_name}', 'w')
        self.token_stack = []
        self.file.write('<tokens>\n')
        self.token_stack.append('</tokens>\n')

    def write_command(self, token):
        token_type = types_dict.get(token[1])
        self.file.write(f'<{token_type}> {token[0]} </{token_type}>\n')

    def done(self):
        while self.token_stack:
            self.file.write(self.token_stack.pop())

    def close(self):
        self.file.close()
