import ply.lex as lex

reserved = {	
	'para'	   :	'PARA',	
	'se'	   :	'SE',
	'senao'	   :	'SENAO',
	'inteiro'  :	'INTEIRO',
    'real'	   :	'REAL',	
	'texto'    :	'TEXTO',	
	'enquanto' :	'ENQUANTO',
	'imprimir' :	'IMPRIMIR',
	'leia'     :	'LEIA'
}


tokens = ['VARIAVEL', 'NUMERO', 'TEXTONORMAL', 'OP_SUB', 'OP_SOMA', 'OP_MULT', 'OP_DIV', 'OP_IGUAL', 'OP_ASPAS',
 'RPAREN', 'LPAREN', 'RBRACE', 'LBRACE', 'OP_VIRGULA', 'OP_PONTO_VIRGULA', 'OP_PONTO', 'OU', 'E', 'OP_DOIS_PONTOS',
 'OP_IGUALDADE', 'OP_DIFERENTE', 'MENOR', 'MAIOR', 'MENORIGUAL', 'MAIORIGUAL'
 ]+ list(reserved.values())


t_ignore 		= ' \t'

t_RPAREN		= r'\)'
t_LPAREN		= r'\('
t_RBRACE		= r'\}'
t_LBRACE		= r'\{'

t_OP_VIRGULA		= r'\,'
t_OP_PONTO_VIRGULA	= r'\;'
t_OU 			    = r'ou'
t_E			        = r'e'
t_OP_DOIS_PONTOS 	= r'\:'
t_OP_PONTO       	= r'\.'

t_OP_IGUALDADE	= r'=='
t_OP_DIFERENTE	= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENORIGUAL	= r'<='
t_MAIORIGUAL 	= r'>='

t_OP_SOMA  		= r'\+'
t_OP_SUB		= r'-'
t_OP_MULT		= r'\*'
t_OP_DIV		= r'/'
t_OP_IGUAL		= r'='
t_OP_ASPAS      = r'\"'

'''
t_PARA		    = r'para'
t_SE		    = r'se'
t_SENAO		    = r'senao'
t_INTEIRO   	= r'inteiro'
t_REAL  	    = r'real'
t_TEXTO         = r'texto'
t_ENQUANTO	    = r'enquanto'
'''


def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:# Check for reserved words
        t.type = reserved[ t.value ]
    return t


def t_TEXTONORMAL(t):
	r'\"([^\\\n]|(\\.))*?\"'
	return t

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t


def t_novaLinha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

teste = '''
inteiro valor 7 + 10
'''

lexer.input(teste)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value)