import pygame
import os
from pathlib import Path

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600

# Farben
WHITE = (255, 255, 255)

# Erstelle ein Pygame-Fenster
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PNG Animation")

# Lade die Bilder für die Animation
animation_path = str(Path.cwd() / "Assets" / "images" / "archer" / "Shot_1.png")
animation_sheet = pygame.image.load(animation_path)

# Teile das Bild in acht separate Bilder auf
frame_width = animation_sheet.get_width() // 14
frame_height = animation_sheet.get_height()
animation_frames = [animation_sheet.subsurface((i * frame_width, 0, frame_width, frame_height)) for i in range(14)]
current_frame = 0

# Festlegen der Bildrate (Frames pro Sekunde)
FPS = 12  # Du kannst die Bildrate anpassen

clock = pygame.time.Clock()

# Hauptspielschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hintergrund leeren
    screen.fill(WHITE)

    # Zeige das aktuelle Bild der Animation an
    screen.blit(animation_frames[current_frame], (100, 100))

    # Aktualisiere den Frame-Zähler
    current_frame = (current_frame + 1) % len(animation_frames)

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Begrenze die Bildrate
    clock.tick(FPS)

# Pygame beenden
pygame.quit()