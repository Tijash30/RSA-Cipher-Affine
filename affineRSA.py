import math

archivo = open("english-nouns.txt")
nue= archivo.readlines()

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

primos = [numero for numero in range(100, 1001) if es_primo(numero)]

def d(numero, modulo):
    def algoritmo_extendido_euclides(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            mcd, x, y = algoritmo_extendido_euclides(b, a % b)
            return (mcd, y, x - (a // b) * y)

    mcd, x, _ = algoritmo_extendido_euclides(numero, modulo)

    if mcd == 1:
        inverso = x % modulo
        return inverso
    else:
        print("no")

def convertir(numeros):    
    abc = " abcdefghijklmnopqrstuvwxyz"
    fra=""
    nums = [int(str(numeros[0]) + str(numeros[1])), int(str(numeros[2]) + str(numeros[3])), int(str(numeros[4]) + str(numeros[5]))]

    for i in range(3):
        for j in range(len(abc)):
            if nums[i] == j:
                fra+=abc[j]
        #print(abc[j], end = "")
    return fra

def getfinalnouns(frase):
    frasespacelist= frase.split()
    cont=0
    for i in frasespacelist:
        if i+"\n" in nue:
            cont+=1
    if cont>=3:
        return True


primos 

for x in primos:
  for y in primos:
    p = int(x)
    q = int(y)

    #p, q = 997, 983
    p2, q2 = p-1, q-1

    e = 2
    n = p2*q2

    while e < n:
        if math.gcd(e, n) == 1:
            break
        else:
            e = e+1

    llave = (p*q, e)

    inversa= d(e, n)
    decodificado = []
    cont = 0
    pal = ""
    incriptado = [182093, 156853, 178658, 316927, 395745, 64975, 277413, 193008, 39131, 411482]

    for i in incriptado:
        decodificado.append(str((pow(i, inversa) % (p*q))))
        if(len(decodificado[cont]) < 6):
          faltan = 6 - len(decodificado[cont]);
          for i in range(faltan):
            pal += "0"
          decodificado[cont] = pal + decodificado[cont]
        cont += 1
        pal = ""
    frastot=""
    for i in decodificado:
      fra= convertir(i)
      frastot+= fra
    condi= getfinalnouns(frastot)
    if condi:
        print(frastot)
        break
  

    
    
