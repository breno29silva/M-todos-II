# biblioteca matemática para solucionar as equações

import NewtonContes as nc

# Valor exato da integral do polinomio
VALOR_EXATO = 17.8764703
# Tolerância defina na lista
TOLERANCIA = pow(10, -6)
# Quantidade de passos que será incrementado
INCREMENTO = 1


def erroRelativo(aproximado):
    return (abs(aproximado - VALOR_EXATO) / VALOR_EXATO)


def resolver(a, b):
    n = 0
    resultado = 0

    while erroRelativo(resultado) > TOLERANCIA:
        print(erroRelativo(resultado))
        i = 0
        resultado = 0
        n += INCREMENTO
        while i < n:
            delta = (b - a) / n;
            xInicial = a + i * delta
            xFinal = xInicial + delta

            resultado += nc.grau_03_funcao_aberta(xInicial, delta)

            i += 1

    return resultado, n


print(resolver(0, 1))
