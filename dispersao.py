def amplitude(x): # AMPLITUDE DE UM VETOR X
    maximo = x[0]
    minimo = x[0]
    for i in x:
        if i != x[0]:
            if i > maximo:
                maximo = i
            if i < minimo:
                minimo = i
    return maximo - minimo

def desvioMedio(x, posicao, n): # DESVIO MEDIO DE UM VETOR X
    soma = 0
    for i in x:
        soma += abs(i - posicao)
    return soma / n

def varianciaA(x, posicao, n): # VARIANCIA AMOSTRAL DE UM VETOR X
    n = n - 1
    desvioQuadrado = 0
    for i in x:
        desvioQuadrado += (i - posicao) ** 2
    return desvioQuadrado / n

def varianciaP(x, posicao, n): # VARIANCIA POPULACIONAL DE UM VETOR X
    desvioQuadrado = 0
    for i in x:
        desvioQuadrado += (i - posicao) ** 2
    return desvioQuadrado / n

def desvioPadrao(variancia): # DESVIO PADRÃO DE UM VETOR X
    return variancia ** (1 / 2)

def erroPadrao(desvioPadrao, n): # ERRO PADRÃO DA MEDIA AMOSTRAL DE UM VETOR X
    return desvioPadrao / (n ** (1 / 2))