import pygame
from time import sleep
pygame.init()
window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('Bhoot.mp3')
pygame.mixer.music.play()
sleep(6)
image=pygame.image.load('img.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(2)
pygame.mixer.music.load('scared.mp3')
pygame.mixer.music.play()
sleep(4)


