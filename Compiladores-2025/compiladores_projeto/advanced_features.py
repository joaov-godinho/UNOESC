# advanced_features.py

def converter_para_decimal(numero, base):
    try:
        return int(numero, base)
    except ValueError:
        print(f"Erro: '{numero}' não é válido na base {base}.")
        return None

def converter_de_decimal(numero_decimal, base_saida, digitos, posicao_sinal):
    if numero_decimal is None:
        return None
    
    if base_saida == 2:
        numero_convertido = bin(numero_decimal)[2:]
    elif base_saida == 8:
        numero_convertido = oct(numero_decimal)[2:]
    elif base_saida == 16:
        numero_convertido = hex(numero_decimal)[2:]
    else:
        numero_convertido = str(numero_decimal)

    # Ajustar a quantidade de dígitos
    if digitos > 0:
        numero_convertido = numero_convertido.zfill(digitos)
    
    # Posicionar o sinal conforme a escolha
    if posicao_sinal == 'direita':
        numero_convertido = numero_convertido + " "
    else:
        numero_convertido = " " + numero_convertido

    return numero_convertido

def tabela_de_simbolos():
    tabela = {}

    def adicionar_simbolo(simbolo, atributos):
        tabela[simbolo] = atributos

    def buscar_simbolo(simbolo):
        return tabela.get(simbolo)

    def exibir_tabela():
        for simbolo, atributos in tabela.items():
            print(f"{simbolo}: {atributos}")

    return adicionar_simbolo, buscar_simbolo, exibir_tabela

def pesquisa_em_tabelas_fixas(tabela_fixa, termo):
    return termo in tabela_fixa

def conversao_numerica():
    print("\n--- Conversão Numérica ---")
    numero = input("Digite um número para conversão: ")
    base = int(input("Digite a base do número (2, 8, 10, 16): "))
    numero_decimal = converter_para_decimal(numero, base)
    print(f"Número em decimal: {numero_decimal}")

    base_saida = int(input("Digite a base para a saída (2, 8, 10, 16): "))
    digitos = int(input("Número de dígitos (0 para padrão): "))
    posicao_sinal = input("Posição do sinal (esquerda/direita): ")
    numero_convertido = converter_de_decimal(numero_decimal, base_saida, digitos, posicao_sinal)
    print(f"Número convertido: {numero_convertido}")


def tabela_de_simbolos_func():
    print("\n--- Tabela de Símbolos ---")
    adicionar_simbolo, buscar_simbolo, exibir_tabela = tabela_de_simbolos()
    
    # Adicionar alguns símbolos padrões
    adicionar_simbolo("pi", {"valor": 3.14159, "constante": True})
    adicionar_simbolo("e", {"valor": 2.71828, "constante": True})
    exibir_tabela()

    # Opção para adicionar novos símbolos
    adicionar_novo_simbolo = input("Deseja adicionar um novo símbolo? (s/n): ")
    if adicionar_novo_simbolo.lower() == 's':
        simbolo_novo = input("Digite o nome do novo símbolo: ")
        valor_novo = input("Digite o valor do símbolo: ")
        constante = input("Este é um valor constante? (s/n): ").lower() == 's'
        adicionar_simbolo(simbolo_novo, {"valor": float(valor_novo), "constante": constante})
        print(f"Símbolo '{simbolo_novo}' adicionado.")

    simbolo = input("Digite um símbolo para buscar na tabela: ")
    atributos = buscar_simbolo(simbolo)
    if atributos:
        print(f"Atributos de {simbolo}: {atributos}")
    else:
        print(f"Símbolo {simbolo} não encontrado.")

    # Pesquisa na tabela fixa
    tabela_fixa = ["if", "else", "while", "for", "return"]
    termo = input("Digite um termo para pesquisar na tabela fixa: ")
    if pesquisa_em_tabelas_fixas(tabela_fixa, termo):
        print(f"O termo '{termo}' foi encontrado na tabela fixa.")
    else:
        print(f"O termo '{termo}' não foi encontrado na tabela fixa.")


def main():
    while True:
        print("\nEscolha a funcionalidade que deseja executar:")
        print("1. Conversão Numérica")
        print("2. Tabela de Símbolos")
        print("3. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            conversao_numerica()
        elif escolha == '2':
            tabela_de_simbolos_func()
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
