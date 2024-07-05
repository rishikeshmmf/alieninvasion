import sys
import pygame
from pygame.examples.go_over_there import screen

import ship
from settings import Settings
 #from ship import ship

ai_settings = Settings()
def check_events():
 for event in pygame.event.get():  """Respond to keypresses and mouse events."""
 if event.type == pygame.QUIT:
   sys.exit()
def update_screen(self):
 """Update images on the screen, and flip to the new screen."""
 self.screen.fill(self.settings.bg_color)
 self.ship.blitme()
 pygame.display.flip()
