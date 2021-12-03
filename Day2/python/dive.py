def read_data(file_path: str) -> tuple:
    """
    Read task input data and create list for solve
    Args:
        file_path (str): Path to input file
    Returnes:
        [tuple]: result tuple of input data 
    """
    with open(file_path, 'r') as file:
        result_tuple = tuple(x.strip() for x in file.readlines())
    return result_tuple


def get_final_horizontal_position(data: tuple) -> int:
    """Calculate final horizontal position by your final depth of submarine by execute command from input data

    Args:
        data (tuple): [description]

    Returns:
        int: [description]
    """
    depth = 0
    hop = 0

    for move in data:
        direction, unites = move.split()
        if direction == 'forward':
            hop += int(unites)
        elif direction == 'down':
            depth += int(unites)
        else:
            depth -= int(unites)
    return hop * depth

def get_aimed_horizontal_position(data: tuple) -> int:
    depth = 0
    hop = 0
    aim = 0

    for move in data:
        direction, unites = move.split()
        if direction == 'forward':
            hop += int(unites)
            depth += aim * int(unites)
        elif direction == 'down':
            aim += int(unites)
        else:
            aim -= int(unites)
    return hop * depth

if __name__ == "__main__":
    data = read_data("../input/input.txt")
    res1 = get_final_horizontal_position(data)
    res2 = get_aimed_horizontal_position(data)
