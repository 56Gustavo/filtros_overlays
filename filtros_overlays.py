import cv2
import numpy as np


imagem = cv2.imread('imagem.jpg')


# A. Filtro Blur (desfoque)
imagem_blur = cv2.GaussianBlur(imagem, (9, 9), 0)
cv2.imwrite('filtro_blur.png', imagem_blur)

# B. Detecção de Bordas
imagem_bordas = cv2.Canny(imagem, 100, 200)
cv2.imwrite('filtro_bordas.png', imagem_bordas)

# C. Imagem em Escalas de Cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imwrite('filtro_cinza.png', imagem_cinza)

# D. Redimensionamento da Imagem
altura, largura = imagem.shape[:2]
nova_largura = largura // 2
nova_altura = altura // 2
imagem_redimensionada = cv2.resize(imagem, (nova_largura, nova_altura))
cv2.imwrite('filtro_redimensionado.png', imagem_redimensionada)

# 2. Aplicar Overlays (Camadas)

# A. Desenhar um retângulo azul com espessura 2px
imagem_com_retangulo = imagem.copy()
altura, largura = imagem.shape[:2]
cv2.rectangle(imagem_com_retangulo, (10, 10), (largura - 10, altura - 10), (255, 0, 0), 2)
cv2.imwrite('imagem_com_retangulo.png', imagem_com_retangulo)

# B. Círculo vermelho com raio de 200px no centro da imagem
centro = (largura // 2, altura // 2)
raio = 200
imagem_com_circulo = imagem.copy()
cv2.circle(imagem_com_circulo, centro, raio, (0, 0, 255), 1)  # Cor vermelha
cv2.imwrite('imagem_com_circulo.png', imagem_com_circulo)

# C. Círculo verde com raio de 50px no centro
raio_interno = 50
imagem_com_circulo_interno = imagem.copy()
cv2.circle(imagem_com_circulo_interno, centro, raio_interno, (0, 255, 0), -1)  # Cor verde (preenchido)
cv2.imwrite('imagem_com_circulo_interno.png', imagem_com_circulo_interno)

# D. Escrever texto no canto inferior direito
imagem_com_texto = imagem.copy()
font = cv2.FONT_HERSHEY_SIMPLEX
texto = "Engenharia de Software"
posicao_texto = (largura - 250, altura - 10)  # Ajuste conforme necessário
cv2.putText(imagem_com_texto, texto, posicao_texto, font, 1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.imwrite('imagem_com_texto.png', imagem_com_texto)

# Exibir a imagem com texto (opcional)
cv2.imshow('Imagem com Texto', imagem_com_texto)
cv2.waitKey(0)
cv2.destroyAllWindows()
