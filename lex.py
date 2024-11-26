import ply.lex as lex

# Palavras reservadas
reserved = {
    'para': 'PARA',
    'se': 'SE',
    'senao': 'SENAO',
    'senaose': 'SENAOSE',
    'inteiro': 'INTEIRO',
    'real': 'REAL',
    'texto': 'TEXTO',
    'enquanto': 'ENQUANTO',
    'imprimir': 'IMPRIMIR',
    'leia': 'LEIA'
}

# Tokens
tokens = ['VARIAVEL', 'NUMERO', 'TEXTONORMAL', 'OP_SUB', 'OP_SOMA', 'OP_MULT', 'OP_DIV',
          'OP_IGUAL', 'RPAREN', 'LPAREN'] + list(reserved.values())

# Ignorar espaços e tabs
t_ignore = ' \t'

# Operadores e delimitadores
t_RPAREN = r'\)'
t_LPAREN = r'\('
t_OP_SOMA = r'\+'
t_OP_SUB = r'-'
t_OP_MULT = r'\*'
t_OP_DIV = r'/'
t_OP_IGUAL = r'='


# Regras para tokens específicos
def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:  # Verifica palavras reservadas
        t.type = reserved[t.value]
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


# Construção do lexer
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