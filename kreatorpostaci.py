import pygame 

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load("images/background.png")
obraz_bazy_postaci = pygame.image.load("images/base.png")
pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_działa = True

while gra_działa:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
         if zdarzenie.key == pygame.K_ESCAPE:
            gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(obraz_tla, (0,0))
    pygame.display.flip()
    zegar.tick(30)
pygame.quit()