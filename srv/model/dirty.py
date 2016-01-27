from model.gameobject import GameObject

def dirty(gameobject):
    """helper which marks objects as dirty so that they will get saved by the 
    Storage class"""
    if isinstance(gameobject, GameObject):
        gameobject.dirty()
