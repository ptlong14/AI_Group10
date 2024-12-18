import pygame
pygame.init()

def display_message(win, message, font, duration=2000):
    background_color = (0, 128, 0) 
    text_color = (255, 215, 0)       
    border_color = (255, 255, 255)
    text_surface = font.render(message, True, text_color)
    text_rect = text_surface.get_rect(
        center=(win.get_width() // 2-100, win.get_height() // 2))

    border_rect = text_surface.get_rect()
    border_rect.inflate_ip(20, 20) 
    border_rect.center = text_rect.center

    pygame.draw.rect(win, background_color, border_rect)  
    pygame.draw.rect(win, border_color, border_rect, 2)   

    win.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(duration)
