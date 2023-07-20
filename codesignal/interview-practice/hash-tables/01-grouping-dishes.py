def solution(dishes):
    ingredient_dishes = {}
    for dish in dishes:
        (dish_name, *ingredients) = dish
        for ingredient in ingredients:
            if ingredient not in ingredient_dishes:
                ingredient_dishes[ingredient] = []
            ingredient_dishes[ingredient].append(dish_name)

    return sorted(
        [
            (ingredient_name, *sorted(dishes))
            for (ingredient_name, dishes) in ingredient_dishes.items()
            if len(dishes) >= 2
        ]
    )
