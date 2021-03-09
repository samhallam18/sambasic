DIGITS = '0123456789'

INT     = 'INT'
FLOAT   = 'FLOAT'
PLUS    = 'PLUS'
MINUS   = 'MINUS'
MUL     = 'MUL'
DIV     = 'DIV'
LPAR    = 'LPAR'
RPAR    = 'RPAR'

class Error:
    def __init__(self, name, details):
        self.name = name
        self.details = details

    def as_string(self):
        return f'{self.name}: {self.details}'

class CharNotAllowedError(Error):
    def __init__(self, details):
        super().__init__('Char Not Allowed', details)

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(LPAR))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RPAR))
                self.advance()
            else:
                current_char = self.current_char
                self.advance()
                return [], CharNotAllowedError("'" + current_char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(INT, int(num_str))
        else:
            return Token(FLOAT, float(num_str))

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error
