from model.abilities.ability import Ability
ABILITIES = {
}

def AbilityFactory(ability_type, *args, **kwargs):
    return CommonFactory("ability", ability_type, ABILITIES, *args, **kwargs)
