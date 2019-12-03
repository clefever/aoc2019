import adventofcode
from collections import defaultdict

# TODO: Refactor horrible code


def intersect_distance(wire1, wire2):
    """
    >>> intersect_distance(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4'])
    6
    >>> intersect_distance(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
    159
    >>> intersect_distance(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
    135
    """
    map = defaultdict(lambda: 0)
    num = 0
    for wire in [wire1, wire2]:
        loc = (0, 0)
        num += 1
        for seg in wire:
            dist = int(seg[1:])
            if seg[0] == "U":
                for y in range(loc[1]+1, loc[1]+dist+1):
                    map[(loc[0], y)] |= num
                loc = (loc[0], loc[1]+dist)
            if seg[0] == "D":
                for y in range(loc[1]-1, loc[1]-dist-1, -1):
                    map[(loc[0], y)] |= num
                loc = (loc[0], loc[1]-dist)
            if seg[0] == "R":
                for x in range(loc[0]+1, loc[0]+dist+1):
                    map[(x, loc[1])] |= num
                loc = (loc[0]+dist, loc[1])
            if seg[0] == "L":
                for x in range(loc[0]-1, loc[0]-dist-1, -1):
                    map[(x, loc[1])] |= num
                loc = (loc[0]-dist, loc[1])

    coords = []

    for coord in map:
        if map[coord] == 3:
            coords.append(coord)

    min = 9999999
    for coord in coords:
        if abs(coord[0]) + abs(coord[1]) < min:
            min = abs(coord[0]) + abs(coord[1])

    return min


def intersect_min_steps(wire1, wire2):
    """
    >>> intersect_min_steps(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4'])
    30
    >>> intersect_min_steps(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
    610
    >>> intersect_min_steps(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
    410
    """
    map = defaultdict(lambda: (0, 0, 0))
    num = 0
    for wire in [wire1, wire2]:
        loc = (0, 0)
        num += 1
        step = 0
        for seg in wire:
            dist = int(seg[1:])
            if seg[0] == "U":
                for y in range(loc[1]+1, loc[1]+dist+1):
                    step += 1
                    step_t = map[(loc[0], y)]
                    if num == 1 and (step < step_t[0] or step_t[0] == 0):
                        map[(loc[0], y)] = (step, step_t[1], step_t[2] | num)
                    if num == 2 and (step < step_t[1] or step_t[1] == 0):
                        map[(loc[0], y)] = (step_t[0], step, step_t[2] | num)
                loc = (loc[0], loc[1]+dist)
            if seg[0] == "D":
                for y in range(loc[1]-1, loc[1]-dist-1, -1):
                    step += 1
                    step_t = map[(loc[0], y)]
                    if num == 1 and (step < step_t[0] or step_t[0] == 0):
                        map[(loc[0], y)] = (step, step_t[1], step_t[2] | num)
                    if num == 2 and (step < step_t[1] or step_t[1] == 0):
                        map[(loc[0], y)] = (step_t[0], step, step_t[2] | num)
                loc = (loc[0], loc[1]-dist)
            if seg[0] == "R":
                for x in range(loc[0]+1, loc[0]+dist+1):
                    step += 1
                    step_t = map[(x, loc[1])]
                    if num == 1 and (step < step_t[0] or step_t[0] == 0):
                        map[(x, loc[1])] = (step, step_t[1], step_t[2] | num)
                    if num == 2 and (step < step_t[1] or step_t[1] == 0):
                        map[(x, loc[1])] = (step_t[0], step, step_t[2] | num)
                loc = (loc[0]+dist, loc[1])
            if seg[0] == "L":
                for x in range(loc[0]-1, loc[0]-dist-1, -1):
                    step += 1
                    step_t = map[(x, loc[1])]
                    if num == 1 and (step < step_t[0] or step_t[0] == 0):
                        map[(x, loc[1])] = (step, step_t[1], step_t[2] | num)
                    if num == 2 and (step < step_t[1] or step_t[1] == 0):
                        map[(x, loc[1])] = (step_t[0], step, step_t[2] | num)
                loc = (loc[0]-dist, loc[1])

    coords = []

    for coord in map:
        if map[coord][2] == 3:
            coords.append((coord, map[coord]))

    min = 9999999
    for coord in coords:
        if coord[1][0] + coord[1][1] < min:
            min = coord[1][0] + coord[1][1]

    return min


def main():
    puzzle_input = adventofcode.read_input(3)
    wire1, wire2 = puzzle_input[0].split(','), puzzle_input[1].split(',')
    adventofcode.answer(1, 709, intersect_distance(wire1, wire2))
    adventofcode.answer(2, 13836, intersect_min_steps(wire1, wire2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
