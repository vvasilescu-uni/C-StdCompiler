import ply.lex as lex
import ply.yacc as yacc

from cminlex import *
from cmingrammar import *

from utils import CustomEncoder

with open('example.c' , 'r') as example_file:
    data = example_file.read()

lexer = lex.lex()
lexer.input(data)

parser = yacc.yacc()
program = parser.parse(data)

print(CustomEncoder().encode(program))
