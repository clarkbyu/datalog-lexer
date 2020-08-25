# Clark Brown

import sys
from Lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer(sys.argv[1])
    lexer.tokenize()
    print(lexer, end="")