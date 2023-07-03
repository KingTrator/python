import pygame

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\Win10\OneDrive\Desktop\chaves-ta-bom-mas-nao-se-irrite.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue

#O código está funcional, mas foi totalmente feito pelo GPT-4.