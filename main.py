import ply.lex as lex
from cminlex import *


lexer = lex.lex()
with open('example.c' , 'r') as example_file:
    data = example_file.read()

lexer.input(data)

while 1:
    token = lexer.token()
    if not token: break
    print('{}\t\t\t{}\t\t\t{}\t\t\t{}'.format(token.type, token.value, token.lineno, token.lexpos))