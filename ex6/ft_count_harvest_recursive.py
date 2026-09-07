def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    countdown(1, days)


def countdown(current, days) -> None:
    if current > days:
        print("Harvest time!")
    else:
        print(f"Day {current}")
        countdown(current + 1, days)
