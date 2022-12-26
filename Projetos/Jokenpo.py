from random import randint
from time import sleep

ops = ('pedra', 'papel', 'tesoura')

print('''Suas opcoes: 
      [0] Pedra
      [1] Papel
      [2] Tesoura'''
      )
def jogo(): 
      jog = int(input('Qual e a sua jogada? '))
      
      print('JO')
      sleep(1)
      print('KEN')
      sleep(1)
      print('PO')
      sleep(2)

      print('-=' * 11)
      comput = randint(0, 2)
      if jog == comput:
            return 'Empate'
  
      if win(jog, comput):
            return 'Voce ganhou'
  
      return 'Voce perdeu'

print('-=' * 11)

def win(player, opponent):
  
      if(player == 0 and opponent == 1) or (player == 1 and opponent == 2) or (player == 2 and opponent == 0):
            return True
      
print(jogo())
