import adventofcode


def total_orbits(orbits):
    """
    >>> total_orbits([["COM", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"], ["B", "G"], ["G", "H"], ["D", "I"], ["E", "J"], ["J", "K"], ["K", "L"]])
    42
    """
    orbit_dict = {orbits[i][1]: orbits[i][0] for i in range(len(orbits))}
    total = 0
    for orbit in orbit_dict.keys():
        total += 1
        while orbit_dict[orbit] in orbit_dict:
            orbit = orbit_dict[orbit]
            total += 1
    return total


def orbit_transfers(orbits, obj_name_1, obj_name_2):
    """
    >>> orbit_transfers([["COM", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"], ["B", "G"], ["G", "H"], ["D", "I"], ["E", "J"], ["J", "K"], ["K", "L"], ["K", "YOU"], ["I", "SAN"]], "YOU", "SAN")
    4
    """
    orbit_dict = {orbits[i][1]: orbits[i][0] for i in range(len(orbits))}
    orbit_list1 = []
    orbit_list2 = []
    for orbit in orbit_dict.keys():
        if orbit == obj_name_1:
            orbit_list1.append(orbit_dict[orbit])
            while orbit_dict[orbit] in orbit_dict:
                orbit = orbit_dict[orbit]
                orbit_list1.append(orbit_dict[orbit])
        elif orbit == obj_name_2:
            orbit_list2.append(orbit_dict[orbit])
            while orbit_dict[orbit] in orbit_dict:
                orbit = orbit_dict[orbit]
                orbit_list2.append(orbit_dict[orbit])
    return len(list(set(orbit_list1) - set(orbit_list2))) + len(list(set(orbit_list2) - set(orbit_list1)))


def main():
    puzzle_input = adventofcode.read_input(6)
    orbits = [orbit.split(')') for orbit in puzzle_input]
    adventofcode.answer(1, 253104, total_orbits(orbits))
    adventofcode.answer(2, 499, orbit_transfers(orbits, "YOU", "SAN"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
