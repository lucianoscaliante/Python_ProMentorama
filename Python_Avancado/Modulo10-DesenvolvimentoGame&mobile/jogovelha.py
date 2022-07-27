# importando bibliotecas math e curses
import math

# importando as biblioteca pandas e pygame
import pandas as pd
import pygame as gamep

# variaveis de cores do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
cinza = (150, 150, 150)


# Tamanho da tela do jogo
window = gamep.display.set_mode((1000, 600))
window.fill(branco)

# tipo de fonte para o jogo
gamep.font.init()

# escolhendo a fonte
fonte = gamep.font.SysFont("Comic Sans MS", 35)

borda_game = [['n', 'n', 'n'],
              ['n', 'n', 'n'],
              ['n', 'n', 'n']]


# clique na variavel
clique_status = 0

# Clique e desative a variável
clique_desative = 0

# clique na posição da variavel
clique_posi_x = -1
clique_posi_y = -1

# O ou X volta
x_ou_o_volta = 'x'

# fim do game
fim_game = 0


# Função para grade do jogo
def grade_jogo(window):
    gamep.draw.rect(window, branco, (0, 0, 600, 600))
    gamep.draw.line(window, preto, (205, 0), (205, 600), 10)
    gamep.draw.line(window, preto, (405, 0), (405, 600), 10)
    gamep.draw.line(window, preto, (0, 205), (600, 205), 10)
    gamep.draw.line(window, preto, (0, 405), (600, 405), 10)


# Função clique no jogo
def clique_jogo(clique_desative, clique_status, x, y):
    if clique_mause[0] == 0 and clique_status == 1:
        clique_desative = 1
        x = (math.ceil(mause[0] / 200) - 1)
        y = (math.ceil(mause[1] / 200) - 1)

    elif clique_mause[0] == 0 and clique_status == 0:
        x = -1
        y = -1

    return clique_desative, clique_status, x, y


# função para renderizar o X e O do jogo
def render_jogo(window, borda_game):
    for n in range(3):
        for nn in range(3):
            if borda_game[nn][n] == 'x':
                jogador_x(window, n, nn)

            elif borda_game[nn][n] == 'o':
                jogador_o(window, n, nn)

            else:
                pass


# função para posições do game
def borda_jogo_data(borda_game, x_ou_o_volta, fim_game, x, y):
    if x < 3 and y < 3:
        if x_ou_o_volta == 'x' and borda_game[y][x] == 'n' and x != -1 and y != -1 and fim_game == 0:
            borda_game[y][x] = 'x'
            x_ou_o_volta = 'o'

        if x_ou_o_volta == 'o' and borda_game[y][x] == 'n' and x != -1 and y != -1 and fim_game == 0:
            borda_game[y][x] = 'o'
            x_ou_o_volta = 'x'

    return borda_game, x_ou_o_volta


