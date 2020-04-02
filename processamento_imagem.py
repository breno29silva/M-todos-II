import cv2
import numpy as np


def detectarBorda(matriz):
    # Adicionando linha e coluna namatriz
    novaMatriz = redimencionarImagem(matriz)

    linhasNovaMatriz, colunasNovaMatriz = novaMatriz.shape
    matrizResultado = np.zeros((matriz.shape[0], matriz.shape[1]))

    for i in range(1, linhasNovaMatriz - 1):
        for j in range(1, colunasNovaMatriz - 1):
            linha = abs(novaMatriz[i][j + 1] - novaMatriz[i][j - 1])
            coluna = abs(novaMatriz[i + 1][j] - novaMatriz[i - 1][j])
            diagonalPrincipal = abs(novaMatriz[i + 1][j + 1] - novaMatriz[i - 1][j - 1])
            diagonalSecundaria = abs(novaMatriz[i - 1][j + 1] - novaMatriz[i + 1][j - 1])

            matrizResultado[i - 1][j - 1] = (coluna + linha + diagonalPrincipal + diagonalSecundaria) / 16

    return matrizResultado


def redimencionarImagem(matriz):
    novaMatriz = np.c_[np.zeros(matriz.shape[0]), matriz, np.zeros(matriz.shape[0])]  # Adicionando colunas
    novaMatriz = np.r_[
        [np.zeros(novaMatriz.shape[1])], novaMatriz, [np.zeros(novaMatriz.shape[1])]]  # Adicionando linhas

    return novaMatriz


def main():
    NOME_IMAGEM = 'rosto_3.jpg'

    # Leitura da imagem em tom de cinza
    img = cv2.imread(NOME_IMAGEM, 0)

    # transformando a imagem para binaria (0 e 255)
    imagemBinaria = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

    detectado = detectarBorda(np.array(imagemBinaria))

    cv2.imshow("Preto e branco", imagemBinaria)
    cv2.imshow("Modificada", detectado)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
