
import pygame
import os
import random
import sys

from itertools import combinations
from collections import deque

from helpers import practice_deck, Card

pygame.font.init()
pygame.mixer.init()

if getattr(sys, 'frozen', False):
    this_dir = os.path.dirname(sys.executable)
elif __file__:
    this_dir = os.path.dirname(__file__)

INITIAL_DECK = practice_deck

WIDTH, HEIGHT = 1500, 1000

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Set")

FPS = 30

BLACK = (0, 0, 0)
RED = (255,0, 0)
BLUE = (51, 153, 255)
DARK_BLUE = (63, 67, 161)
YELLOW = (255, 239, 4)
PURPLE = (120, 37, 155)


PLAY_AGAIN_RECT = pygame.Rect(317, 807, 242, 124)
MENU_RECT = pygame.Rect(924, 807, 244, 124)


TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)

VERSUS_TIMER = pygame.USEREVENT + 2

SET_SOUND = pygame.mixer.Sound(os.path.join(this_dir,  'Assets', 'Positive.wav'))
NOT_SET_SOUND = pygame.mixer.Sound(os.path.join(this_dir,  'Assets', 'Negative.wav'))
GAME_START = pygame.mixer.Sound(os.path.join('Sound_Assets', 'game_start.wav'))
BUTTON_PRESS = pygame.mixer.Sound(os.path.join(this_dir,  'Sound_Assets', 'menuselect4-36147.wav'))
BOT_SET = pygame.mixer.Sound(os.path.join(this_dir,  'Sound_Assets', 'correct-choice-43861.wav'))
# GAME_WIN = pygame.mixer.Sound(os.path.join(this_dir,  'Sound_Assets', 'game_win.wav'))

# SOUND1 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', 'Faster than that.wav'))
# SOUND2 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 2.wav'))
# SOUND3 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 3.wav'))
# SOUND4 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 4.wav'))
# SOUND5 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 5.wav'))
# SOUND6 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 6.wav'))
# SOUND7 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 7.wav'))
# SOUND8 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 8.wav'))
# SOUND9 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 9.wav'))
# SOUND10 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 10.wav'))
# SOUND11 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 11.wav'))
# SOUND12 = pygame.mixer.Sound(os.path.join(this_dir,  'Why', '136 N Fields Cir 12.wav'))
# SOUNDS = [SOUND1, SOUND2, SOUND3, SOUND4, SOUND5, SOUND6, SOUND7, SOUND8, SOUND9, SOUND10, SOUND11, SOUND12]

SET_FONT = pygame.font.SysFont('aerial', 60)
PLAYER_INFO_FONT = pygame.font.SysFont('aerial', 34)
SCORE_INFO_FONT = pygame.font.SysFont('aerial', 60)
ENDGAME_INFO_FONT = pygame.font.SysFont('aerial', 70)

REVEAL_BUTTON_RECT = pygame.Rect(922, 817, 200, 85)
SET_BUTTON_RECT = pygame.Rect(570, 783, 257, 128)
INFO_PANEL_RECT = pygame.Rect(825, 800, 325, 150)

PLACEMENT_RECTS = []
SELECTED_RECTS = []

COORDINATES_X = []
COORDINATES_Y = []
for i in range(3):
    for k in range(4):
        COORDINATES_X.append(250 + (k * 112) + (141 * k))
        COORDINATES_Y.append(50 + (i * 30) + (215 * i))

        PLACEMENT_RECTS.append(pygame.Rect(250 + (k * 112) + (141 * k), 50 + (i * 30) + (215 * i), 141, 215))
        SELECTED_RECTS.append(pygame.Rect((250 + (k * 112) + (141 * k)) - 10, (50 + (i * 30) + (215 * i)) - 10, 161, 235))

EXTRA_PLACEMENT_RECTS = [pygame.Rect(1262, 50, 141, 215), pygame.Rect(1262, 295, 141, 215), pygame.Rect(1262, 540, 141, 215)]
EXTRA_SELECTED_RECTS = [pygame.Rect(1252, 40, 161, 235), pygame.Rect(1252, 285, 161, 235), pygame.Rect(1252, 530, 161, 235)]

