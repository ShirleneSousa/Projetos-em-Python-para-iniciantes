import random 

def adv(x):
  random_n = random.randint(1, x)
  adv = 0
  while adv != random_n:
    adv = int(input('Numero entre 1 e {x}: '))
    if adv < random_n:
      print('Tente novamente, valor pequeno.')
    elif adv > random_n:
      print('Tente novamente, valor grande.')
      
  print(f'Parabens. Voce acertou o numero {random_n} corretamente')
  
adv(100)
    
