import random

def GuessNumber(x):
  number = random.randint(1, x)
  guess = 0
  while guess != number:
    guess = int(input(f'Qual é o numero entre 1 e {x}: '))
    if guess < number:
      print('Tente novamente. Número pequeno')
    elif guess > number:
      print('Tente novamente. Número grande')
      
  print(f'Parabéns. Você acertou o número {number} corretamente')
      
    
GuessNumber(10)
  
