from posicao import * # PARAMETROS DE POSIÇÃO
from dispersao import * # PARAMETROS DE DISPERSÃO
from correlacao import * # PARAMETROS DE CORRELAÇÃO

class Vetor():
    def __init__(self, dados, posicao = 'media', tipo = 'populacional'):
        self.dados = dados
        self.n = len(dados)
        self.tipo = tipo
        # POSICAO:
        if posicao == 'media':
            self.posicao = media(self.dados, self.n)
        elif posicao == 'mediaQuadratica':
            self.posicao = mediaQuadratica(self.dados, self.n)
        elif posicao == 'mediana':
            self.posicao = mediana(self.dados, self.n)
        elif posicao == 'moda':
            self.posicao = moda(self.dados)
        # DISPERSÃO:
        self.amplitude = amplitude(self.dados)
        self.desvioMedio = desvioMedio(self.dados, self.posicao, self.n)
        if tipo == 'amostral':
            self.variancia = varianciaA(self.dados, self.posicao, self.n)
        elif tipo == 'populacional':
            self.variancia = varianciaP(self.dados, self.posicao, self.n)
        self.desvioPadrao = desvioPadrao(self.variancia)
        self.erroPadrao = erroPadrao(self.desvioPadrao, self.n)
class Correlacao():
    def __init__(self, DadosX, DadosY):
        if DadosX.n == DadosY.n:
            self.dados = [DadosX.dados, DadosY.dados]
            self.n = DadosX.n
            if DadosX.tipo == 'amostral':
                self.covariancia = covarianciaA(DadosX.dados, DadosY.dados, DadosX.posicao, DadosY.posicao, self.n)
            elif DadosX.tipo == 'populacional':
                self.covariancia = covarianciaP(DadosX.dados, DadosY.dados, DadosX.posicao, DadosY.posicao, self.n)
            self.coeficienteCorrelacao = coeficienteCorrelacao(DadosX.desvioPadrao, DadosY.desvioPadrao, self.covariancia)
        else:
            print('NÃO É POSSIVEL CORRELACIONAR !!!') # <--- ERRO

# TESTES:
DadosX = Vetor([21, 19, 25, 19, 21, 18, 20, 20, 19, 20, 25, 20, 20, 20])
DadosY = Vetor([78, 64, 83, 59.2, 71, 70, 60, 55, 45, 120, 67, 64, 69, 83])
DadosXY = Correlacao(DadosX, DadosY)

print(DadosX.dados)
print(DadosX.n)
print(DadosX.posicao)
print(DadosX.variancia)
print(DadosX.desvioPadrao, '\n')

print(DadosY.dados)
print(DadosY.n)
print(DadosY.posicao)
print(DadosY.variancia)
print(DadosY.desvioPadrao, '\n')

print(DadosXY.dados)
print(DadosXY.n)
print(DadosXY.covariancia)
print(DadosXY.coeficienteCorrelacao)