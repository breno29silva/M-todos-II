# biblioteca matemática para solucionar as equações
import newton_contes

# Valor exato da integral do polinomio
VALOR_EXATO = 17.8764703
# Tolerância defina na lista
TOLERANCIA = pow(10, -6)
# Quantidade de passos que será incrementado
INCREMENTO = 1


def erroRelativo(aproximado):
    return abs(aproximado - VALOR_EXATO) / VALOR_EXATO


def resolver(formulaNewton, a, b):
    '''Variando n ate encontrar o tolerancia pedida'''
    n = 0
    resultado = 0
    loop = 0

    while erroRelativo(resultado) > TOLERANCIA:
        loop += 1
        resultado = dividirEspaco(formulaNewton, a, b, n)

        n += INCREMENTO

    return loop


def dividirEspaco(formulaNewton, a, b, n):
    '''Dividindo o espaco de a ate em b em n pedacos'''
    i = 0
    resultado = 0
    while i < n:
        delta = (b - a) / n
        xInicial = a + i * delta
        xFinal = xInicial + delta

        if 'f' in formulaNewton:
            if 'g01f' == formulaNewton:
                resultado += newton_contes.grau_01_funcao_fechada(xInicial, xFinal, delta)
            elif 'g02f' == formulaNewton:
                resultado += newton_contes.grau_02_funcao_fechada(xInicial, xFinal, delta)
            elif 'g03f' == formulaNewton:
                resultado += newton_contes.grau_03_funcao_fechada(xInicial, xFinal, delta)
            elif 'g04f' == formulaNewton:
                resultado += newton_contes.grau_04_funcao_fechada(xInicial, xFinal, delta)
        else:
            if 'g01a' == formulaNewton:
                resultado += newton_contes.grau_01_funcao_aberta(xInicial, delta)
            elif 'g02a' == formulaNewton:
                resultado += newton_contes.grau_02_funcao_aberta(xInicial, delta)
            elif 'g03a' == formulaNewton:
                resultado += newton_contes.grau_03_funcao_aberta(xInicial, delta)
            elif 'g04a' == formulaNewton:
                resultado += newton_contes.grau_04_funcao_aberta(xInicial, delta)

        i += 1

    return resultado


def main():
    for i in range(4):
        funcaof = 'g0' + str(i + 1) + 'f'
        funcaoa = 'g0' + str(i + 1) + 'a'
        print(
            'Total de particoes para formula de Grau {} fechada: {} iteracoes'.format((i + 1), resolver(funcaof, 0, 1)))
        print(
            'Total de particoes para formula de Grau {} aberta: {} iteracoes'.format((i + 1), resolver(funcaoa, 0, 1)))
        print('************************************************************')


if __name__ == '__main__':
    print('************************** CALCULANDO **************************')
    main()
