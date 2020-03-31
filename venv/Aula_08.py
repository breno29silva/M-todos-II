# biblioteca matemática para solucionar as equações
from sympy import *

init_printing(pretty_print=true)
x = Symbol('x')
y = Function('y')

pol = (sin(2 * x) + 4 * x ** 2 + 3 * x) ** 2


def valoresBasicos(pol):
    '''Retorna o f(0) e f(1)'''
    resultados = list()

    resultados.append(pol.evalf(subs={x: 0}))
    resultados.append(pol.evalf(subs={x: 1}))

    return resultados


# Newton Contes Fechada
def grau_01():
    '''(DeltaX / 2) * (f(0) + f(1))'''

    print('Resultado {}'.format(((1/2) / 2) * (valoresBasicos(pol)[0] + valoresBasicos(pol)[1])))


grau_01()
