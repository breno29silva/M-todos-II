from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

arquivo = open('nome.txt', 'w')


def percorrerMatriz(matriz):
    for i in matriz:
        for j in i:
            arquivo.writelines(str(j) + ' ')
            #print(j, end=' ')
        #print()
        arquivo.writelines('\n')


def output_image(name):
    plt.imshow(name)
    plt.show()


# abrindo imagem colorida e convertendo imagem para tom de cinza
img = Image.open('cubo_2.jpg').convert('L')

percorrerMatriz(np.array(img))
