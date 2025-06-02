import pygame, random
from recursos.basicos import limparTela, aguarde

pygame.init()

tamanho = (800, 600)

tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron man do marcao")
relogio = pygame.time.Clock()


branco = (255, 255, 255)
preto = (0, 0, 0)

iron = pygame.image.load("assets/iron.png")
fundoJogo = pygame.image.load("assets/fundoJogo.png")
missel = pygame.image.load("assets/missile.png")
misselSound = pygame.mixer.Sound('assets/missile.wav')
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)

posicaoXiron = 275
posicaoYiron = 400
movimenntoXiron = 0
movimentoYiron = 0
velocidadeIron = 10
posicaoXmissel = 250
posicaoYmissel = 0
velocidadeMissel = 5
pontos = 0
fonte = pygame.font.SysFont('comicsans', 18)
fonteMorte = pygame.font.SysFont('comicsans', 40)
while True:

    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_a or evento.key == pygame.K_LEFT):
            movimenntoXiron = -velocidadeIron
        elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_d or evento.key == pygame.K_RIGHT):
            movimenntoXiron = velocidadeIron
        elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_w or evento.key == pygame.K_UP): 
            movimentoYiron = -velocidadeIron
        elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_s or evento.key == pygame.K_DOWN):
            movimentoYiron = velocidadeIron

        elif evento.type == pygame.KEYUP and (evento.key == pygame.K_a or evento.key == pygame.K_LEFT):
            movimenntoXiron = 0
        elif evento.type == pygame.KEYUP and (evento.key == pygame.K_d or evento.key == pygame.K_RIGHT):
            movimenntoXiron = 0
        elif evento.type == pygame.KEYUP and (evento.key == pygame.K_w or evento.key == pygame.K_UP):
            movimentoYiron = 0
        elif evento.type == pygame.KEYUP and (evento.key == pygame.K_s or evento.key == pygame.K_DOWN):
            movimentoYiron = 0
        
    posicaoXiron += movimenntoXiron
    posicaoYiron += movimentoYiron

    if posicaoXiron < 0:
        posicaoXiron = 0
    elif posicaoXiron > tamanho[0] - iron.get_width():
        posicaoXiron = tamanho[0] - iron.get_width()

    if posicaoYiron < 0:
        posicaoYiron = 0
    elif posicaoYiron > tamanho[1] - iron.get_height():
        posicaoYiron = tamanho[1] - iron.get_height()

    posicaoYmissel += velocidadeMissel

    if posicaoYmissel > 600:
        posicaoYmissel = -250
        pygame.mixer.Sound.play(misselSound)
        posicaoXmissel = random.randint(0,800)
        velocidadeMissel += 1

        pontos += 1

    tela.fill(branco)
    tela.blit(fundoJogo, (0, 0))
    tela.blit(missel, (posicaoXmissel,posicaoYmissel))
    tela.blit(iron, (posicaoXiron, posicaoYiron))
    textoPontos = fonte.render(f"Pontos: {pontos}", True, preto)
    textoMorte = fonteMorte.render("Cuidado com os mísseis!", True, preto)
    tela.blit(textoPontos, (10, 10))

    iron_rect = pygame.Rect(posicaoXiron, posicaoYiron, iron.get_width(), iron.get_height())
    missel_rect = pygame.Rect(posicaoXmissel, posicaoYmissel, missel.get_width(), missel.get_height())
    if iron_rect.colliderect(missel_rect):

        tela.blit(textoMorte, (200, 300))
        pygame.display.update()
        aguarde(2)
        pygame.quit()
        exit()

    pygame.display.update()
    relogio.tick(60)