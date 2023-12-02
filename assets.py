mountain_image = 'images/bg/mountains.png'
trees_image = 'images/bg/trees.png'
bushes_image = 'images/bg/bushes.png'

sky_image = 'images/bg/sky.png'

def heart_image(image_number):
    return f'images/heart/heart{image_number}.png'

def background_assets(pygame):
    background_assets = []
    background_assets.append(pygame.image.load(mountain_image).convert_alpha())
    background_assets.append(pygame.image.load(trees_image).convert_alpha())
    background_assets.append(pygame.image.load(bushes_image).convert_alpha())
    return background_assets
