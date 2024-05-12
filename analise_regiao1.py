import cv2
import relative_path

def executar_analise_regiao1():
    # Função para binarizar a imagem
    def binarizar_imagem(imagem):
        # Converter a imagem para tons de cinza
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Aplicar uma operação de limiarização para binarizar a imagem
        _, imagem_binarizada = cv2.threshold(imagem_gray, 70, 255, cv2.THRESH_BINARY_INV)

        return imagem_binarizada

    # Função para extrair a matrícula da imagem binarizada
    def extrair_matricula(regiao_binarizada):
        matricula = ''
        for linha in range(8):
            digitos = []
            for coluna in range(10):
                x1 = coluna * 60
                y1 = linha * 110
                x2 = coluna * 60 + 30
                y2 = linha * 110 - 18

                circulo = regiao_binarizada[y1:y2, x1:x2]
                cv2.imshow('circulo', circulo)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                altura, largura = circulo.shape[:2]
                area_circulo = cv2.countNonZero(circulo)
                if area_circulo > 0.15* altura * largura:
                    digitos.insert(0, str(coluna))  # Inserir o dígito no início da lista

            matricula += ''.join(digitos)

        return matricula[::-1]  # Inverter a matrícula antes de retornar

    # Ler a imagem da região
    imagem_regiao = cv2.imread(relative_path.resource_path('regiao_enem/regiao_1.jpg'))

    # Redimensionar a imagem (aumentar 3x)
    imagem_regiao = cv2.resize(imagem_regiao, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)

    # Binarizar a imagem da região
    imagem_binarizada = binarizar_imagem(imagem_regiao)

    # Exibir a imagem binarizada
    # cv2.imshow('Imagem Binarizada', imagem_binarizada)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Extrair a matrícula da imagem binarizada
    matricula = extrair_matricula(imagem_binarizada)
    matricula_pronta = matricula[::-1] # Hugo alterou aqui

    # Imprimir a matrícula invertida
    print(f'Matrícula: {matricula_pronta}') # Hugo alterou aqui



# Chamada da função principal
if __name__ == "__main__":
    executar_analise_regiao1()


