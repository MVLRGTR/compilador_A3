# codegen.py

def gerar_codigo(ast):
    """
    Função principal que recebe a AST e gera o código Python correspondente.
    """
    return gerador_blocos(ast)

def gerador_blocos(ast):
    """
    Função recursiva que gera código para um bloco de instruções.
    """
    if isinstance(ast, list):  # Verifica se é uma lista de instruções
        return "\n".join(gerador_instrucao(instr) for instr in ast)
    else:
        return gerador_instrucao(ast)

def gerador_instrucao(instrucao):
    """
    Função que gera código para uma única instrução.
    """
    if instrucao['tipo'] == 'imprimir':
        return f"print({instrucao['valor']})"
    
    elif instrucao['tipo'] == 'declaracao':
        return f"{instrucao['variavel']} = {instrucao['valor']}"
    
    elif instrucao['tipo'] == 'enquanto':
        return f"while {instrucao['condicao']}:\n    {gerador_blocos(instrucao['bloco'])}"
    
    elif instrucao['tipo'] == 'se':
        condicao = instrucao['condicao']
        bloco = gerador_blocos(instrucao['bloco'])
        codigo = f"if {condicao}:\n    {bloco}"
        
        if 'senao' in instrucao:
            senao_bloco = gerador_blocos(instrucao['senao'])
            codigo += f"\nelse:\n    {senao_bloco}"
        
        return codigo
    
    elif instrucao['tipo'] == 'leia':
        return f"{instrucao['variavel']} = input('Digite um valor: ')"
    
    # Adicionar mais instruções conforme os tipos no seu parser
    return ''

# Exemplo de como a AST pode ser representada:
ast_exemplo = [
    {'tipo': 'imprimir', 'valor': '"Olá Mundo!"'},
    {'tipo': 'declaracao', 'variavel': 'x', 'valor': '5'},
    {'tipo': 'enquanto', 'condicao': 'x > 0', 'bloco': [
        {'tipo': 'imprimir', 'valor': '"Decrementando x"'},
        {'tipo': 'declaracao', 'variavel': 'x', 'valor': 'x - 1'}
    ]}
]

# Geração do código
codigo_python = gerar_codigo(ast_exemplo)
print(codigo_python)
