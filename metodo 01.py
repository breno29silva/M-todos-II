import numpy as np
import cv2

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

def main():
    # abrindo imagem colorida e convertendo imagem para tom de cinza
    img = cv2.imread('cinza.png', cv2.IMREAD_GRAYSCALE)

    imageModificada = detectarBordas(img)

    cv2.imshow("Original", img)
    cv2.imshow("Modifcada", imageModificada)

    cv2.waitKey(0)

if __name__ == '__main__':
  main()