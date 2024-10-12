import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego Simple y Adictivo")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Jugador
player_size = 20
player_pos = [width//2, height//2]
player_speed = 5

# Enemigos
enemy_size = 30
enemy_pos = [random.randint(0, width-enemy_size), random.randint(0, height-enemy_size)]
enemy_list = [enemy_pos]

# Disparos
bullet_size = 10
bullet_speed = 10
bullets = []

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Reloj
clock = pygame.time.Clock()

def draw_player(pos):
    pygame.draw.rect(screen, WHITE, (pos[0], pos[1], player_size, player_size))

def draw_enemies(enemies):
    for enemy_pos in enemies:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def create_bullet(pos):
    return [pos[0] + player_size//2 - bullet_size//2, pos[1] + player_size//2 - bullet_size//2]

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(create_bullet(player_pos))
    
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
        player_pos[1] += player_speed
    
    # Movimiento de los enemigos y detección de colisiones
    for idx, enemy_pos in enumerate(enemy_list):
        if detect_collision(player_pos, enemy_pos):
            running = False
        
        # Mover enemigo
        if enemy_pos[0] < player_pos[0]:
            enemy_pos[0] += 1
        else:
            enemy_pos[0] -= 1
        if enemy_pos[1] < player_pos[1]:
            enemy_pos[1] += 1
        else:
            enemy_pos[1] -= 1
    
    # Movimiento y colisión de balas
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        else:
            for enemy_pos in enemy_list[:]:
                if (enemy_pos[0] < bullet[0] < enemy_pos[0] + enemy_size and
                    enemy_pos[1] < bullet[1] < enemy_pos[1] + enemy_size):
                    enemy_list.remove(enemy_pos)
                    bullets.remove(bullet)
                    score += 10
                    break
    
    # Generar nuevos enemigos
    if random.randint(1, 30) == 1:
        enemy_list.append([random.randint(0, width-enemy_size), random.randint(0, height-enemy_size)])
    
    # Dibujar todo
    screen.fill(BLACK)
    draw_player(player_pos)
    draw_enemies(enemy_list)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_size, bullet_size))
    
    # Mostrar puntuación
    score += 1
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()