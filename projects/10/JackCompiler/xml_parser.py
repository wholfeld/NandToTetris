import re


class XMLParser():

    def __init__(self, file):
        self.file = file
        self.position = 0
        self.tokens_array = []
        with file.open() as f:
            for l in f:
                l_stripped = l.strip()
                if len(l) > 0:
                    self.tokens_array.append(l_stripped)

    def has_more_commands(self) -> bool:
        return self.position < len(self.tokens_array)

    def advance(self):
        self.position += 1

    def get_token(self):
        line = self.tokens_array[self.position]
        token_type_result = re.findall("<[^/]*>", line)
        token_type = ''
        if token_type_result:
            token_type = token_type_result[0][1:-1]
        keyword_result = re.findall(">.*<", line)
        keyword = ''
        if keyword_result:
            keyword = keyword_result[0][2:-2]
        return (token_type, keyword, line)
