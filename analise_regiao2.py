import cv2
import relative_path

def executar_analise_regiao2():
    # Função para binarizar a imagem
    def binarizar_imagem(imagem):
        # Converter a imagem para tons de cinza
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Aplicar uma operação de limiarização para binarizar a imagem
        _, imagem_binarizada = cv2.threshold(imagem_gray, 70, 255, cv2.THRESH_BINARY_INV)

        return imagem_binarizada

    # Função para extrair o código da prova da imagem binarizada
    def extrair_codigo_prova(regiao_binarizada):
        codigo_prova = ''
        count_circulos = 0  # Contador de círculos preenchidos
        for linha in range(5):  # Ajuste para 5 linhas
            for coluna in range(10):
                x1 = coluna * 50
                y1 = linha * 50
                x2 = (coluna + 1) * 50
                y2 = (linha + 1) * 50

                circulo = regiao_binarizada[y1:y2, x1:x2]
                altura, largura = circulo.shape[:2]
                area_circulo = cv2.countNonZero(circulo)
                if area_circulo > 0.10 * altura * largura:
                    codigo_prova += str(coluna)  # Adicionar o dígito ao código da prova
                    count_circulos += 1
                    if count_circulos >= 5:
                        break  # Interromper o loop após encontrar cinco círculos preenchidos
            if count_circulos >= 5:
                break  # Interromper o loop externo se já tivermos cinco círculos preenchidos
        return codigo_prova


    # Ler a imagem da região 2 (Código da Prova)
    imagem_regiao2 = cv2.imread(relative_path.resource_path('regiao_enem/regiao_2.jpg'))

    # Redimensionar a imagem (aumentar 3x)
    imagem_regiao2 = cv2.resize(imagem_regiao2, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)

    # Binarizar a imagem da região 2
    imagem_binarizada2 = binarizar_imagem(imagem_regiao2)

    # Exibir a imagem binarizada da região 2
    #cv2.imshow('Imagem Binarizada Região 2 (Código da Prova)', imagem_binarizada2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Extrair o código da prova da imagem binarizada da região 2
    codigo_prova = extrair_codigo_prova(imagem_binarizada2)

    # Imprimir o código da prova
    print(f'Código da Prova: {codigo_prova}')

    

# Chamada da função principal
if __name__ == "__main__":
    executar_analise_regiao2()


