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


if __name__ == "__main__":
    data = read_data("../input/input.txt")
    numbers = data[0].split(',')
    c = 0
    i = 0
    grid_list = [[]]
    for x in data[2:]:
        if x != '':
            if c < 5:
                grid_list[i].append(x)
                c += 1
            else:
                c = 1
                i += 1
                grid_list.append([x, ])
    res_dict = {}
    for n in numbers:
        for matrix_num in range(len(grid_list)):
            for r in range(5):
                for c in range(5):
                    pass