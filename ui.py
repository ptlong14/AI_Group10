import pygame
from settings import BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR, FONT


def draw_button(win, x, y, width, height, text, action=None, button_color=(100, 100, 100), hover_color=(150, 150, 150), text_color=(255, 255, 255)):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, width, height)
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(win, hover_color, button_rect) 
        if click[0] == 1 and action:
            action() 
    else:
        pygame.draw.rect(win, button_color, button_rect)
    # Vẽ viền nút
    pygame.draw.rect(win, (255, 255, 255), button_rect, 2)
    # Vẽ văn bản lên nút
    text_surface = FONT.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    win.blit(text_surface, text_rect)

def get_mouse_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def draw_multiline_text(surface, text, font, color, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    for line in lines:
        line_surface = font.render(line.strip(), True, color)
        surface.blit(line_surface, (x, y))
        y += line_surface.get_height()

def draw_instruction_box(win, instructions):
    win.fill((220, 220, 220))
    instruction_box_x = 50
    instruction_box_y = 30
    instruction_box_width = 700
    instruction_box_height = 600
    pygame.draw.rect(win, (50, 50, 50), (instruction_box_x - 5, instruction_box_y - 5, instruction_box_width + 10, instruction_box_height + 10), 0) 
    pygame.draw.rect(win, (255, 255, 255), (instruction_box_x, instruction_box_y, instruction_box_width, instruction_box_height))
    y_offset = instruction_box_y + 20
    for line in instructions:
        draw_multiline_text(win, line, FONT, (0, 0, 0),
                            instruction_box_x + 10, y_offset, instruction_box_width - 20)
        y_offset += FONT.get_height() * 2.1
    pygame.display.update()


def draw_result_box(win, result_message, MAZE_WIDTH):
    result_box_x = MAZE_WIDTH + 15
    result_box_y = 260
    result_box_width = 300
    result_box_height = 400
    pygame.draw.rect(win, (0, 255, 255), (result_box_x,
                     result_box_y, result_box_width, result_box_height))
    pygame.draw.rect(win, (255, 255, 255), (result_box_x + 5, result_box_y + 5,
                     result_box_width - 10, result_box_height - 10))

    result_lines = result_message.split('\n')
    for i, line in enumerate(result_lines):
        result_text = FONT.render(line, True, (0, 0, 0))
        win.blit(result_text, (result_box_x + 10, result_box_y +
                 10 + i * (FONT.get_height() + 5)))
