# PortuPython: Uma Linguagem Inspirada no Portugol

Este projeto foi desenvolvido como parte do trabalho da disciplina de Teoria da Computação e Compiladores da UNIFACS, Salvador-BA. Ele consiste na criação de uma linguagem fictícia chamada **PortuPython**, que combina a simplicidade do **Portugol** com funcionalidades adicionais, como encapsulamento com chaves `{}`. O objetivo do projeto é compilar o código escrito em **PortuPython** para **Python**. Foram utilizados no projeto as bibliotecas PLY e Tkinter.

https://youtu.be/OQb7Jp_h-gw

---

## 📋 Componentes do Grupo
- **Henrique Cavalcanti Rocha** - RA: 12722117519  
- **Marcos Vinicius Lima Ribeiro** - RA: 12723116626  
- **Pedro Martins Caires** - RA: 12722124034  
- **Rafael Rodrigues Figueiredo** - RA: 12722130532  
- **Sérgio Filho de Paula Fidelis** - RA: 1272215886  

---

## 🛠 Estrutura do Projeto

### Arquivos Principais
- **lexer.py**  
  Este arquivo contém o analisador léxico da linguagem, implementado com a biblioteca **PLY**. O lexer é responsável por identificar os tokens que compõem o código fonte da linguagem **PortuPython**, como palavras-chave (`SE`, `SENAO`, `ENQUANTO`), operadores, identificadores e outros elementos.

- **grammar.py**  
  Este arquivo implementa o analisador sintático da linguagem também com **PLY**. Ele define as regras gramaticais que determinam como os tokens reconhecidos pelo lexer devem ser combinados para formar construções válidas em **PortuPython**, como estruturas condicionais, loops e declarações de variáveis.

---

## 🌐 Equivalência da Linguagem Criada para Python

A linguagem **PortuPython** é projetada para ser intuitiva, utilizando palavras-chave em português, semelhantes ao **Portugol**. Após a compilação, o código é convertido para **Python**, com a seguinte equivalência entre seus elementos:

| **PortuPython**  | **Python**   |
|-------------------|--------------|
| `SE`             | `if`         |
| `SENAO`          | `else`       |
| `ENQUANTO`       | `while`      |
| `PARA`           | `for`        |
| `INTEIRO`        | `int`        |
| `REAL`           | `float`      |
| `TEXTO`          | `str`        |
| `IMPRIMIR`       | `print`      |
| `LEIA`           | `input`      |
| `{}`             |              |

Exemplo em **PortuPython**:
```plaintext
INTEIRO x;
SE x > 0 {
    IMPRIMIR("Positivo");
} SENAO {
    IMPRIMIR("Negativo");
}

exemplo de código :
inteiro x = 10
se (x == 10) {
imprimir (x)
} senao {
imprimir ("Não é igual a 10")
}

inteiro x = 10
enquanto (x < 15) {
imprimir (x)
x = x + 1
}

inteiro x = 10.5
real y = "texto"
texto z = 10
