import pygame
pygame.init()
pygame.mixer.music.load()
#colocar o mp3 nos parentes do load
pygame.mixer.music.play()
pygame.event.wait()