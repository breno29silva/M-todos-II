from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

def detectarBordas(img):
    M, N = img.shape
    imagemResultado = np.zeros((M, N))

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            corAnterior = img[i][j - 1]
            if corAnterior > 128:
                corAnterior = 1
            else:
                corAnterior = 0
            corPosterior = img[i][j + 1]
            if corPosterior > 128:
                corPosterior = 1
            else:
                corPosterior = 0
            derivada = corPosterior - corAnterior
            if derivada == 1:
                imagemResultado[i][j] = 1
            else:
                imagemResultado[i][j] = 0

    for j in range(1, N - 1):
        for i in range(1, M - 1):
            corAnterior = img[i - 1][j]
            if corAnterior > 128:
                corAnterior = 1
            else:
                corAnterior = 0
            corPosterior = img[i + 1][j]
            if corPosterior > 128:
                corPosterior = 1
            else:
                corPosterior = 0
            derivada = corPosterior - corAnterior
            if derivada == 1:
                imagemResultado[i][j] = 1

    return imagemResultado

# abrindo imagem colorida e convertendo imagem para tom de cinza
img = Image.open('circle.png').convert('L')
img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)

image = mpimg.imread("out.jpg")
percorrerMatriz(np.array(image))

image = detectarBordas(image)

output_image(image)
