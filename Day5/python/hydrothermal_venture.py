def read_data(file_path: str) -> tuple:
    """
    Read task input data and create list for solve
    Args:
        file_path (str): Path to input file
    Returnes:
        [tuple]: result tuple of input data
    """
    with open(file_path, 'r') as file:
        result_tuple = tuple(x.strip().split('->') for x in file.readlines())

    return result_tuple


def mark_dot(c1, c2, counter, grid, overlap_set):
    try:
        grid[c1][c2] += 1
        if (c1, c2) not in overlap_set:
            overlap_set.add((c1, c2))
            counter += 1
    except TypeError:
        grid[c1][c2] = 1
    return counter


def count_overlap(data):
    counter = 0
    overlap_set = set()
    grid = [[None for _ in range(1000)] for _ in range(1000)]
    for row in data:
        y1, x1 = map(int, row[0].split(','))
        y2, x2 = map(int, row[1].split(','))
        # task 1
        if x1 == x2 or y1 == y2:
            
            if x1 == x2:
                if y2 <= y1:
                    while y2 <= y1:
                        counter = mark_dot(x2, y2, counter, grid, overlap_set)
                        y2 += 1
                else:
                    while y2 >= y1:
                        counter = mark_dot(x2, y2, counter, grid, overlap_set)
                        y2 -= 1
            else:
                if x1 <= x2:
                    while x1 <= x2:
                        counter = mark_dot(x2, y2, counter, grid, overlap_set)
                        x2 -= 1
                else:
                    while x1 >= x2:
                        counter = mark_dot(x2, y2, counter, grid, overlap_set)
                        x2 += 1
        # task 2
        else:
            if x1 <= x2 and y1 >= y2:
                while x1 <= x2 and y1 >= y2:
                    counter = mark_dot(x1, y1, counter, grid, overlap_set)
                    x1 += 1
                    y1 -= 1
            elif x1 >= x2 and y1 <= y2:
                while x1 >= x2 and y1 <= y2:
                    counter = mark_dot(x1, y1, counter, grid, overlap_set)
                    x1 -= 1
                    y1 += 1
            elif x1 >= x2 and y1 >= y2:
                while x1 >= x2 and y1 >= y2:
                    counter = mark_dot(x1, y1, counter, grid, overlap_set)
                    x1 -= 1
                    y1 -= 1
            elif x1 <= x2 and y1 <= y2:
                while x1 <= x2 and y1 <= y2:
                    counter = mark_dot(x1, y1, counter, grid, overlap_set)
                    x1 += 1
                    y1 += 1
    return counter


if __name__ == "__main__":
    raw_data = read_data("../input/input.txt")
    count_overlap(raw_data)