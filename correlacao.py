def covarianciaA(x, y, mediaX, mediaY, n): # COVARIANCIA AMOSTRAL ENTRE 2 VETORES X E Y
    soma = 0
    for i in range(0, n):
        soma += (x[i] - mediaX) * (y[i] - mediaY)
    return soma / (n - 1)

def covarianciaP(x, y, mediaX, mediaY, n): # COVARIANCIA POPULACIONAL ENTRE 2 VETORES X E Y
    soma = 0
    for i in range(0, n):
        soma += (x[i] - mediaX) * (y[i] - mediaY)
    return soma / n

def coeficienteCorrelacao(sigmaX, sigmaY, covariancia): # COEFICIENTE DE CORRELAÇÃO LINEAR DE PEARSON
    return covariancia / (sigmaX * sigmaY)