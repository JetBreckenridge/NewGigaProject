import pygame
import settings

pygame.init()


class Rect:
    def __init__(self):
        self.rectHeight = settings.HEIGHT/2
        self.rectWidth = settings.WIDTH
        self.color = settings.BLUE
        self.y_pos = 0
        self.x_pos = 0

        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.rectWidth, self.rectHeight)

    def draw(self, window):
        pygame.draw.rect(window, self.color)



class Rect2:
    def __init__(self):
        self.rectHeight = settings.HEIGHT/2
        self.rectWidth = settings.WIDTH/2
        self.color = settings.RED
        self.y_pos = settings.HEIGHT/2
        self.x_pos = 0

        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.rectWidth, self.rectHeight)

    def draw(self, window):
        pygame.draw.rect(window, self.color)


def draw_text(window, text, size, color, x, y, centered):
    font = pygame.font.Font(settings.FONT, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    if centered:
        text_rect.midtop = (x, y)
    window.blit(text_surface, text_rect)

class Button(object):
   """A fairly straight forward button class."""
   def __init__(self, rect, color, function, **kwargs):
       self.rect = pygame.Rect(rect)
       self.color = color
       self.function = function
       self.clicked = False
       self.hovered = False
       self.hover_text = None
       self.clicked_text = None
       self.process_kwargs(kwargs)
       self.render_text()

   def process_kwargs(self, kwargs):
       """Various optional customization you can change by passing kwargs."""
       options = {"text": None,
                  "font": pygame.font.Font(None, 80),
                  "call_on_release": True,
                   "hover_color": None,
                   "clicked_color": None,
                   "font_color": settings.WHITE,
                   "hover_font_color": None,
                   "clicked_font_color": None}
       for kwarg in kwargs:
           if kwarg in options:
               options[kwarg] = kwargs[kwarg]
           else:
               raise AttributeError("Button has no keyword: {}".format(kwarg))
       self.__dict__.update(options)

   def render_text(self):
       """Pre render the button text."""
       if self.text:
           if self.hover_font_color:
               color = self.hover_font_color
               self.hover_text = self.font.render(self.text, True, color)
           if self.clicked_font_color:
               color = self.clicked_font_color
               self.clicked_text = self.font.render(self.text, True, color)
           self.text = self.font.render(self.text, True, self.font_color)

   def check_event(self, event):
       """The button needs to be passed events from your program event loop."""
       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           self.on_click(event)
       elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
           self.on_release(event)

   def on_click(self, event):
       if self.rect.collidepoint(event.pos):
           self.clicked = True
           if not self.call_on_release:
               self.function()

   def on_release(self, event):
       if self.clicked and self.call_on_release:
           self.function()
       self.clicked = False

   def check_hover(self):
       if self.rect.collidepoint(pygame.mouse.get_pos()):
           if not self.hovered:
               self.hovered = True
       else:
           self.hovered = False

   def update(self, surface):
       """Update needs to be called every frame in the main loop."""
       color = self.color
       text = self.text
       self.check_hover()
       if self.clicked and self.clicked_color:
           color = self.clicked_color
           if self.clicked_font_color:
               text = self.clicked_text
       elif self.hovered and self.hover_color:
           color = self.hover_color
           if self.hover_font_color:
               text = self.hover_text
       surface.fill(pygame.Color("black"), self.rect)
       surface.fill(color, self.rect.inflate(-4, -4))
       if self.text:
           text_rect = text.get_rect(center=self.rect.center)
           surface.blit(text, text_rect)


class Button2(object):
   """A fairly straight forward button class."""
   def __init__(self, rect, color, function, **kwargs):
       self.rect = pygame.Rect(rect)
       self.color = color
       self.function = function
       self.clicked = False
       self.hovered = False
       self.hover_text = None
       self.clicked_text = None
       self.process_kwargs(kwargs)
       self.render_text()

   def process_kwargs(self, kwargs):
       """Various optional customization you can change by passing kwargs."""
       options = {"text": None,
                  "font": pygame.font.Font(settings.FONT,settings.FONT_SIZE),
                  "call_on_release": True,
                   "hover_color": None,
                   "clicked_color": None,
                   "font_color": settings.WHITE,
                   "hover_font_color": None,
                   "clicked_font_color": None}
       for kwarg in kwargs:
           if kwarg in options:
               options[kwarg] = kwargs[kwarg]
           else:
               raise AttributeError("Button has no keyword: {}".format(kwarg))
       self.__dict__.update(options)

   def render_text(self):
       """Pre render the button text."""
       if self.text:
           if self.hover_font_color:
               color = self.hover_font_color
               self.hover_text = self.font.render(self.text, True, color)
           if self.clicked_font_color:
               color = self.clicked_font_color
               self.clicked_text = self.font.render(self.text, True, color)
           self.text = self.font.render(self.text, True, self.font_color)

   def check_event(self, event):
       """The button needs to be passed events from your program event loop."""
       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           self.on_click(event)
       elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
           self.on_release(event)

   def on_click(self, event):
       if self.rect.collidepoint(event.pos):
           self.clicked = True
           if not self.call_on_release:
               self.function()

   def on_release(self, event):
       if self.clicked and self.call_on_release:
           self.function()
       self.clicked = False

   def check_hover(self):
       if self.rect.collidepoint(pygame.mouse.get_pos()):
           if not self.hovered:
               self.hovered = True
       else:
           self.hovered = False

   def update(self, surface):
       """Update needs to be called every frame in the main loop."""
       color = self.color
       text = self.text
       self.check_hover()
       if self.clicked and self.clicked_color:
           color = self.clicked_color
           if self.clicked_font_color:
               text = self.clicked_text
       elif self.hovered and self.hover_color:
           color = self.hover_color
           if self.hover_font_color:
               text = self.hover_text
       surface.fill(pygame.Color("black"), self.rect)
       surface.fill(color, self.rect.inflate(-4, -4))
       if self.text:
           text_rect = text.get_rect(center=self.rect.center)
           surface.blit(text, text_rect)