WHITE = (255, 255, 255)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Set_Background.png')), (WIDTH, HEIGHT))
VERSUS_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Versus Background.png')), (WIDTH, HEIGHT))
COMP_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Set_Game_Freeplay.png')), (WIDTH, HEIGHT))

GAME_OVER_SCREEN = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Freeplay-Timed Background.png')), (WIDTH, HEIGHT))
VERSUS_GAME_OVER_SCREEN = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Versus Game Over.png')), (WIDTH, HEIGHT))


DECK_BACK_RECT = pygame.Rect(36, 295, 141, 215)
DECK_BACK = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'card_back.jpg')), (141, 215))
SHADOW = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Shadow.png')), (206, 285))
MENU_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Assets', 'Menu button.png')), (193, 84))
MENU_BUTTON_RECT = pygame.Rect(14, 653, 193, 84)

MENU_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'Set_Menu.png')), (WIDTH, HEIGHT))
T120 = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', '120s_1.png')), (179, 76))
T60 = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', '60s.png')), (179, 76))
T90 = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', '90s_1.png')), (179, 76))
EASY = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'Easy.png')), (150, 73))
MEDIUM = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'medium.png')), (150, 73))
HARD = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'hard.png')), (150, 73))
EXPERT = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'expert.png')), (150, 73))
FREEPLAY = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'Freeplay.png')), (143, 71))

ELI = pygame.transform.scale(pygame.image.load(os.path.join(this_dir, 'Menu_Assets', 'Eli.png')), (180, 73))

MENU_SELECT_DIAMOND = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'diamond.png')), (207, 88))
MENU_SELECT_NOODLE = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'noodle.png')), (176, 95))
MENU_SELECT_OVAL = pygame.transform.scale(pygame.image.load(os.path.join(this_dir,  'Menu_Assets', 'oval.png')), (150, 79))

DIAMOND_MENU_RECT = pygame.Rect(401, 660, 179, 76)
NOODLE_MENU_RECT = pygame.Rect(629, 660, 150, 73)
OVAL_MENU_RECT = pygame.Rect(844, 660, 143, 71)

START_GAME_RECT = pygame.Rect(581, 780, 230, 117)


def bot_sound():
    # random.seed()
    # rand_bit = bool(random.getrandbits(1))
    # random_sound = random.randint(0,11)

    # if rand_bit:
    #     BOT_SET.play()
    
    # else:
    #     SOUNDS[random_sound].play()
    BOT_SET.play()


def calculate_final_card(card1, card2):
    final_card = Card(BACKGROUND, None, None, None, None)

    if card1.color == card2.color:
        final_card.color = card1.color
    else:
        final_card.color = 6 - (card1.color + card2.color)

    if card1.shape == card2.shape:
        final_card.shape = card1.shape
    else:
        final_card.shape = 6 - (card1.shape + card2.shape)

    if card1.number_of_shapes == card2.number_of_shapes:
        final_card.number_of_shapes = card1.number_of_shapes
    else:
        final_card.number_of_shapes = 6 - (card1.number_of_shapes + card2.number_of_shapes)

    if card1.shading == card2.shading:
        final_card.shading = card1.shading
    else:
        final_card.shading = 6 - (card1.shading + card2.shading)

    return final_card


def find_specific(reference, cards_on_table, extra_cards_on_table, card_keys):
    found = 0

    for key in card_keys:
        if key <= 12:
            if cards_on_table[key].shape == reference.shape:
                if cards_on_table[key].number_of_shapes == reference.number_of_shapes:
                    if cards_on_table[key].shading == reference.shading:
                        if cards_on_table[key].color == reference.color:
                            found =  key

        if key >= 13:
            if extra_cards_on_table[key].shape == reference.shape:
                if extra_cards_on_table[key].number_of_shapes == reference.number_of_shapes:
                    if extra_cards_on_table[key].shading == reference.shading:
                        if extra_cards_on_table[key].color == reference.color:
                            found = key
    
    return found   


