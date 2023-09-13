'''
Constantes: "variaveis que não vão mudar ao decorrer da escrita do programa

Muitas condições no mesmo if são praticas ruins. 

    <- contagem de complexidade (ruim)
    
    sempre pensar em uma forma de simplificar o código e minimizar longas expressões em uma linha
'''

# variaveis que podem mudar podem ser escritas normalmente 
velocidade_carro = 31 # velocidade atual do carro

local_do_carro = 100 # local em que o carro esta na estrada
'''
Programa para medir a velocidade do carro em uma faixa do radar
'''
# Usamos caixa alta para deifinir variaveis constantes
RADAR_1 = 60 # velocidade maxima do radar
LOCAL_1 = 100 # local one o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pegar 

Vel_carro_pass_radar_1 = velocidade_carro > RADAR_1

# verificando apartir do ponto do radar que é o local 100, criamos uma faixa de +1 e - 1 para criar o espaço de captura do radar
# a barra invertida permite quebrar a linha de código
carro_passou_radar_1 = local_do_carro >= (LOCAL_1 - RADAR_RANGE) and local_do_carro <= (LOCAL_1 + RADAR_RANGE) 

carro_multado_radar_1 = carro_passou_radar_1 and Vel_carro_pass_radar_1

if Vel_carro_pass_radar_1:
    print("Carro passou no radar 1")

if carro_passou_radar_1:
    print('Carro passou no radar1')
    
if carro_multado_radar_1:
    print('Carro multado no Radar 1')