from config import WINDOW_WIDTH
import math


def background_draw_sky(display, image):
    num_bg_tiles = math.ceil(WINDOW_WIDTH / image.get_width()) + 1
    # draw the sky
    for i in range(num_bg_tiles):
        display.blit(image, (i * image.get_width(), 0))
    
def background_draw_layers(display, image, array_of_asset, parallax):
    num_bg_tiles = math.ceil(WINDOW_WIDTH / image.get_width()) + 1
    # draw each background layer
    for i in range(len(array_of_asset)):
        
        bg = array_of_asset[i]
        
        for j in range(num_bg_tiles):
            display.blit(bg, (j * bg.get_width() + parallax[i], 0))

def background_manager(display, parallax, array_of_asset, image):
    num_bg_tiles = math.ceil(WINDOW_WIDTH / image.get_width()) + 1
    background_draw_sky(display, image)
    background_draw_layers(display, image, array_of_asset, parallax)

    # draw each background layer
    for i in range(len(array_of_asset)):
        
        bg = array_of_asset[i]
        
        for j in range(num_bg_tiles):
            display.blit(bg, (j * bg.get_width() + parallax[i], 0))
            
    # update how much each layer will scroll
    for i in range(len(parallax)):
        
        # top layer should scroll faster
        parallax[i] -= i + 1
        
        if abs(parallax[i]) > array_of_asset[i].get_width():
            parallax[i] = 0
