import random
import subprocess
import platform
from playsound import playsound
platform.system()
x = random.randrange(0,50)
cont = 0
audio_file = "palmas.wav"
def portuguese():
    for cont in range(10): 
    
        y = int (input("Escolha um número de 0 a 50\n"))
    
        if y == x:
            print ("Você acertou")
            if platform.system() == 'Windows':
                playsound('palmas.wav')
            else:
                return_code = subprocess.call(["afplay", audio_file])
            break
        elif (y>x) and (y<=50):
            print ("Nº número alto, tente um número menor.\n")
        elif (y<x):
            print ("Nº número baixo, tente um número maior.\n")
        elif (y>50):
            print ("Número maior que 50, tente novamente.\n")
    
        cont += 1
    print ("Fim de jogo")


def english():
    for cont in range(10): 
    
        y = int (input("Choose a number between 0 and 50\n"))
    
        if y == x:
            print ("You won!")
            if platform.system() == 'Windows':
                playsound('palmas.wav')
            else:
                return_code = subprocess.call(["afplay", audio_file])
            break
        elif (y>x) and (y<=50):
            print ("high number, try a smaller.\n")
        elif (y<x):
            print ("low number, try a higher.\n")
        elif (y>50):
            print ("above 50, try again.\n")
    
        cont += 1
    print ("End game")
    print("Escolha uma língua / Choose a linguage")
choose = int(input("""[1] Portuguese
[2] English \n"""))
if choose == 1:
    portuguese()
else:
    english()
print("Escolha uma língua / Choose a linguage")
