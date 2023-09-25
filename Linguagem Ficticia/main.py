import re

#esta linguagem aceita numeros inteiros, operadores aritimeticos e espaços em branco
def analisador_lexico(entrada):
    
    padrao_numero = r'\d+'
    padrao_operador = r'[+\-\*\/]'
    padrao_espaco = r'\s+'

    tokens = []

    while entrada:

        espaco_match = re.match(padrao_espaco, entrada)
        if espaco_match:
            entrada = entrada[espaco_match.end():]
            continue

        numero_match = re.match(padrao_numero, entrada)
        if numero_match:
            token = numero_match.group()
            tokens.append(('NUMERO', token))
            entrada = entrada[numero_match.end():]
            continue

        operador_match = re.match(padrao_operador, entrada)
        if operador_match:
            token = operador_match.group()
            tokens.append(('OPERADOR', token))
            entrada = entrada[operador_match.end():]
            continue

        raise ValueError(f"Erro léxico: Caractere não aceito '{entrada[0]}'")

    return tokens

entrada = "12 + 34 * 5"
tokens = analisador_lexico(entrada)

print(tokens,"\n")
for token in tokens:
    print(token)
