def gcd(a, b):
    modulo= a%b
    if modulo==0:
        return b
    else:
        return gcd(b, modulo)

def getE():
    e = 2
    while e < n:
        if gcd(e, n) == 1:
            break
        else:
            e = e+1
    return e

def checkBoth(p, q):
    def isPrime(n):
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True
    if isPrime(p) and isPrime(q):
        return True
    else: 
        return False

def pal(frase):
    listi = []
    abc = " abcdefghijklmnopqrstuvwxyz"
    finallist=[]
    for i in range(len(frase)):
        for j in range(len(abc)):
            if frase[i] == abc[j]:
                if(j < 10):
                    listi.append(str(0) + str(j))
                else:
                    listi.append(str(j))

    aux=[]
    while len(listi)%3!=0:
        aux.append(listi.pop())
    if len(aux)==2:
        listi.append("00")
        listi.append(aux[1])
        listi.append(aux[0])
    elif len(aux)==1:
        listi.append("00")
        listi.append("00")
        listi.append(aux[0])

    for i in range(0, len(listi), 3):
        finallist.append(listi[i]+listi[i+1]+listi[i+2])
    
    return finallist
    
def getencryptMess(p, q, e):
    listifinal= pal(frase)
    print("Groups of 3:\t", listifinal)
    for i in range(len(listifinal)):
        aux= int(listifinal[i])
        listifinal[i]= aux

    incriptado = []

    for i in listifinal:
        incriptado.append(pow(i, e) % (p*q))
    print("Encrypted:\t",incriptado)
    return incriptado

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

def decodify(incriptado,e, n):
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



frase = input("Input a frase:\t")
p = int(input("p:\t"))
q= int(input("q:\t"))
if checkBoth(p, q):
    n = (p-1)*(q-1)
    e= getE()
    print("e:\t",e)

    incriptado2= getencryptMess(p, q, e)
    decodificado= decodify(incriptado2, e, n)

    print("\nDesencriptado: ", end = "")

    for i in decodificado:
        convertir(i)
else:
    print("a number is not prime")