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

    # Criar uma janela para exibir a imagem
    cv2.namedWindow('Selecione os Retângulos')
    cv2.setMouseCallback('Selecione os Retângulos', selecionar_retangulo)

    # Loop principal
    while True:
        cv2.imshow('Selecione os Retângulos', imagem_copia)
        
        # Aguardar pressionamento de tecla
        tecla = cv2.waitKey(1) & 0xFF
        
        # Finalizar a seleção de retângulos se a tecla 'q' for pressionada
        if tecla == ord('q'):
            break

    # Fechar todas as janelas
    cv2.destroyAllWindows()

    # Verificar se os retângulos foram selecionados e armazenar suas coordenadas
    if retangulos:
        print("Retângulos selecionados com sucesso!")
        print("Coordenadas dos retângulos:")
        for idx, pontos in retangulos.items():
            print(f"Retângulo {idx + 1}: {pontos}")
        
        # Criar o diretório "regiao_enem" se ele não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
            print(f"Diretório '{pasta_destino}' criado com sucesso!")
        
        # Recortar as regiões correspondentes dos retângulos selecionados
        for idx, pontos in retangulos.items():
            # Obter as coordenadas do retângulo
            (x1, y1), (x2, y2) = pontos
            # Recortar a região correspondente da imagem original
            regiao = imagem[y1:y2, x1:x2]
            # Salvar a região recortada como uma imagem separada na pasta "regiao_enem"
            cv2.imwrite(os.path.join(pasta_destino, f'regiao_{idx + 1}.jpg'), regiao)
            
        print(f"Regiões recortadas salvas na pasta '{pasta_destino}'.")
    else:
        print("Nenhum retângulo foi selecionado.")


executar_retangulos_enem()

