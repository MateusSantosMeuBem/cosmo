def get_variations(
    actions: list[str],
    middles: list[str],
    objects: list[str]
) -> list[str]:
    variations: list[str] = []

    for action in actions:
        for middle in middles:
            for object in objects:
                variations.append(' '.join([action, middle, object]))
    
    for action in actions:
        for object in objects:
            variations.append(' '.join([action, object]))

    for object in objects:
        variations.append(object)

    return variations
    
