from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Chover', 'GramaMolhada'), ('Sprinkler', 'GramaMolhada')])

cpd_chuva = TabularCPD('Chover', 2, [[0.3], [0.7]])
cpd_sprinkler = TabularCPD('Sprinkler', 2, [[0.5], [0.5]])
cpd_grama = TabularCPD('GramaMolhada', 2,
                       [[0.99, 0.9, 0.9, 0.01],
                        [0.01, 0.1, 0.1, 0.99]],
                       evidence=['Chover', 'Sprinkler'],
                       evidence_card=[2, 2])

model.add_cpds(cpd_chuva, cpd_sprinkler, cpd_grama)
print("Modelo_valido?", model.check_model())

infer = VariableElimination(model)

resultado1 = infer.query(variables=['GramaMolhada'], evidence={'Sprinkler': 1})
print(resultado1)

resultado2 = infer.query(variables=['Chover'], evidence={'GramaMolhada': 1})
print(resultado2)

##5 - 
# 1. O que muda nos resultados se a probabilidade de chuva for alterada para 70%?
#       R: Na implementação em questão, a probrabilidade de chuva ja está em 70%, como consta em "TabularCPD('Chover', 2, [[0.3], [0.7]])". 
#           isso significa P(Chover=0) = 0.3 (Não Chove) e P(Chover=1) = 0.7 (Chove).

# 2. O modelo continua válido se adicionarmos uma nova variável, como "Vento"?
#       R: O modelo pode continuar válido estruturalmente desde que se atendam algumas condições. Como manter o grafo como um DAG, definir a Tabela de Probabilidade Condicional,
#           atualizar as váriaveis das CPDs já existentes para incluir as variáveis do Vento, etc...

# 3. Em quais outros cenários profissionais Redes Bayesianas podem ser aplicadas?
#       R: Sendo uma ferramenta poderosa para modelar incerteza e probabilistica, algumas implementações podem ser feitas como: diagnósticos médicos, sistemas de recomendação,
#           análise de risco, reconhecimento de fala e processamento de linguagem natural, mercado financeiro, etc...

## Desafio de extensão

prob_chuva_extensao = 0.7
model_ext = DiscreteBayesianNetwork([
    ('Chover', 'GramaMolhada'), 
    ('Sprinkler', 'GramaMolhada'),
    ('GramaMolhada', 'SensorUmidade')
])

cpd_chuva_ext = TabularCPD('Chover', 2, [[1-prob_chuva_extensao], [prob_chuva_extensao]])
cpd_sprinkler_ext = TabularCPD('Sprinkler', 2, [[0.5], [0.5]])
cpd_grama_ext = TabularCPD('GramaMolhada', 2,
                       [[0.99, 0.9, 0.9, 0.01],
                        [0.01, 0.1, 0.1, 0.99]],
                       evidence=['Chover', 'Sprinkler'],
                       evidence_card=[2, 2])

# Nova CPD para SensorUmidade
# SensorUmidade: 0 = inativo; 1 = ativo
# GramaMolhada: 0 = seca; 1 = molhada
cpd_sensor = TabularCPD('SensorUmidade', 2,
                        [[0.90, 0.05],
                         [0.10, 0.95]],
                         evidence=['GramaMolhada'],
                         evidence_card=[2])

model_ext.add_cpds(cpd_chuva_ext, cpd_sprinkler_ext, cpd_grama_ext, cpd_sensor)
print("Modelo estendido válido?", model_ext.check_model())

infer_ext = VariableElimination(model_ext)

# Probabilidade a priori do sensor estar ativo
resultado_sensor_prior = infer_ext.query(variables=['SensorUmidade'])
print("\nP(SensorUmidade):")
print(resultado_sensor_prior)

# Se o sensor estiver ativo, qual a probabilidade da grama estar molhada?
resultado_gm_sensor_ativo = infer_ext.query(variables=['GramaMolhada'], evidence={'SensorUmidade': 1})
print("\nP(GramaMolhada | SensorUmidade = 1):")
print(resultado_gm_sensor_ativo)

# Se o sensor estar ativo, qual a probabilidade de ter chovido?
resultado_chuva_sensor_ativo = infer_ext.query(variables=['Chover'], evidence={'SensorUmidade': 1})
print("\nP(Chover | SensorUmidade = 1):")
print(resultado_chuva_sensor_ativo)

# Se o sensor esta ativo e o sprinkler desligado, qual a probabilidade de ter chovido?
resultado_chuva_sensor_sprinlçer = infer_ext.query(variables=['Chover'], evidence={'SensorUmidade': 1, 'Sprinkler': 0})
print("\nP(Chover | SensorUmidade = 1), Sprinkler = 0:")
print(resultado_gm_sensor_ativo)