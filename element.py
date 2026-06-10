import pygame

class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka):
        super().__init__()
        self.obraz = pygame.image.load(sciezka)

class Element():
    def __init__(self, typ):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1, 4):
            sciezka = f'images/{typ}{i}.png'
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz) 


    def wybierzNastepny(self):
        return self.lista_obrazow[self.wybrany].obraz
    
class NakrycieGłowy(Element):
    def __init__(self):
        super().__init__('head')

class Oczy(Element):
    def __init__(self):
        super().__init__('eye')

class Bron(Element):
    def __init__(self):
        super().__init__('weapon')

class Cialo(Element):
    def __init__(self):
        super().__init__('body')