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

def get_rate(data: tuple, type: str) -> int:
    """Calculate gamma rate and the epsilon rate from data

    Args:
        data (tuple): data tuple
        type (str): gamma or epsilon rate

    Returns:
        int: result rate integer 
    """
    gamma_list = tuple(dict() for _ in range(len(data[0])))
    for x in data:
        l = len(x)
        for i in range(l):
            try:
                gamma_list[i][x[i]] += 1
            except KeyError:
                gamma_list[i][x[i]] = 1
    if type == 'gamma':
        return  int(''.join(x for x in [max(d, key=lambda x: d[x]) for d in gamma_list]), 2)
    else:
        return  int(''.join(x for x in [min(d, key=lambda x: d[x]) for d in gamma_list]), 2)

def get_life_support_rating(data: tuple) -> int:
    """
    Calculate life support rating by multiply the oxygen generator rating (23) by the CO2 scrubber rating (10)

    Args:
        data (tuple): data tuple

    Returns:
        int: life support rating
    101000100001
    """
    elem = dict()
    input_elem_len = len(data[0])
    oxygen_data = data
    co2_data = data
    for i in range(input_elem_len):
        for x in oxygen_data:
            try:
                elem[x[i]] += 1
            except KeyError:
                elem[x[i]] = 0
        current_value_oxygen = max(elem, key=lambda x: elem[x])
        
        oxygen_data = tuple(x for x in oxygen_data if x[i] == current_value_oxygen)
        elem = dict()

        for x in co2_data:
            try:
                elem[x[i]] += 1
            except KeyError:
                elem[x[i]] = 0
        current_value_co2 = min(elem, key=lambda x: elem[x])
        co2_data = tuple(x for x in co2_data if x[i] == current_value_co2)
        elem = dict()

    return int(oxygen_data[0], 2) * int(co2_data[0], 2)

if __name__ == "__main__":
    data = read_data("../input/input.txt")
    get_rate(data, 'gamma') * get_rate(data, 'epsilon ')
    get_life_support_rating(data)
