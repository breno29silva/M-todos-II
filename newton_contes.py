import math


def resolverPolinomio(valor):
    '''Resolvendo a formula:(sen(2x) + 4 x^2 + 3 x)^2'''
    interno = math.sin(2 * valor) + 4 * math.pow(valor, 2) + 3 * valor
    return pow(interno, 2)


# *********************************  Newton Contes Fechada  *********************************
def grau_01_funcao_fechada(xInicial, xFinal, delta):
    return (delta / 2) * (resolverPolinomio(xInicial) + resolverPolinomio(xFinal))


def grau_02_funcao_fechada(xInicial, xFinal, delta):
    h = delta / 2
    meio = 4 * resolverPolinomio(xInicial + h)
    return (delta / 6) * (
            resolverPolinomio(xInicial) + meio + resolverPolinomio(xFinal))


def grau_03_funcao_fechada(xInicial, xFinal, delta):
    h = delta / 3
    meio = 3 * resolverPolinomio(xInicial + h) + 3 * resolverPolinomio(xInicial + 2 * h)
    return (delta / 8) * (
            resolverPolinomio(xInicial) + meio + resolverPolinomio(xFinal))


def grau_04_funcao_fechada(xInicial, xFinal, delta):
    h = delta / 4

    meio = 64 / 3 * resolverPolinomio(xInicial + h) + 8 * resolverPolinomio(
        xInicial + 2 * h) + 64 / 3 * resolverPolinomio(xInicial + 3 * h)

    return (delta / 60) * (14 / 3 * resolverPolinomio(xInicial) + meio + 14 / 3 * resolverPolinomio(xFinal))


# *********************************  Newton Contes Aberta  *********************************
def grau_01_funcao_aberta(xInicial, delta):
    h = delta / 3
    return (delta / 2) * (resolverPolinomio(xInicial + h) + resolverPolinomio(xInicial + 2 * h))


def grau_02_funcao_aberta(xInicial, delta):
    h = delta / 4
    meio = resolverPolinomio(xInicial + 2 * h)
    return (delta / 3) * (
            2 * resolverPolinomio(xInicial + h) - meio + 2 * resolverPolinomio(xInicial + 3 * h))


def grau_03_funcao_aberta(xInicial, delta):
    h = delta / 5
    meio = resolverPolinomio(xInicial + 2 * h) + resolverPolinomio(xInicial + 3 * h)
    return (delta / 24) * (
            11 * resolverPolinomio(xInicial + h) + meio + 11 * resolverPolinomio(xInicial + 4 * h))


def grau_04_funcao_aberta(xInicial, delta):
    h = delta / 6
    meio = -21 * resolverPolinomio(xInicial + 2 * h) + 39 * resolverPolinomio(
        xInicial + 3 * h) - 21 * resolverPolinomio(xInicial + 4 * h)
    return (delta / 30) * (
            33 / 2 * resolverPolinomio(xInicial + h) + meio + 33 / 2 * resolverPolinomio(xInicial + 5 * h))
