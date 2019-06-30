def media(x, n): # MEDIA DE UM VETOR X
    soma = 0
    for i in x:
        soma += i
    return soma / n

def mediaQuadratica(x, n): # MEDIA QUADRATICA DE UM VETOR X
    soma = 0
    for i in x:
        soma += i ** 2
    return (soma / n) ** (1 / 2)

def mediana(x, n): # MEDIANA DE UM VETOR X
    ordem = sorted(x) # Por em ordem crescente
    print(ordem)
    if n % 2 == 0: # Par
        x1 = ordem[int(n / 2 - 1)]
        x2 = ordem[int(n / 2)]
        resultado = (x1 + x2) / 2
    else: # Impar
        resultado = ordem[int(n / 2)]
    return resultado

def moda(x): # MODA DE UM VETOR X
    resultado = ['']
    temp1 = 0
    for i in x:
        temp2 = 0
        for j in x:
            if i == j:
                temp2 += 1
        if temp2 > temp1:
            temp1 = temp2
            resultado = [i]
        elif temp2 == temp1:
            if i not in resultado:
                resultado.append(i)
    return resultado