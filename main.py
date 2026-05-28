"""
Punto de entrada principal.
Ejecutar desde la raíz del proyecto:  python main.py
"""
import random
import pygame

from settings  import BLANCO, ALTURA, ANCHURA, FPS, RUTA_SFX_COMIDA, RUTA_SFX_PERDIDO
from src.serpiente import SERPIENTE
from src.comida import COMIDA
from src.hud import VER_MARCADOR


def main() -> None:
    pygame.mixer.init()
    pygame.init()

    screen = pygame.display.set_mode((ALTURA, ANCHURA))
    pygame.display.set_caption('El juego de la serpiente')

    # ── Grupos de sprites ────────────────────────────────
    lista_serpiente = pygame.sprite.Group()
    lista_comida    = pygame.sprite.Group()
    lista_global    = pygame.sprite.Group()

    # ── Sonidos globales ─────────────────────────────────
    sfx_comida  = pygame.mixer.Sound("assets/sound/COMIDA.wav");  sfx_comida.set_volume(1.0)
    sfx_perdido = pygame.mixer.Sound("assets/sound/PERDER.wav"); sfx_perdido.set_volume(1.0)

    # ── Crear serpiente ──────────────────────────────────
    serpiente = SERPIENTE(lista_serpiente, lista_comida, lista_global)
    lista_global.add(serpiente)

    reloj  = pygame.time.Clock()
    termina = False
    print("Empezamos...")

    # ── Bucle principal ──────────────────────────────────
    while not termina:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                termina = True
            elif event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_LEFT  and serpiente.DIRECCION != 'D': serpiente.DIRECCION = 'I'
                elif event.key == pygame.K_RIGHT and serpiente.DIRECCION != 'I': serpiente.DIRECCION = 'D'
                elif event.key == pygame.K_UP    and serpiente.DIRECCION != 'B': serpiente.DIRECCION = 'A'
                elif event.key == pygame.K_DOWN  and serpiente.DIRECCION != 'A': serpiente.DIRECCION = 'B'

        # Aparición aleatoria de comida
        if random.randint(0, 18) == 0:
            nueva_comida = COMIDA()
            if not pygame.sprite.spritecollide(nueva_comida, lista_global, False):
                sfx_comida.play()
                lista_global.add(nueva_comida)
                lista_comida.add(nueva_comida)

        # Renderizado
        lista_global.update()
        screen.fill(BLANCO)
        lista_global.draw(screen)
        VER_MARCADOR(screen, serpiente.PUNTOS)

        # Game over
        if serpiente.TERMINA:
            sfx_perdido.play()
            pygame.time.wait(5_000)
            termina = True

        pygame.display.flip()
        reloj.tick(FPS)

    print(f"Su marcador: {serpiente.PUNTOS} puntos")
    pygame.quit()


if __name__ == "__main__":
    main()