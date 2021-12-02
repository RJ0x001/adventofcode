def read_data(file_path: str) -> tuple:
    """
    Read task input data and create list for solve
    Args:
        file_path (str): Path to input file
    Returnes:
        [tuple]: result tuple of input data 
    """
    with open(file_path, 'r') as file:
        result_tuple = tuple(int(x.strip()) for x in file.readlines())
    return result_tuple


def count_increased_measurement(data: tuple) -> int:
    """Calculate how many measurements are larger than the previous

    Args:
        data (tuple): data input

    Returns:
        int: counting result
    """
    res = 0
    l = len(data)
    for i in range(1, l):
        if data[i] > data[i - 1]:
            res += 1
    return res

def count_increased_measurement_window(data: tuple) -> int:
    """counting the number of times the sum of measurements in this sliding window increases from the previous sum

    Args:
        data (tuple): data input

    Returns:
        int: counting result
    """
    current = data[0] + data[1] + data[2]
    res = 0
    l = len(data)
    for x in range(1, l - 2):
        next_sum = data[x] + data[x + 1] + data[x + 2]
        if next_sum > current:
            res += 1
        current = next_sum
    return res


if __name__ == "__main__":
    data = read_data("../input/task1.txt")
    res1 = count_increased_measurement(data)
    res2 = count_increased_measurement_window(data)
