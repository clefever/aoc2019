from fractions import Fraction
import math
import adventofcode


def part1(puzzle_input):
    coords = list_from_input(puzzle_input)
    return max(detected_from_pos(coord, coords) for coord in coords)


def part2(puzzle_input, best_coord):
    coords = list_from_input(puzzle_input)
    detected = sorted_destroy_list(best_coord, coords)
    coord = detected[199][4]
    return coord[0] * 100 + coord[1]


def sorted_destroy_list(coord, coords):
    destroy_list = []
    coords_copy = coords.copy()
    coords_copy.remove(coord)
    for c in coords_copy:
        if c[0] == coord[0]:
            dist = coord_distance(c, coord)
            if c[1] < coord[1]:
                destroy_list.append((math.inf, 1, dist, c))
            else:
                destroy_list.append((math.inf, 3, dist, c))
    coords_copy = [c for c in coords_copy if c[0] != coord[0]]
    for c in coords_copy:
        sid = slope_intercept_dir(coord, c)
        dist = coord_distance(c, coord)
        quad = get_quad(coord, c)
        slope = abs(sid[0]) if quad == 1 or quad == 3 else -abs(sid[0])
        destroy_list.append((slope, quad, dist, c))
    sorted_list = sorted(destroy_list, key=lambda tup: (-tup[0],tup[1],tup[2]))
    counts = {}
    nums = {}
    for c in sorted_list:
        if (c[0], c[1]) not in counts:
            counts[(c[0], c[1])] = 1
        else:
            counts[(c[0], c[1])] += 1
        nums[(c[0], c[1], c[2])] = counts[(c[0], c[1])]
    new_list = [(nums[c[0], c[1], c[2]], c[0], c[1], c[2], c[3]) for c in sorted_list]
    return sorted(new_list, key=lambda tup: (tup[0],tup[2],-tup[1],tup[3]))


def get_quad(coord1, coord2):
    if (coord2[1] < coord1[1] and coord2[0] >= coord1[0]):
        return 1
    elif (coord2[1] >= coord1[1] and coord2[0] > coord1[0]):
        return 2
    elif (coord2[1] > coord1[1] and coord2[0] <= coord1[0]):
        return 3
    else:
        return 4


def coord_distance(coord1, coord2):
    """
    >>> coord_distance((-3,7),(1,2))
    6.4031242374328485
    """
    return math.sqrt(abs(coord2[0] - coord1[0]) ** 2 + abs(coord2[1] - coord1[1]) ** 2)


def detected_from_pos(coord, coords):
    coords_copy = coords.copy()
    coords_copy.remove(coord)
    vertical_lower = any([c[0] == coord[0] for c in coords_copy if c[1] < coord[1]])
    vertical_upper = any([c[0] == coord[0] for c in coords_copy if c[1] > coord[1]])
    coords_copy = [c for c in coords_copy if c[0] != coord[0]]
    unique_slopes_and_intercepts = set()
    for c in coords_copy:
        unique_slopes_and_intercepts.add(slope_intercept_dir(coord, c))
    one_more = 1 if vertical_lower else 0
    one_more2 = 1 if vertical_upper else 0
    return len(unique_slopes_and_intercepts) + one_more + one_more2


def slope_intercept_dir(coord1, coord2):
    """
    >>> slope_intercept_dir((2,2),(3,4))
    (Fraction(2, 1), Fraction(-2, 1), 1)
    """
    m = Fraction(coord2[1] - coord1[1], coord2[0] - coord1[0])
    b = coord1[1] - (m * coord1[0])
    d = -1 if coord2[0] < coord1[0] else 0 if coord2[0] == coord1[0] else 1
    return (m, b, d)


def list_from_input(puzzle_input):
    coords = []
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            if puzzle_input[y][x] == '#':
                coords.append((x,y))
    return coords


def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 288, part1(puzzle_input))
    adventofcode.answer(1, 616, part2(puzzle_input, (17, 22)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
