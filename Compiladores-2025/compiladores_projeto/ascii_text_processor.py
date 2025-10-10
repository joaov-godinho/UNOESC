import string

def extrair_caracteres(arquivo):
    """
    Lê um arquivo de texto e retorna a sequência de caracteres ASCII individuais.
    """
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    return list(conteudo)

def remover_caracteres_nao_desejados(caracteres, indesejados):
    """
    Remove caracteres indesejados da lista fornecida.
    """
    return [c for c in caracteres if c not in indesejados]

def listar_linhas_numeradas(arquivo):
    """
    Cria uma listagem numerada do texto do arquivo.
    """
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    return [(i + 1, linha.strip()) for i, linha in enumerate(linhas)]

def tabela_referencias_cruzadas(arquivo):
    """
    Gera uma tabela de referências cruzadas indicando as linhas onde cada palavra ocorre.
    """
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    referencias = {}
    for i, linha in enumerate(linhas):
        palavras = linha.strip().translate(str.maketrans('', '', string.punctuation)).split()
        for palavra in palavras:
            palavra_lower = palavra.lower()
            if palavra_lower not in referencias:
                referencias[palavra_lower] = set()
            referencias[palavra_lower].add(i + 1)

    referencias_ordenadas = {k: sorted(v) for k, v in sorted(referencias.items())}
    return referencias_ordenadas

def main():
    arquivo = input("Digite o nome do arquivo de texto: ")

    # Etapa 1: Extrair caracteres
    caracteres = extrair_caracteres(arquivo)
    print("\nSequência de caracteres ASCII no arquivo:")
    print(caracteres)

    # Etapa 2: Remover caracteres indesejados
    indesejados = ['\n', '\t', ' ', '\r']  # Brancos, espaçadores, tabulações, etc.
    caracteres_filtrados = remover_caracteres_nao_desejados(caracteres, indesejados)
    print("\nSequência após remover caracteres indesejados:")
    print(caracteres_filtrados)

    # Etapa 3: Listagem numerada
    linhas_numeradas = listar_linhas_numeradas(arquivo)
    print("\nListagem numerada do texto:")
    for num, linha in linhas_numeradas:
        print(f"{num}: {linha}")

    # Etapa 4: Tabela de referências cruzadas
    referencias = tabela_referencias_cruzadas(arquivo)
    print("\nTabela de referências cruzadas:")
    for palavra, linhas in referencias.items():
        print(f"{palavra}: {', '.join(map(str, linhas))}")

if __name__ == "__main__":
    main()