def find_sets(cards_on_table, extra_cards_on_table):
    card_keys = []

    set_keys = []

    for i in range(1,16):
        if i <= 12:
            if cards_on_table[i] != None:
                card_keys.append(i)
        else:
            if extra_cards_on_table[i] != None:
                card_keys.append(i)
            else:
                break

    combos = combinations(card_keys, 2)

    for couple in combos:

        if couple[0] <=12:
            card1 = cards_on_table[couple[0]]
        else:
            card1 = extra_cards_on_table[couple[0]]
        
        if couple[1] <=12:
            card2 = cards_on_table[couple[1]]
        else:
            card2 = extra_cards_on_table[couple[1]]

        search_for = calculate_final_card(card1, card2)
        found = find_specific(search_for, cards_on_table, extra_cards_on_table, card_keys)
        if found != 0:
            set_keys.append([found, couple[0], couple[1]])

    return list(set(tuple(sorted(i)) for i in set_keys))


def set_analysis(selected, cards_on_table, extra_cards_on_table):
    checking = []

    for key in selected:
        if selected[key] == True and key <= 12:
            checking.append(cards_on_table[key])
        elif selected[key] == True and key >= 13:
            checking.append(extra_cards_on_table[key])
    
    # COLOR, SHAPE, NUMBER OF SHAPES, SHADING
    if checking[0].color == checking[1].color and checking[1].color == checking[2].color:
        pass
    elif checking[0].color != checking[1].color and checking[1].color != checking[2].color and checking[0].color != checking[2].color:
        pass
    else:
        return False

    if checking[0].shape == checking[1].shape and checking[1].shape == checking[2].shape:
        pass
    elif checking[0].shape != checking[1].shape and checking[1].shape != checking[2].shape and checking[0].shape != checking[2].shape:
        pass
    else:
        return False

    if checking[0].number_of_shapes == checking[1].number_of_shapes and checking[1].number_of_shapes == checking[2].number_of_shapes:
        pass
    elif checking[0].number_of_shapes != checking[1].number_of_shapes and checking[1].number_of_shapes != checking[2].number_of_shapes and checking[0].number_of_shapes != checking[2].number_of_shapes:
        pass
    else:
        return False

    if checking[0].shading == checking[1].shading and checking[1].shading == checking[2].shading:
        pass
    elif checking[0].shading != checking[1].shading and checking[1].shading != checking[2].shading and checking[0].shading != checking[2].shading:
        pass
    else:
        return False
    
    return True


def choose_bot_timer(sets_on_table, versus_mode):
    frequencies = deque([.025, .025, .05, .05, .05, .05, .1, .15, .15, .1, .05, .05, .05, .05, .025, .025])

    if versus_mode == 0:
        sets_multiplier = ((sets_on_table - 1)) * -1
        population = range(12 - (versus_mode * 2), 28 - (versus_mode * 2))
        frequencies.rotate(sets_multiplier)

    elif versus_mode == 1:
        sets_multiplier = ((sets_on_table - 1)) * -1
        population = range(9 - (versus_mode * 2), 25 - (versus_mode * 2))
        frequencies.rotate(sets_multiplier)
        
    elif versus_mode == 2 or versus_mode == 3:
        sets_multiplier = ((sets_on_table - 1) + versus_mode) * -1
        population = range(5 - (versus_mode), 21 - (versus_mode))
        frequencies.rotate(sets_multiplier)

    elif versus_mode == 4:
        sets_multiplier = ((sets_on_table - 1) + versus_mode - 1) * -1
        population = range(2, 13)
        
        frequencies = deque([.05, .05, .05, .075, .125, .15, .15, .125, .075, .05, .05, .05])
        frequencies.rotate(sets_multiplier)
        


    weights = []

    for i in range(len(population)):
        weights.append(frequencies[i])

    return random.choices(population, weights)[0]


def choose_card(times, deck):
    chosen_cards = []

    chosen_ints = random.sample(deck.keys(), times)
    for i in chosen_ints:
        chosen_cards.append(deck[i])
        deck.pop(i)
    return chosen_cards


def deal_cards(cards_on_table, counter, deck):

    chosen_cards = choose_card(counter, deck)

    for card in cards_on_table:
        if cards_on_table[card] == None:
            cards_on_table[card] = chosen_cards[counter - 1]
            counter -= 1


