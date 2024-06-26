import os
import cv2

import relative_path

# Variáveis globais para armazenar informações sobre a seleção de retângulos
pontos = []
selecionando_retangulo = False
retangulos = {}
imagem = None  # Definir imagem globalmente

# Função de callback para o evento de clique do mouse
def selecionar_retangulo(event, x, y, flags, parametros):
    global pontos, selecionando_retangulo, imagem_copia, retangulos

    # Se o botão esquerdo do mouse for pressionado, iniciar a seleção de um retângulo
    if event == cv2.EVENT_LBUTTONDOWN:
        pontos = [(x, y)]
        selecionando_retangulo = True
    
    # Se o mouse estiver se movendo durante a seleção, atualizar o retângulo
    elif event == cv2.EVENT_MOUSEMOVE and selecionando_retangulo:
        imagem_copia = imagem.copy()  # Copiar a imagem original
        for retangulo in retangulos.values():
            cv2.rectangle(imagem_copia, retangulo[0], retangulo[1], (0, 255, 0), 2)
        cv2.rectangle(imagem_copia, pontos[0], (x, y), (0, 255, 0), 2)
    
    # Se o botão esquerdo do mouse for liberado, finalizar a seleção de um retângulo
    elif event == cv2.EVENT_LBUTTONUP and selecionando_retangulo:
        pontos.append((x, y))
        # Armazenar as coordenadas do retângulo selecionado
        retangulos[len(retangulos)] = pontos
        selecionando_retangulo = False

def executar_retangulos_enem():
    global selecionando_retangulo, imagem_copia, imagem

    # Check if the regiao_enem folder already contains cropped images
    pasta_destino = 'regiao_enem'
    if os.path.exists(pasta_destino) and os.listdir(pasta_destino):
        print("As imagens já estão cortadas. Pulando o processo de seleção de retângulos.")
        return

    # Carregar a imagem do cartão de resposta
    imagem = cv2.imread(relative_path.resource_path('provas_enem/aluno-1.jpg'))

    # Redimensionar a imagem para uma largura de 600 pixels
    largura_nova = 1080
    proporcao = largura_nova / imagem.shape[1]
    altura_nova = int(imagem.shape[0] * proporcao)
    imagem = cv2.resize(imagem, (largura_nova, altura_nova))

    imagem_copia = imagem.copy()
# Rascunho
    # local = [(x1, y1), (x2, y2)]
    # regiao = imagem[y1:y2, x1:x2]

    # MATRICULA
    regiao = imagem[290:502, 167:450]
    cv2.imwrite(os.path.join(pasta_destino, f'regiao_{1}.jpg'), regiao)

    # Cod da Prova
    regiao = imagem[286:422, 621:900]
    cv2.imwrite(os.path.join(pasta_destino, f'regiao_{2}.jpg'), regiao)

    # Area 3
    regiao = imagem[587:1291, 140:281]
    cv2.imwrite(os.path.join(pasta_destino, f'regiao_{3}.jpg'), regiao)

    # Area 4
    regiao = imagem[589:1291, 366:514]
    cv2.imwrite(os.path.join(pasta_destino, f'regiao_{4}.jpg'), regiao)

    # Area 5
    regiao = imagem[590:1291, 595:738]
    cv2.imwrite(os.path.join(pasta_destino, f'regiao_{5}.jpg'), regiao)

    # Area 6
    regiao = imagem[590:1291, 826:975]
    cv2.imwrite(os.path.join(pasta_destino, f'regiao_{6}.jpg'), regiao)

    print(f"Regiões recortadas salvas na pasta '{pasta_destino}'.")


executar_retangulos_enem()

