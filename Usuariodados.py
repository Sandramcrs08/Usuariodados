# Este código solicitará ao usuário o nome completo e o ano de nascimento. Ele continuará pedindo ao usuário para digitar até que um valor válido seja inserido, usando a função input().

def obter_dados_usuario():
    nome_completo = input("Digite seu nome completo: ")
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1923 e 2023): "))
            if 1923 <= ano_nascimento <= 2023:
                return nome_completo, ano_nascimento
            else:
                print("Por favor, digite um ano de nascimento válido.")
        except ValueError:
            print("Erro: Por favor, digite um valor numérico para o ano de nascimento.")

nome, ano = obter_dados_usuario()


# calcular a idade do usuário no ano atual (2024). Usando o módulo datetime.

from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

idade = calcular_idade(ano)

# imprimir o nome do usuário e sua idade.

print(f"Olá, {nome}! Você tem {idade} anos.")



