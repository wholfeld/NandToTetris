from enum import Enum
from symbol_table import TokenTypes, keyword_set, symbol_set


class JackParser:

    def __init__(self, file):
        self.file = file
        self.tokens = []
        self.location = 0
        processing_type = None
        with file.open() as f:
            for line in f:
                clean_command = remove_whitespace(line)
                current_token = ''
                for char in clean_command:
                    if processing_type == TokenTypes.COMMENT_START:
                        if char == '/':
                            processing_type = None
                            break
                        elif char == '*':
                            processing_type = TokenTypes.COMMENT
                            if '*/' in line:
                                processing_type = None
                                break
                        else:
                            self.tokens.append(('/', TokenTypes.SYMBOL))
                            processing_type = None
                    elif processing_type == TokenTypes.IDENTIFIER:
                        if char == '_' or char.isalnum():
                            current_token += char
                        else:
                            if current_token in keyword_set:
                                processing_type = TokenTypes.KEYWORD
                            self.tokens.append((current_token, processing_type))
                            processing_type = None
                    elif processing_type == TokenTypes.STRING_CONST:
                        if char == '"':
                            self.tokens.append((current_token, processing_type))
                            processing_type = None
                            continue
                        else:
                            current_token += char
                    elif processing_type == TokenTypes.INT_CONST:
                        if char.isnumeric():
                            current_token += char
                        else:
                            self.tokens.append((current_token, processing_type))
                            processing_type = None
                    elif processing_type == TokenTypes.COMMENT:
                        if char == '/':
                            processing_type = None
                            continue

                    if not processing_type:
                        current_token = ''
                        if char in symbol_set and char != '/':
                            symbol = char
                            if symbol == '<':
                                symbol = '&lt;'
                            elif symbol == '>':
                                symbol = '&gt;'
                            elif symbol == '"':
                                symbol = '&quot;'
                            elif symbol == '&':
                                symbol = '&amp;'
                            self.tokens.append((symbol, TokenTypes.SYMBOL))
                        elif char.isnumeric():
                            current_token += char
                            processing_type = TokenTypes.INT_CONST
                        elif char.isalpha() or char == '_':
                            current_token += char
                            processing_type = TokenTypes.IDENTIFIER
                        elif char == '/':
                            processing_type = TokenTypes.COMMENT_START
                        elif char == '"':
                            processing_type = TokenTypes.STRING_CONST

    def has_more_tokens(self) -> bool:
        return self.location < len(self.tokens)

    def advance(self) -> str:
        token = self.tokens[self.location]
        self.location += 1
        return token

    def token_type(self) -> Enum:
        return TokenTypes.KEYWORD


def remove_whitespace(command: str) -> str:
    no_whitespace_str = command.strip()
    return no_whitespace_str
