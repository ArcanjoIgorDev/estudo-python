"""
CONSTANTE = "Variáveis" que não vão mudar

Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 40 # velocidade atual do carro
local_carro = 99 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega


vel_carr_passou_radar_1= velocidade > RADAR_1

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carr_passou_radar_1:
    print('Velocidade do carro passou do radar 1')


if carro_multado_radar_1 and vel_carr_passou_radar_1:
    print('carro multado em radar 1')