def deal_extra_card(extra_cards_on_table, deck):
    chosen_card = choose_card(1, deck)

    for card in extra_cards_on_table:
        if extra_cards_on_table[card] == None:
            extra_cards_on_table[card] = chosen_card[0]
            return


def draw_window(cards_on_table, extra_cards_on_table, selected, revealed_selected, player_score, cards_remaining, sets_on_table, time_sec, time_min, time_tens, gamemode, bot_pause, bot_score, versus_mode):
    if gamemode == "Timed":
        WIN.blit(COMP_BACKGROUND, (0, 0))
    elif gamemode == "Freeplay":
        WIN.blit(BACKGROUND, (0, 0))
        reveal_button_font2 = SET_FONT.render(f"{sets_on_table}", 1, WHITE)
        WIN.blit(reveal_button_font2, (1147, 841)    )
    else:
        WIN.blit(VERSUS_BACKGROUND, (0, 0))

    for key in cards_on_table:
        if revealed_selected[key] == True:
            WIN.fill(YELLOW, SELECTED_RECTS[key - 1])

        elif selected[key] == True:
            WIN.fill(RED, SELECTED_RECTS[key - 1])

        if cards_on_table[key] != None:
            WIN.blit(SHADOW, (SELECTED_RECTS[key - 1].x - 15, SELECTED_RECTS[key - 1].y - 15))
            WIN.blit(cards_on_table[key].image, (PLACEMENT_RECTS[key - 1].x, PLACEMENT_RECTS[key - 1].y))

    for extra in extra_cards_on_table:
        if revealed_selected[extra]:
            WIN.fill(YELLOW, EXTRA_SELECTED_RECTS[extra - 13])

        elif selected[extra] == True and extra_cards_on_table[extra] != None:
            WIN.fill(RED, EXTRA_SELECTED_RECTS[extra - 13])

        if extra_cards_on_table[extra] != None:
            WIN.blit(SHADOW, (EXTRA_SELECTED_RECTS[extra - 13].x - 15, EXTRA_SELECTED_RECTS[extra - 13].y - 15))
            WIN.blit(extra_cards_on_table[extra].image, (EXTRA_PLACEMENT_RECTS[extra - 13].x, EXTRA_PLACEMENT_RECTS[extra - 13].y))

    cards_left_info_font = SCORE_INFO_FONT.render(f"{cards_remaining}", 1, WHITE)
    timer_info_font = SCORE_INFO_FONT.render(f"{time_min}:{time_tens}{time_sec}", 1, WHITE)
    score_info_font = SCORE_INFO_FONT.render(f"{player_score}", 1, WHITE)

    WIN.blit(score_info_font, (97, 85))
    
    if gamemode != "Versus":
        WIN.blit(cards_left_info_font, (83, 215 ))
        WIN.blit(timer_info_font, (1271, 835))
    else:
        bot_score_info_font = SCORE_INFO_FONT.render(f"{bot_score}", 1, WHITE)

        WIN.blit(cards_left_info_font, (1075, 835 ))
        WIN.blit(timer_info_font, (1271, 835))
        WIN.blit(bot_score_info_font, (97, 215 ))

    WIN.blit(SHADOW, (DECK_BACK_RECT.x - 25, DECK_BACK_RECT.y - 25))
    WIN.blit(DECK_BACK, DECK_BACK_RECT)
    WIN.blit(MENU_BUTTON, MENU_BUTTON_RECT)

    pygame.display.update()


    if bot_pause and versus_mode == 0:
        pygame.time.delay(5000)
    elif bot_pause:
        pygame.time.delay(2000)



def draw_endgame_window(player_score, time_sec, time_tens, time_min, gamemode, bot_score):
    endgame_score_font = ENDGAME_INFO_FONT.render(f"{player_score}", 1, DARK_BLUE)
    endgame_timer_font = ENDGAME_INFO_FONT.render(f"{time_min}:{time_tens}{time_sec}", 1, DARK_BLUE)
    endgame_gamemode_font = ENDGAME_INFO_FONT.render(f"{gamemode}", 1, DARK_BLUE)

    if gamemode != "Versus":
        WIN.blit(GAME_OVER_SCREEN, (0, 0))

        WIN.blit(endgame_score_font, (750, 420))
        WIN.blit(endgame_timer_font, (750, 543))
        WIN.blit(endgame_gamemode_font, (750, 666))

    else:
        WIN.blit(VERSUS_GAME_OVER_SCREEN, (0, 0))

        endgame_bot_font = ENDGAME_INFO_FONT.render(f"{bot_score}", 1, RED)

        WIN.blit(endgame_bot_font, (750, 478))
        WIN.blit(endgame_score_font, (750, 394))
        WIN.blit(endgame_timer_font, (750, 560))
        WIN.blit(endgame_gamemode_font, (750, 649))

    pygame.display.update()


