import pygame, data, datetime


def speed(SCREEN, speed, freeze):
    font = pygame.font.SysFont(None, 15)
    if not freeze:
        text_speed = font.render(f"speed: {speed}", True, (255, 255, 255))
    else:
        text_speed = font.render(f"paused", True, (255, 255, 255))

    SCREEN.blit(text_speed, (0, 10))

def help(SCREEN, status):
    width = 100
    height = 150
    if status:
        X_move = 0
    else:
        X_move = -width+1
    Y_move = 300

    outer_1 = pygame.Rect((X_move, Y_move, width, height))
    outer_2 = pygame.Rect((X_move+width-1, Y_move, 15, 20))
    inner_1 = pygame.Rect((X_move, Y_move+2, width-2, height-4))
    inner_2 = pygame.Rect((X_move+width-2, Y_move+2, 13, 16))
    outer = [outer_1, outer_2]
    inner = [inner_1, inner_2]

    for rect in outer:
        pygame.draw.rect(SCREEN, (data.color_help_outer), rect)
    for rect in inner:
        pygame.draw.rect(SCREEN, (data.color_help_inner), rect)

    font = pygame.font.SysFont(None, 20)
    H = font.render("H", True, (255, 255, 255))
    SCREEN.blit(H, (X_move+width, Y_move+4))

def date(SCREEN, t):
    start_date = datetime.date(2026, 1, 3)
    current_date = start_date + datetime.timedelta(days=t)
    
    font = pygame.font.SysFont(None, 15)
    display_date = font.render(f"{current_date}", True, (255, 255, 255))
    SCREEN.blit(display_date, (0, 0))

def crosshair(SCREEN):
    rect_1 = pygame.Rect((data.X_adjust-2, data.Y_adjust-2, 1, 4))
    rect_2 = pygame.Rect((data.X_adjust+1, data.Y_adjust-2, 1, 4))
    rect_3 = pygame.Rect((data.X_adjust-1, data.Y_adjust-2, 2, 1))
    rect_4 = pygame.Rect((data.X_adjust-1, data.Y_adjust+1, 2, 1))
    rects = [rect_1, rect_2, rect_3, rect_4]
    for rect in rects:
        pygame.draw.rect(SCREEN, (255, 0,0), rect)
    


        