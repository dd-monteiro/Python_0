def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed: str = seed_type.capitalize()
    if "packets" in unit:
        print(seed, "seeds:", quantity, unit, "avalilable")
    elif "grams" in unit:
        print(seed, "seeds:", quantity, unit, "in total")
    elif "area" in unit:
        print(seed, "seeds: covers", quantity, "square", unit)
    else:
        print("Unkown unit type")
