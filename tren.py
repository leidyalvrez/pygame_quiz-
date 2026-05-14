# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame 
import sys
import math

PI = math.pi

negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
verde = (0,255,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0,255,255)
gris = (50,50,50)
gris_estandar = (128,128,128)
gris_claro = (200,200,200)

ventana = pygame.display.set_mode((1000,400))



pygame.init()

while True:

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)




    
    pygame.draw.ellipse(ventana, gris, (400,200,300,150), 0)
    punto_5 = [(450,190), (450,360), (500,360), (500,190)]
    pygame.draw.polygon(ventana, gris_estandar, punto_5, 0)
    punto_6 = [(520,195), (520,355), (820,355), (820,195)]
    pygame.draw.polygon(ventana, gris_claro, punto_6, 0)
    pygame.draw.circle(ventana, gris_estandar, (570,350), 50, 0)
    pygame.draw.circle(ventana, gris_estandar, (670,350), 50, 0)
    pygame.draw.circle(ventana, gris_estandar, (770,350), 50, 0)
    punto_6 = [(690,370), (690,340), (740,340), (740,370)]
    pygame.draw.polygon(ventana, negro, punto_6, 0)
    punto_7 = [(590,370), (590,340), (640,340), (640,370)]
    pygame.draw.polygon(ventana, negro, punto_7, 0)
    punto_8 = [(530,150), (530,195), (555,195), (555,150)]
    pygame.draw.polygon(ventana, gris_estandar, punto_8, 0)
    punto_9 = [(530,150), (530,195), (565,195), (565,150)]
    pygame.draw.polygon(ventana, gris_estandar, punto_9, 0)
    puntos_10 = [(510,120), (510,150), (580,150), (580,120)]
    pygame.draw.polygon(ventana, gris_estandar, puntos_10, 0)
    puntos_11 = [(600,100), (600,195), (820,195), (820,100)]
    pygame.draw.polygon(ventana, gris_estandar, puntos_11, 0)
    puntos_12 = [(630,115), (630,175), (790,175), (790,115)]
    pygame.draw.polygon(ventana, gris_claro, puntos_12, 0)
    pygame.draw.circle(ventana, amarillo, (710,150), 40, 0)
    pygame.draw.circle(ventana, rojo, (710,170), 10, 0)
    pygame.draw.circle(ventana, blanco, (690,145), 10, 0)
    pygame.draw.circle(ventana, blanco, (730,145), 10, 0)
    pygame.draw.circle(ventana, negro, (690,145), 5, 0)
    pygame.draw.circle(ventana, negro, (730,145), 5, 0)





    # Autoria
    fuente_arial = pygame.font.SysFont("Arial", 30, (200,220))
    texto = fuente_arial.render("Leidy Alvarez",1,blanco)
    ventana.blit(texto, (600,200))

    # actualizar visualización de la ventana
    pygame.display.flip()