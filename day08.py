from collections import defaultdict
import adventofcode


def part1(puzzle_input, width, height):
    layers = parse_image_layers(puzzle_input, width, height)
    num_counts = [layer_num_counts(layer, width, height) for layer in layers]
    min_zero_layer = num_counts.index(min(num_counts, key=lambda n: n[0]))
    return num_counts[min_zero_layer][1] * num_counts[min_zero_layer][2]


def part2(puzzle_input, width, height):
    flattened_image = flatten_layers(puzzle_input, width, height)
    return parse_image_text(flattened_image, width)


def parse_image_layers(data, width, height):
    """
    >>> parse_image_layers("123456789012", 3, 2)
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]]
    """
    num_layers = len(data) // (width*height)
    image = [[] for _ in range(num_layers)]
    counter = 0
    for layer in range(num_layers):
        for y in range(height):
            image[layer].append([])
            for _ in range(width):
                image[layer][y].append(int(data[counter]))
                counter += 1
    return image


def layer_num_counts(image, width, height):
    counts = defaultdict(int)
    for y in range(height):
        for x in range(width):
            counts[image[y][x]] += 1
    return counts


def flatten_layers(image, width, height):
    """
    >>> flatten_layers("0222112222120000", 2, 2)
    [[0, 1], [1, 0]]
    """
    layers = parse_image_layers(image, width, height)
    flattened_image = [[2 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            flattened_image[y][x] = next((layer[y][x] for layer in layers if layer[y][x] == 1 or layer[y][x] == 0), 2)
    return flattened_image


def parse_image_text(flattened_image, width):
    letter_width, letter_height = 5, 6
    letter_dict = {
        '111101000011100100001000011110': 'E',
        '111101000011100100001000010000': 'F',
        '100101001011110100101001010010': 'H',
        '100101010011000101001010010010': 'K',
        '100011000101010001000010000100': 'Y'
    }
    return ''.join(letter_dict[square_string(flattened_image, x, letter_width, letter_height)] for x in range(0, width, letter_width))


def square_string(flattened_image, width_offset, width, height):
    return ''.join([str(flattened_image[y][x]) for y in range(height) for x in range(width_offset, width+width_offset)])


def main():
    image_width, image_height = 25, 6
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 1572, part1(puzzle_input, image_width, image_height))
    adventofcode.answer(2, "KYHFE", part2(puzzle_input, image_width, image_height))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
