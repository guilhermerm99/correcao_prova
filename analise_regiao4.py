import cv2
import relative_path

def executar_analise_regiao4():

    # Função para binarizar a imagem
    def binarizar_imagem(imagem):
        # Converter a imagem para tons de cinza
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Aplicar uma operação de limiarização para binarizar a imagem
        _, imagem_binarizada = cv2.threshold(imagem_gray, 70, 255, cv2.THRESH_BINARY_INV)

        return imagem_binarizada

    # Função para extrair as respostas das questões da região 3
    def extrair_respostas_regiao_3(regiao_binarizada):
        respostas = []
        for linha in range(25):  # Ajuste para 25 linhas
            for coluna in range(5):  # Ajuste para 5 colunas
                x1 = coluna * 50
                y1 = linha * 50
                x2 = (coluna + 1) * 50
                y2 = (linha + 1) * 50

                circulo = regiao_binarizada[y1:y2, x1:x2]
                altura, largura = circulo.shape[:2]
                area_circulo = cv2.countNonZero(circulo)
                if area_circulo > 0.15 * altura * largura:
                    resposta = chr(65 + coluna)  # Converte o índice da coluna para a letra correspondente ('A' a 'E')
                    respostas.append(resposta)

        return respostas

    # Ler a imagem da região 3
    imagem_regiao3 = cv2.imread(relative_path.resource_path('regiao_enem/regiao_4.jpg'))

    # Redimensionar a imagem (aumentar 3x)
    imagem_regiao3 = cv2.resize(imagem_regiao3, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)

    # Binarizar a imagem da região 3
    imagem_binarizada3 = binarizar_imagem(imagem_regiao3)

    # Exibir a imagem binarizada da região 3
    #cv2.imshow('Imagem Binarizada Região 3', imagem_binarizada3)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Extrair as respostas das questões da imagem binarizada da região 3
    respostas_regiao3 = extrair_respostas_regiao_3(imagem_binarizada3)

    # Imprimir as respostas das questões
    for i, resposta in enumerate(respostas_regiao3, start=25):
        print(f'Questão {i+1}: {resposta}')


# Chamada da função principal
if __name__ == "__main__":
    executar_analise_regiao4()

