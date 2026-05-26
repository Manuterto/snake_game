import pygame 
import time
import random 


pygame.init()

largura=800
altura=600
tela= pygame.display.set_mode(((largura, altura)))
pygame.display.set_caption(' JOGO DA COBRINHA ')

#CORES
branco=(255, 255, 255)
azul=(0, 0, 255)
preto=(0, 0, 0)
vermelho=(225, 0 ,0)
cinza=(40,40,40)

#timer frames ps

clock= pygame.time.Clock()
speed=10

#tamanho dos blocos
tamanho_bloco=20

fonte=pygame.font.SysFont(None, 35)

#pontuação

def mostrar_pontuacao(pontos):
    valor = fonte.render("Pontos: " + str(pontos), True, preto)
    tela.blit(valor, [10,10 ])

def jogo():
    x=largura//2
    y=altura//2
    x_mudanca=0
    y_mudanca=0     

    cobra=[]
    comprimento_cobra= 1
    comidax=round(random.randrange(0, largura-tamanho_bloco)/20)*20
    comiday=round(random.randrange(0, altura-tamanho_bloco)/20)*20

    fim_de_jogo= False
    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                fim_de_jogo= True
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_LEFT:
                    x_mudanca=-tamanho_bloco    
                    y_mudanca=0
                elif evento.key==pygame.K_RIGHT:
                    x_mudanca=tamanho_bloco
                    y_mudanca=0
                elif evento.key==pygame.K_UP:
                    y_mudanca=-tamanho_bloco
                    x_mudanca=0
                elif evento.key==pygame.K_DOWN:
                    y_mudanca=tamanho_bloco
                    x_mudanca=0
        #nova posição da cobra
        x+=x_mudanca
        y+=y_mudanca
        tela.fill(branco)
    
    #cobra bateu
        if x>=largura or  x<0 or y>=altura or y<0:
            fim_de_jogo=True
            tela.fill(branco)

        pygame.draw.rect(tela, vermelho, [comidax, comiday, tamanho_bloco, tamanho_bloco])

        cabeca=[]
        cabeca.append(x)
        cabeca.append(y)
        cobra.append(cabeca)

        if len(cobra)>comprimento_cobra:
            del cobra[0]
    
        #cobra bateu nela mesma
        for bloco in cobra [:-1]:
            if bloco==cabeca:
                fim_de_jogo=True

        for bloco in cobra:    
            pygame.draw.rect(tela, azul, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        mostrar_pontuacao(comprimento_cobra-1)
    
        pygame.display.update()

        #cobra comeu a comida
        if x==comidax and y==comiday:
            comidax=round(random.randrange(0, largura-tamanho_bloco)/20)*20
            comiday=round(random.randrange(0, altura-tamanho_bloco)/20)*20
            comprimento_cobra+=1
        clock.tick(speed)

    #game over
    tela.fill(preto)
    mensagem= fonte.render('GAME OVER', True, branco)

    rect_msg = mensagem.get_rect(center=(800 // 2, 600 // 2))

    tela.blit(mensagem, rect_msg)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
jogo()