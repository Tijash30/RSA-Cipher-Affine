def gcd(a, b):
    modulo= a%b
    if modulo==0:
        return b
    else:
        return gcd(b, modulo)
    
def getE(n):
    e = 2
    while e < n:
        if gcd(e, n) == 1:
            break
        else:
            e = e+1
    return e

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def getInverse(numero, modulo):
    def exteuclides(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            mcd, x, y = exteuclides(b, a % b)
            return (mcd, y, x - (a // b) * y)

    mcd, x, _ = exteuclides(numero, modulo)

    if mcd == 1:
        inverso = x % modulo
        return inverso
    
def decodify(incriptado,e, n, p, q):
    inversa= getInverse(e, n)
    decodificado = []
    cont = 0
    pal = ""
    for i in incriptado:
        decodificado.append(str((pow(i, inversa) % (p*q))))
        if(len(decodificado[cont]) < 6):
            faltan = 6 - len(decodificado[cont]);
            for i in range(faltan):
                pal += "0"
            decodificado[cont] = pal + decodificado[cont]
        cont += 1
        pal = ""
    return decodificado

def convertir(numeros):    
    abc = " abcdefghijklmnopqrstuvwxyz"
    nums = [int(str(numeros[0]) + str(numeros[1])), int(str(numeros[2]) + str(numeros[3])), int(str(numeros[4]) + str(numeros[5]))]

    for i in range(3):
        for j in range(len(abc)):
            if nums[i] == j:
                print(abc[j], end = "")


def getDesFrase(listi):
    for p in primos:
        for q in primos:
            n= (p-1)*(q-1)
            e= getE(n)
            listanumfi= decodify(listi, e, n, p, q)
            convertir(listanumfi)


primos = [numero for numero in range(100, 1001) if es_primo(numero)]
#print(primos)
frase= [28300, 234270, 36103, 115456, 77090, 125987, 31388, 155622]
getDesFrase(frase)

"""archivo = open("frasesRSA.txt")
nue= archivo.readlines()
for i in nue:
    for j in i:
        print(j)"""