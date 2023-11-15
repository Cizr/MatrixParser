import ply.lex as lex
import ply.yacc as yacc

#Lexical specifications start here
tokens = ['NUM', 'COMMA', 'OPEN_BRACKET', 'CLOSE_BRACKET']

#regular expressions for tokens
t_NUM = r'\d+'
t_COMMA = r','
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'

#characters to be ignored (whitespace and tabs and so on)
t_ignore = ' \t'

#rule to handle newline characters
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#handle errors in the lexer
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

#p_S function defines the production rules for the non-terminal S in the parser
def p_S(p): 
    '''S : OPEN_BRACKET Lignes CLOSE_BRACKET 
         | S OPEN_BRACKET Lignes CLOSE_BRACKET'''
    print("Matrix is written correctly")

#p_Lignes function defines the production rules for the non-terminal lignes each represented by the non-terminal Ligne
#Elements are separated by commas(sequence can also consist of a single element without commas)
def p_Lignes(p):
    '''Lignes : Ligne COMMA Lignes
              | Ligne'''
              
#Ligne can be defined as a single numerical element represented by the non-terminal NUM (Ligne can be defined as a numerical element followed by another ligne)
#it allows for parsing a sequence of numerical elements in succession.
def p_Ligne(p):
    '''Ligne : NUM
             | NUM Ligne'''

#handle syntax errors in the parser(triggered when a syntax error occurs during parsing)
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {find_column(input_text, p)}: Unexpected token {p.value}")

#find_column function calculates the column number of a given token in our input text the function identifies the position of the last newline character 
#before the token's lexeme and computes the column number by subtracting the starting position of the line from the token's position
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()
parser = yacc.yacc()

#input example
input_text = "[1,34]\n[3,6]"

#print tokens
lexer.input(input_text)
for tok in lexer:
    print(tok)

#print the result
parser.parse(input_text)
