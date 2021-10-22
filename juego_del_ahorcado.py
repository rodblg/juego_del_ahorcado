import random
from os import system, name
from time import sleep

def clear():
    if name == 'posix':
        sleep(2)
        _ = system('clear')

def run():
    print("Bienvenido al juego del ahorcado, ¿estás listo para aventurarte?: Y/N")
    resp = input().upper()
    #assert (), "Ingresa un caracter"
    if resp== 'Y':
        print('Que comience el juego')
        print('---------------------')
        juego()
    else:
        print('Vuelve pronto')

def pal(palabra):
    p = ['_' for letra in range(1,len(palabra))]
    #print(palabra)
    print(p)
    print('\n')
    #print(len(p))
    a = 0
    for e in range(1000):
        var = 0
        po = []
        for i in range(len(p)):
            if p[i] == '_':
                po.append(i)
                #print(po)  
        if a >= len(p):
            print('Tenemos un ganador, muchas felicidades')
            break    
                      
        var = input('Ingresa la letra: ').upper()
        for j in po:
            if palabra[j] == var:
                p[j] = var
                a = a + 1
        print(p)
    
def juego():
    #Accedemos a nuestra base de datos de palabras
    with open("./archivos/data.txt", "r", encoding='utf-8') as f:
        opciones = [palabra for palabra in f]
        num = random.randint(1, len(opciones))    
        palabra = opciones[num]
        #print(opciones[num])
        clear()
        print('Adivina la palabra\n')
        pal(palabra.upper())

if __name__ == '__main__': 
    run()
    