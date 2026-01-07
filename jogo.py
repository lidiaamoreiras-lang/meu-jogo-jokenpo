import random
from pyscript import Element

vitorias_voce = 0
vitorias_robo = 0

def jogar(escolha_usuario):
    global vitorias_voce, vitorias_robo
    
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolha_robo = random.choice(opcoes)
    
    status = Element("status").element
    resultado = ""
    
    # Lógica do Jogo
    if escolha_usuario == escolha_robo:
        resultado = f"Empate! Ambos escolheram {escolha_usuario}"
        status.style.color = "white"
    elif (escolha_usuario == 'Pedra' and escolha_robo == 'Tesoura') or \
         (escolha_usuario == 'Papel' and escolha_robo == 'Pedra') or \
         (escolha_usuario == 'Tesoura' and escolha_robo == 'Papel'):
        resultado = f"Você Ganhou! {escolha_usuario} vence {escolha_robo}"
        status.style.color = "#4ade80" # Verde
        vitorias_voce += 1
    else:
        resultado = f"Robô Ganhou! {escolha_robo} vence {escolha_usuario}"
        status.style.color = "#f87171" # Vermelho
        vitorias_robo += 1
        
    status.innerText = resultado
    Element("placar").element.innerText = f"Você: {vitorias_voce} | Robô: {vitorias_robo}"