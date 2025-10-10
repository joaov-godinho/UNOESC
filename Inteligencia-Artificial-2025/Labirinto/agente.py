import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def inicializar_ambiente(tamanho):
    """
    Inicializa o ambiente com uma matriz, a posição do agente e a posição do alvo.

    Args:
        tamanho (int): Tamanho do grid (tamanho x tamanho).

    Returns:
        tuple: Matriz do ambiente, posição inicial do agente, posição do alvo.
    """
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    # Adicionar obstáculos aleatórios
    for i in range(tamanho):
        for j in range(tamanho):
            if random.random() < 0.2:  # 20% de chance de ser um obstáculo
                matriz[i][j] = 1

    # Garantir que o agente e o alvo estejam em células livres
    pos_agente = (0, 0)
    pos_alvo = (tamanho - 1, tamanho - 1)
    matriz[0][0] = 0
    matriz[tamanho - 1][tamanho - 1] = 0

    return matriz, pos_agente, pos_alvo

def imprimir_matriz(matriz):
    """Imprime a matriz do ambiente no console."""
    for linha in matriz:
        print(' '.join(map(str, linha)))

def get_local_view(matriz, x, y):
    """
    Retorna a visão local 3x3 do agente.

    Args:
        matriz (list): Matriz do ambiente.
        x (int): Coordenada x do agente.
        y (int): Coordenada y do agente.

    Returns:
        list: Visão local 3x3 preenchida com paredes virtuais nas bordas.
    """
    tamanho = len(matriz)
    local_view = []

    for i in range(x - 1, x + 2):
        linha = []
        for j in range(y - 1, y + 2):
            if 0 <= i < tamanho and 0 <= j < tamanho:
                linha.append(matriz[i][j])
            else:
                linha.append(1)  # Parede virtual
        local_view.append(linha)

    return local_view

def imprimir_local_view(local_view):
    """Imprime a visão local 3x3 no console."""
    for linha in local_view:
        print(' '.join(map(str, linha)))

def distancia_manhattan(pos1, pos2):
    """
    Calcula a distância de Manhattan entre duas posições.

    Args:
        pos1 (tuple): Coordenada (x, y) da primeira posição.
        pos2 (tuple): Coordenada (x, y) da segunda posição.

    Returns:
        int: Distância de Manhattan.
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def greedy_move(agent_pos, target_pos, matrix, visited):
    """
    Determina o próximo movimento do agente usando a estratégia gulosa.

    Args:
        agent_pos (tuple): Coordenada (x, y) do agente.
        target_pos (tuple): Coordenada (x, y) do alvo.
        matrix (list): Matriz representando o ambiente.
        visited (set): Conjunto de células já visitadas pelo agente.

    Returns:
        tuple: Próxima posição (x, y) do agente.
    """
    x, y = agent_pos
    tamanho = len(matrix)

    # Definir as direções possíveis (cima, baixo, esquerda, direita)
    direcoes = [
        (x - 1, y),  # Cima
        (x + 1, y),  # Baixo
        (x, y - 1),  # Esquerda
        (x, y + 1),  # Direita
    ]

    # Avaliar as direções válidas
    melhores_opcoes = []
    menor_distancia = float('inf')
    for nova_pos in direcoes:
        nx, ny = nova_pos
        if (0 <= nx < tamanho and 0 <= ny < tamanho and
                (matrix[nx][ny] == 0 or matrix[nx][ny] == 3) and  # Permitir movimento para o alvo
                nova_pos not in visited):  # Verifica célula válida

            distancia = distancia_manhattan(nova_pos, target_pos)
            if distancia < menor_distancia:
                melhores_opcoes = [nova_pos]
                menor_distancia = distancia
            elif distancia == menor_distancia:
                melhores_opcoes.append(nova_pos)

    # Escolher uma das melhores opções
    if melhores_opcoes:
        return random.choice(melhores_opcoes)  # Retorna uma posição aleatória entre as melhores
    return agent_pos  # Retorna a posição atual se não houver movimento possível

def executar_agente(matriz, pos_agente, pos_alvo):
    """
    Executa o loop do agente até que ele alcance o alvo ou fique preso.

    Args:
        matriz (list): Matriz representando o ambiente.
        pos_agente (tuple): Posição inicial do agente.
        pos_alvo (tuple): Posição do alvo.
    """
    passos = 0
    visited = set()
    caminho = []

    while pos_agente != pos_alvo:
        passos += 1
        visited.add(pos_agente)
        caminho.append(pos_agente)
        print(f"\nPasso {passos}:")
        print(f"Agente em: {pos_agente}, Alvo em: {pos_alvo}")

        # Obter a percepção local
        local_view = get_local_view(matriz, pos_agente[0], pos_agente[1])
        print("Percepção Local:")
        imprimir_local_view(local_view)

        # Determinar o próximo movimento
        nova_pos = greedy_move(pos_agente, pos_alvo, matriz, visited)

        # Verificar se o agente ficou preso (sem movimentos possíveis)
        if nova_pos == pos_agente:
            print("O agente não pode se mover. Encerrando execução.")
            return caminho

        # Atualizar a posição do agente
        matriz[pos_agente[0]][pos_agente[1]] = 0  # Marca a célula anterior como livre
        matriz[nova_pos[0]][nova_pos[1]] = 2  # Marca a nova posição do agente
        pos_agente = nova_pos

        # Imprimir o grid atualizado
        imprimir_matriz(matriz)

    print("\nO agente alcançou o alvo com sucesso!")
    return caminho

def exibir_interface(matriz, caminho):
    """
    Exibe a interface gráfica do ambiente e o caminho do agente usando matplotlib.

    Args:
        matriz (list): Matriz representando o ambiente.
        caminho (list): Lista de posições percorridas pelo agente.
    """
    fig, ax = plt.subplots()

    def atualizar(frame):
        ax.clear()
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] == 1:
                    ax.add_patch(plt.Rectangle((j, len(matriz) - 1 - i), 1, 1, color="black"))
                elif matriz[i][j] == 3:
                    ax.add_patch(plt.Rectangle((j, len(matriz) - 1 - i), 1, 1, color="green"))
        if frame < len(caminho):
            x, y = caminho[frame]
            ax.add_patch(plt.Rectangle((y, len(matriz) - 1 - x), 1, 1, color="blue"))
        ax.set_xlim(0, len(matriz))
        ax.set_ylim(0, len(matriz))
        ax.set_aspect("equal")

    ani = animation.FuncAnimation(fig, atualizar, frames=len(caminho), interval=500)
    plt.show()

if __name__ == "__main__":
    tamanho = 10
    matriz, pos_agente, pos_alvo = inicializar_ambiente(tamanho)

    # Marcar as posições do agente e do alvo na matriz
    matriz[pos_agente[0]][pos_agente[1]] = 2  # Marca o agente com '2'
    matriz[pos_alvo[0]][pos_alvo[1]] = 3  # Marca o alvo com '3'

    print("Matriz Inicial:")
    imprimir_matriz(matriz)

    # Executar o loop do agente
    caminho = executar_agente(matriz, pos_agente, pos_alvo)

    # Exibir a interface gráfica
    exibir_interface(matriz, caminho)
