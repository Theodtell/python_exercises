#faça um programa que abra e reproduza o áudio de um arquivo mp3

import pygame

pygame.init() #iniciando o pygame
pygame.mixer.music.load('Paramore - Ignorance.mp3') #iniciando o arquivo
pygame.mixer.music.play() #tocnado o arquivo

input("Press enter to stop the music")
pygame.mixer.quit() #finalizando a música