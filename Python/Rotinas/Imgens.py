import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

# Carregue a imagem original e a imagem do botão que você deseja encontrar
img_rgb = cv2.imread(".\\Rotinas\\screenshot\\screenshot4.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(".\\Rotinas\\screenshot\\botao.png", 0)

# Obtenha as dimensões do template
w, h = template.shape[::-1]

# Realize a correspondência de templates
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Defina um threshold para a correspondência
threshold = 0.8

# Encontre as posições onde a correspondência excede o threshold
loc = np.where(res >= threshold)

# Inicialize listas para armazenar as coordenadas X e Y
posicoes_x = []
posicoes_y = []

# Capture as coordenadas X e Y dos retângulos encontrados
for pt in zip(*loc[::-1]):
    posicoes_x.append(pt[0] + w // 2)
    posicoes_y.append(pt[1] + h // 2)

# Exiba as coordenadas X e Y
for i in range(len(posicoes_x)):
    print(f'Posição {i+1}: X={posicoes_x[i]}, Y={posicoes_y[i]}')

# Desenhe retângulos ao redor das correspondências encontradas
centros_x = []
centros_y = []
for pt in zip(*loc[::-1]):
    x = pt[0] + w // 2
    y = pt[1] + h // 2
    centros_x.append(x)
    centros_y.append(y)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    cv2.circle(img_rgb, (x, y), 5, (255, 0, 0), -1)



# Salve a imagem com os retângulos
cv2.imwrite('imagem_saida.png', img_rgb)

for i in range(len(centros_x)):
    print(f'Centro {i+1}: X={centros_x[i]}, Y={centros_y[i]}')



pyautogui.moveTo(centros_x[i],301)