def draw_menu_window(menu_value, menu_selected):
    WIN.blit(MENU_BACKGROUND, (0, 0))

    if menu_selected[0]:
        WIN.blit(MENU_SELECT_DIAMOND, (387, 655))
    elif menu_selected[1]:
        WIN.blit(MENU_SELECT_NOODLE, (617, 651))
    elif menu_selected[2]:
        WIN.blit(MENU_SELECT_OVAL, (837, 658))

    if menu_value["diamond"] == 0:
        WIN.blit(T120, DIAMOND_MENU_RECT)
    elif menu_value["diamond"] == 1:
        WIN.blit(T90, DIAMOND_MENU_RECT)
    elif menu_value["diamond"] == 2:
        WIN.blit(T60, DIAMOND_MENU_RECT)

    if menu_value["noodle"] == 0:
        WIN.blit(EASY, NOODLE_MENU_RECT)
    elif menu_value["noodle"] == 1:
        WIN.blit(MEDIUM, NOODLE_MENU_RECT)
    elif menu_value["noodle"] == 2:
        WIN.blit(HARD, NOODLE_MENU_RECT)
    elif menu_value["noodle"] == 3:
        WIN.blit(EXPERT, NOODLE_MENU_RECT)
    elif menu_value["noodle"] == 4:
        WIN.blit(ELI, NOODLE_MENU_RECT)

    WIN.blit(FREEPLAY, OVAL_MENU_RECT)

    pygame.display.update()


def game():
    game_over = False
    menu = True
    in_game = False

    gamemode = None
    timed_mode = 0
    versus_mode = 0

    deck = INITIAL_DECK.copy()

    player_score = 0
    cards_remaining = 81
    sets_on_table = 0
    time_sec = 0
    time_min = 0
    time_tens = 0

    reveal = False
    revealed_showing = 0

    selected = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False}
    revealed_selected = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False}

    menu_value = {"diamond": 0, "noodle": 0, "oval": 0}
    menu_selected = [False, False, False]

    cards_on_table = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12: None}
    extra_cards_on_table = {13: None, 14: None, 15: None}

    clock = pygame.time.Clock()

    versus_timer = 0
    reset_bot_timer = False
    bot_pause = False
    bot_score = 0