# função para saber quem ganho o jogo
def vencedor(window, borda_game, x_ou_o_volta, fim_game):
    if borda_game[0][0] == 'x' and borda_game[0][1] == 'x' and borda_game[0][2] == 'x' \
            or borda_game[0][0] == 'o' and borda_game[0][1] == 'o' and borda_game[0][2] == 'o':
        gamep.draw.line(window, verde, (30, 100), (570, 100), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[1][0] == 'x' and borda_game[1][1] == 'x' and borda_game[1][2] == 'x' \
            or borda_game[1][0] == 'o' and borda_game[1][1] == 'o' and borda_game[1][2] == 'o':
        gamep.draw.line(window, verde, (30, 300), (570, 300), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[2][0] == 'x' and borda_game[2][1] == 'x' and borda_game[2][2] == 'x' \
            or borda_game[2][0] == 'o' and borda_game[2][1] == 'o' and borda_game[2][2] == 'o':
        gamep.draw.line(window, verde, (30, 500), (570, 500), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[0][0] == 'x' and borda_game[1][0] == 'x' and borda_game[2][0] == 'x' \
            or borda_game[0][0] == 'o' and borda_game[1][0] == 'o' and borda_game[2][0] == 'o':
        gamep.draw.line(window, verde, (100, 30), (100, 580), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[0][1] == 'x' and borda_game[1][1] == 'x' and borda_game[2][1] == 'x' \
            or borda_game[0][1] == 'o' and borda_game[1][1] == 'o' and borda_game[2][1] == 'o':
        gamep.draw.line(window, verde, (300, 30), (380, 580), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[0][2] == 'x' and borda_game[1][2] == 'x' and borda_game[2][2] == 'x' \
            or borda_game[0][2] == 'o' and borda_game[1][2] == 'o' and borda_game[2][2] == 'o':
        gamep.draw.line(window, verde, (500, 30), (500, 580), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[0][0] == 'x' and borda_game[1][1] == 'x' and borda_game[2][2] == 'x' \
            or borda_game[0][0] == 'o' and borda_game[1][1] == '0' and borda_game[2][2] == 'o':
        gamep.draw.line(window, verde, (30, 30), (580, 580), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    elif borda_game[2][0] == 'x' and borda_game[1][1] == 'x' and borda_game[0][2] == 'x' \
            or borda_game[2][0] == 'o' and borda_game[1][1] == 'o' and borda_game[0][2] == 'o':
        gamep.draw.line(window, verde, (580, 30), (30, 580), 10)
        fim_game = 1
        x_ou_o_volta = 'x'

    return fim_game, x_ou_o_volta


# função para o botão reset do jogo
def botao_reset(window):
    gamep.draw.rect(window, cinza, (700, 100, 200, 65))
    texto = fonte.render('Restart', 1, preto)
    window.blit(texto, (750, 110))


# função para dar reset no jogo
def reset_game(borda_game, x, y, fim_game, clique_desative):
    if clique_desative == 1 and fim_game == 1:
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            borda_game = [['n', 'n', 'n'],
                          ['n', 'n', 'n'],
                          ['n', 'n', 'n']]
            fim_game = 0

    return borda_game, fim_game


# função game status
def game_status(borda_game, x_ou_o_volta, fim_game):
    cont = 0
    for n in range(3):
        for nn in range(3):
            if borda_game[nn][n] != 'n':
                cont += 1

    if cont == 9 and x_ou_o_volta == 'x':
        x_ou_o_volta = 'o'
        fim_game = 1

    elif cont == 9 and x_ou_o_volta == 'o':
        x_ou_o_volta = 'x'
        fim_game = 1

    return fim_game, x_ou_o_volta


# funções para desenha o x e o no jogo
def jogador_x(window, x, y):
    gamep.draw.line(window, vermelho, ((x * 200) + 30,
                    (y * 200) + 30), ((x * 200) + 180, (y * 200) + 180), 10)
    gamep.draw.line(window, vermelho, ((x * 200) + 180,
                    (y * 200) + 30), ((x * 200) + 30, (y * 200) + 180), 10)


def jogador_o(window, x, y):
    gamep.draw.circle(window, azul, ((x * 200) + 105, (y * 200) + 105), 75)
    gamep.draw.circle(window, branco, ((x * 200) + 105, (y * 200) + 105), 65)


# logica do game
while True:
    for event in gamep.event.get():
        if event.type == gamep.QUIT:
            gamep.quit()
            quit()

    # variavel para posição do mause
    mause = gamep.mouse.get_pos()
    mause_posi_x = mause[0]
    mause_posi_y = mause[1]

    # variavel do clique mause
    clique_mause = gamep.mouse.get_pressed()

    # Game - Jogo da velha
    grade_jogo(window)  # função da grade do jogo

    clique_desative, clique_status, clique_posi_x, clique_posi_y = clique_jogo(
        clique_desative, clique_status, clique_posi_x, clique_posi_y)

    # função para renderizar o X e O no jogo no array
    render_jogo(window, borda_game)

    # função para marca a vez de que joga
    borda_game, x_ou_o_volta = borda_jogo_data(
        borda_game, x_ou_o_volta, fim_game, clique_posi_x, clique_posi_y)

    # função para o vencedor do jogo
    fim_game, x_ou_o_volta = vencedor(
        window, borda_game, x_ou_o_volta, fim_game)

    # função para o botão
    botao_reset(window)

    # função do botão para resetar o game
    borda_game, fim_game = reset_game(
        borda_game, mause_posi_x, mause_posi_y, fim_game, clique_desative)

    # função para saber se o jogo deu enpate
    fim_game, x_ou_o_volta = game_status(borda_game, x_ou_o_volta, fim_game)

    # Clique dos Status do game
    if clique_mause[0] == 1:
        clique_status = 1
    else:
        clique_status = 0

    gamep.display.update()
