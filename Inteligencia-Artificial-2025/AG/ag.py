import random

# 1. Criação da população inicial
def gerar_populacao(tam_populacao, num_bits):
    """
    Gera uma população inicial aleatória de indivíduos.
    Cada indivíduo é uma lista de bits (0s e 1s).
    """
    return [[random.randint(0, 1) for _ in range(num_bits)] for _ in range(tam_populacao)]

# 2. Cálculo de fitness
def fitness(individuo):
    """
    Calcula o valor de "fitness" de um indivíduo.
    Neste exemplo, o fitness é a soma dos bits do indivíduo.
    Um fitness maior indica um indivíduo mais "forte".
    """
    return sum(individuo)

# 3. Seleção por torneio
def selecao_torneio(populacao):
    """
    Seleciona um indivíduo da população usando o método de torneio.
    Dois indivíduos são escolhidos aleatoriamente, e o que tiver maior fitness é selecionado.
    """
    # Garante que haja pelo menos 2 indivíduos na população para o torneio
    if len(populacao) < 2:
        return random.choice(populacao)

    competidor1, competidor2 = random.sample(populacao, 2)
    return competidor1 if fitness(competidor1) > fitness(competidor2) else competidor2

# 4. Cruzamento de um ponto
def cruzamento(pai1, pai2):
    """
    Realiza o cruzamento de um ponto entre dois pais para gerar dois filhos.
    Um ponto aleatório é escolhido, e os genes são trocados a partir desse ponto.
    """
    ponto_cruzamento = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]
    filho2 = pai2[:ponto_cruzamento] + pai1[ponto_cruzamento:]
    return filho1, filho2

# 5. Mutação
def mutacao(individuo, taxa_mutacao):
    """
    Aplica mutação a um indivíduo.
    Para cada gene, há uma chance (taxa_mutacao) de que ele seja invertido (0 vira 1, e 1 vira 0).
    """
    individuo_mutado = []
    for gene in individuo:
        if random.random() < taxa_mutacao:
            individuo_mutado.append(1 - gene)  # Inverte o bit
        else:
            individuo_mutado.append(gene)
    return individuo_mutado


### --------- Execução e Evolução -------------


# Parâmetros do Algoritmo Genético
TAMANHO_POPULACAO = 10
NUM_BITS = 8
TAXA_MUTACAO = 0.1 # 10%
NUM_GERACOES = 10

# Geração inicial da população
populacao = gerar_populacao(TAMANHO_POPULACAO, NUM_BITS)
print(f"--- População Inicial (Geração 0) ---")
for i, ind in enumerate(populacao):
    print(f"Indivíduo {i+1}: {ind} (Fitness: {fitness(ind)})")
print("-" * 40)

# 6. Evolução por 10 gerações
for geracao in range(1, NUM_GERACOES + 1):
    nova_populacao = []

    # Enquanto a nova população não estiver cheia
    while len(nova_populacao) < TAMANHO_POPULACAO:
        # Seleção de dois pais por torneio
        pai1 = selecao_torneio(populacao)
        pai2 = selecao_torneio(populacao)

        # Cruzamento para gerar filhos
        filho1, filho2 = cruzamento(pai1, pai2)

        # Mutação nos filhos
        filho1_mutado = mutacao(filho1, TAXA_MUTACAO)
        filho2_mutado = mutacao(filho2, TAXA_MUTACAO)

        # Adiciona os filhos mutados à nova população
        nova_populacao.extend([filho1_mutado, filho2_mutado])

    # Se a nova população exceder o tamanho, trunca
    nova_populacao = nova_populacao[:TAMANHO_POPULACAO]

    # A nova população se torna a população atual para a próxima geração
    populacao = nova_populacao

    print(f"\n--- População na Geração {geracao} ---")
    melhor_fitness_geracao = 0
    pior_fitness_geracao = NUM_BITS + 1 # Valor maior que o máximo possível
    soma_fitness_geracao = 0

    for i, ind in enumerate(populacao):
        current_fitness = fitness(ind)
        print(f"Indivíduo {i+1}: {ind} (Fitness: {current_fitness})")
        soma_fitness_geracao += current_fitness
        if current_fitness > melhor_fitness_geracao:
            melhor_fitness_geracao = current_fitness
        if current_fitness < pior_fitness_geracao:
            pior_fitness_geracao = current_fitness

    print(f"Média de Fitness na Geração {geracao}: {soma_fitness_geracao / TAMANHO_POPULACAO:.2f}")
    print(f"Melhor Fitness na Geração {geracao}: {melhor_fitness_geracao}")
    print(f"Pior Fitness na Geração {geracao}: {pior_fitness_geracao}")
    print("-" * 40)

# Exibindo a população final
print(f"\n--- População Final (Após {NUM_GERACOES} Gerações) ---")
melhor_individuo_final = []
melhor_fitness_final = 0
for i, ind in enumerate(populacao):
    current_fitness = fitness(ind)
    print(f"Indivíduo {i+1}: {ind} (Fitness: {current_fitness})")
    if current_fitness > melhor_fitness_final:
        melhor_fitness_final = current_fitness
        melhor_individuo_final = ind

print(f"\nO melhor indivíduo encontrado foi: {melhor_individuo_final} com fitness: {melhor_fitness_final}")