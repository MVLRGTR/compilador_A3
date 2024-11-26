def gerar_codigo(ast):
    codigo = []

    # Gerando declarações de variáveis
    for comando in ast:
        if comando['tipo'] == 'declaracao':
            codigo.append(f"{comando['variavel']} = {comando['valor']}")

        # Gerando comandos 'imprimir'
        elif comando['tipo'] == 'imprimir':
            codigo.append(f"print({comando['valor']})")

        # Gerando comandos 'leia'
        elif comando['tipo'] == 'leia':
            codigo.append(f"{comando['variavel']} = input()")

        # Gerando estruturas de controle 'se'
        elif comando['tipo'] == 'se':
            codigo.append(f"if {comando['condicao']}:")
            codigo.append("    " + gerar_codigo(comando['bloco']))

        # Gerando estrutura 'enquanto'
        elif comando['tipo'] == 'enquanto':
            codigo.append(f"while {comando['condicao']}:")
            codigo.append("    " + gerar_codigo(comando['bloco']))

        # Gerando estrutura 'para'
        elif comando['tipo'] == 'para':
            codigo.append(f"for {comando['variavel']} in range({comando['inicio']}, {comando['fim']}):")
            codigo.append("    " + gerar_codigo(comando['bloco']))

    return "\n".join(codigo)
