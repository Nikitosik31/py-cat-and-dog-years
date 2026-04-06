def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_and_dog_in_human_years = []
    if cat_age < 15:
        cat_and_dog_in_human_years.append(0)
    elif cat_age < 24:
        cat_and_dog_in_human_years.append(1)

    elif cat_age >= 24:
        human_age = (
            (2 + (cat_age - 24) // 4)
        )
        cat_and_dog_in_human_years.append(human_age)

    if dog_age < 15:
        cat_and_dog_in_human_years.append(0)
    elif dog_age < 24:
        cat_and_dog_in_human_years.append(1)
    elif dog_age >= 24:
        human_age = (
            (2 + (dog_age - 24) // 5)
        )
        cat_and_dog_in_human_years.append(human_age)

    return cat_and_dog_in_human_years
