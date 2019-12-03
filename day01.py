import adventofcode


def fuel_required(mass):
    """
    >>> fuel_required(12)
    2
    >>> fuel_required(14)
    2
    >>> fuel_required(1969)
    654
    >>> fuel_required(100756)
    33583
    """
    return mass // 3 - 2


def fuel_required_extra(mass):
    """
    >>> fuel_required_extra(14)
    2
    >>> fuel_required_extra(1969)
    966
    >>> fuel_required_extra(100756)
    50346
    """
    fuel = 0
    next_fuel = mass
    while (next_fuel := fuel_required(next_fuel)) > 0:
        fuel += next_fuel
    return fuel


def sum_of_fuel(puzzle_input, func):
    return sum([func(int(line)) for line in puzzle_input])


def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 3154112, sum_of_fuel(puzzle_input, fuel_required))
    adventofcode.answer(2, 4728317, sum_of_fuel(puzzle_input, fuel_required_extra))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