# NEED OVERALL LOOP! THIS CAN HAVE PYGAME.QUIT
    while True:
        clock.tick(FPS)

        deck = INITIAL_DECK.copy()
        selected.update( (k, False) for k in selected)
        cards_on_table.update( (k, None) for k in cards_on_table)
        extra_cards_on_table.update( (k, None) for k in extra_cards_on_table)

        while menu: # MENU LOOP

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if DIAMOND_MENU_RECT.collidepoint(mouse_pos):
                        BUTTON_PRESS.play()
                        menu_value["diamond"] = (menu_value["diamond"] + 1) % 3
                        gamemode = "Timed"
                        timed_mode = 120 - menu_value["diamond"] * 30

                        menu_selected[0] = True
                        menu_selected[1], menu_selected[2] = False, False

                    elif NOODLE_MENU_RECT.collidepoint(mouse_pos):
                        BUTTON_PRESS.play()
                        menu_value["noodle"] = (menu_value["noodle"] + 1) % 5
                        gamemode = "Versus"
                        versus_mode = menu_value["noodle"]

                        menu_selected[1] = True
                        menu_selected[0], menu_selected[2] = False, False

                    elif OVAL_MENU_RECT.collidepoint(mouse_pos):
                        BUTTON_PRESS.play()
                        gamemode = "Freeplay"

                        menu_selected[2] = True
                        menu_selected[0], menu_selected[1] = False, False

                    elif START_GAME_RECT.collidepoint(mouse_pos) and gamemode != None:
                        GAME_START.play()
                        menu = False
                        in_game = True

                        player_score = 0
                        bot_score = 0
                        cards_remaining = 81
                        sets_on_table = 0
                        time_sec = 0
                        time_min = 0
                        time_tens = 0
                        reset_bot_timer = True


            
            draw_menu_window(menu_value, menu_selected)


        while game_over: # ENDGAME LOOP
            clock.tick(FPS)

            deck = INITIAL_DECK.copy()
            selected.update( (k, False) for k in selected)
            cards_on_table.update( (k, None) for k in cards_on_table)
            extra_cards_on_table.update( (k, None) for k in extra_cards_on_table)

            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit() 

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()

                            if PLAY_AGAIN_RECT.collidepoint(mouse_pos):
                                GAME_START.play()
                                game_over = False
                                in_game = True

                                player_score = 0
                                bot_score = 0
                                cards_remaining = 81
                                sets_on_table = 0
                                time_sec = 0
                                time_min = 0
                                time_tens = 0
                                reset_bot_timer = True

                            if MENU_RECT.collidepoint(mouse_pos):
                                BUTTON_PRESS.play()
                                game_over = False
                                menu = True

                                gamemode = None
                                timed_mode = 0                
            if gamemode != None:
                draw_endgame_window(player_score, time_sec, time_tens, time_min, gamemode, bot_score)


        while in_game: # GAME LOOP
            clock.tick(FPS)

            extra_card = False
            
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit() 

                        if event.type == TIMER:
                            time_sec += 1
                            versus_timer -= 1
                            if time_sec == 10:
                                time_sec = 0
                                time_tens += 1
                            if time_tens == 6:
                                time_tens = 0
                                time_min += 1

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()

                            if MENU_BUTTON_RECT.collidepoint(mouse_pos): # IF THEY CLICK MENU
                                BUTTON_PRESS.play()
                                selected.update( (k, False) for k in selected)
                                reveal = False

                                cards_on_table.update( (k, None) for k in cards_on_table)
                                extra_cards_on_table.update( (k, None) for k in extra_cards_on_table)

                                menu = True
                                in_game = False

                            elif REVEAL_BUTTON_RECT.collidepoint(mouse_pos) and gamemode == "Freeplay": # IF THEY CLICK REVEAL SETS
                                reveal = True
                                revealed_showing += 1

                            elif DECK_BACK_RECT.collidepoint(mouse_pos): # IF THEY CLICK ADD CARD
                                extra_card = True

                            elif SET_BUTTON_RECT.collidepoint(mouse_pos): # IF THEY CLICK SET BUTTON

                                if sum(list(selected.values())) != 3:
                                    selected.update( (k, False) for k in selected)

                                else:
                                    if set_analysis(selected, cards_on_table, extra_cards_on_table):
                                        # PLAY SOUND, UPDATE PLAYER SCORE
                                        player_score += 3
                                        SET_SOUND.play()
                                        reset_bot_timer = True

                                        # SET CARDS_ON_TABLE TO EMPTY
                                        for key in selected:
                                            if selected[key] == True and key <= 12:
                                                cards_on_table[key] = None           
                                        
                                        # RESHUFLE EXTRAS, SET EXTRA CARDS TO EMPTY
                                        for s in range(13, 16):
                                            if extra_cards_on_table[s] != None and selected[s] == False:
                                                for t in cards_on_table:
                                                    if cards_on_table[t] == None:
                                                        cards_on_table[t] = extra_cards_on_table[s]
                                                        extra_cards_on_table[s] = None
                                            else:
                                                extra_cards_on_table[s] = None

                                    else:
                                        # PLAY SOUND, RESET SELECTED
                                        NOT_SET_SOUND.play()
                                    
                                selected.update( (k, False) for k in selected)   
                            
                            else: # IF THEY CLICK A CARD

                                z = 0
                                for rectangle in PLACEMENT_RECTS + EXTRA_PLACEMENT_RECTS: # CHECKS ALL PLACEMENT RECTANGLES
                                    z += 1
                                    if rectangle.collidepoint(mouse_pos):

                                        reveal = False # UNSELECTS ALL REVEALED

                                        if sum(list(selected.values())) == 3:
                                            if selected[z] == True:
                                                selected[z] = False

                                        else:

                                            selected[z] = not selected[z] 

            if bot_pause: # REMOVES CARDS, FRAME AFTER SELECTION
                for bot_selection in revealed_selected:
                    if bot_selection <= 12 and revealed_selected[bot_selection]:
                        cards_on_table[bot_selection] = None
                    if bot_selection > 12 and revealed_selected[bot_selection]:
                        extra_cards_on_table[bot_selection] = None

                for s in range(13, 16):
                    if extra_cards_on_table[s] != None and selected[s] == False:
                        for t in cards_on_table:
                            if cards_on_table[t] == None:
                                cards_on_table[t] = extra_cards_on_table[s]
                                extra_cards_on_table[s] = None
                    else:
                        extra_cards_on_table[s] = None

                bot_pause = False
                reset_bot_timer = True
                revealed_selected.update( (k, False) for k in revealed_selected)


            counter = 0 # COUNTS NUMBER OF EMPTY CARD SLOTS 
            for card in cards_on_table:
                if cards_on_table[card] == None:
                    counter += 1

            if cards_remaining != 0:

                if counter > 0:
                    deal_cards(cards_on_table, counter, deck)
                    cards_remaining -= counter

                if extra_card == True and (None in extra_cards_on_table.values()):
                    deal_extra_card(extra_cards_on_table, deck)
                    cards_remaining -= 1

            # FINDING AND REVEALING SETS
            set_tuples = find_sets(cards_on_table, extra_cards_on_table)
            sets_on_table = len(set_tuples)

            if sets_on_table == 0 and cards_remaining != 0:
                deal_extra_card(extra_cards_on_table, deck)
                cards_remaining -= 1

            # GAMEMODE TIMER
            if gamemode == "Timed":
                if timed_mode == time_sec + (time_tens * 10) + (time_min * 60):
                    # draw_endgame_window(player_score, time_sec, time_tens, time_min)
                    game_over = True
                    in_game = False
                    break

            # ENDGAME
            # IF NO SETS LEFT CARDS == 0, ENDGAME. DISPLAY SCORE
            if sets_on_table == 0 and cards_remaining == 0:
                # draw_endgame_window(player_score, time_sec, time_tens, time_min)
                game_over = True
                in_game = False
                break

            # NORMAL ENDGAME AND GAME, VARIBLE FOR WINDOW 
            # FUNCTION TO RANDOMLY FIND SETS, INTERVAL, SETS ON TABLE
            if gamemode == "Versus":
                if reset_bot_timer:
                    versus_timer = choose_bot_timer(sets_on_table, versus_mode)
                    reset_bot_timer = False

                if versus_timer <= 0: # CHOOSE SET
                    if sets_on_table > 0:
                        if versus_mode != 4:
                            BOT_SET.play()
                        else:
                            bot_sound()

                        bot_score += 3
                        revealed_selected.update( (k, False) for k in revealed_selected)
                        selected.update( (k, False) for k in selected)

                        for i in set_tuples[revealed_showing]:
                            revealed_selected[i] = True
                        bot_pause = True

            # DEALS WITH TOGGLING BETWEEN SELECTED AND REVEALED SELECTED
            else:

                if revealed_showing == sets_on_table:
                    revealed_showing = 0
                    selected.update( (k, False) for k in selected)

                if reveal and sets_on_table > 0:
                    selected.update( (k, False) for k in selected)

                    revealed_selected.update( (k, False) for k in revealed_selected)
                    
                    for i in set_tuples[revealed_showing]:
                        revealed_selected[i] = True
                
                else:
                    revealed_selected.update( (k, False) for k in revealed_selected)
                    revealed_showing = 0
                            

            draw_window(cards_on_table, extra_cards_on_table, selected, revealed_selected, player_score, cards_remaining, sets_on_table, time_sec, time_min, time_tens, gamemode, bot_pause, bot_score, versus_mode)

if __name__ == "__main__":
    game()
