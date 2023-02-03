import time

def regres(x):
  while x:
    min, sec = divmod(x, 60)
    timer = '{:02d}:{:02d}'.format(min, sec)
    print(timer, end="\r")
    time.sleep(1)
    x -= 1
    
  print('Feito!!')
  
x = input('Tempo em segundos: ')
regres(int(x))