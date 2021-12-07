import copy
import pprint


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


def check_first_win(d_r: dict, d_c: dict):
    for m_k, m in d_r.items():
        for k, v in m.items():
            if False not in v:
                return m_k, k, 'r'
    for m_k, m in d_c.items():
        for k, v in m.items():
            if False not in v:
                return m_k, k, 'c'

def check_last_win():
    pass


def count_prize(pos, pos_number, matrix_key, grid, transpose, marked_dict_tuple, win_number):
    print(pos, pos_number, matrix_key, win_number)
    if pos == 'r':
        wining_matrix = copy.deepcopy(grid[matrix_key])
        marked_dict = marked_dict_tuple[0]
        for k, v in marked_dict[matrix_key].items():
            for i, status in enumerate(v):
                    if status:
                        elem = grid[matrix_key][k][i]
                        wining_matrix[k].remove(elem)
        wining_matrix = [int(a) for b in wining_matrix for a in b]
        return sum(wining_matrix) * int(win_number)
    else:
        wining_matrix = copy.deepcopy(transpose[matrix_key])
        marked_dict = marked_dict_tuple[1]
        for k, v in marked_dict[matrix_key].items():
            for i, status in enumerate(v):
                    if status:
                        elem = transpose[matrix_key][k][i]
                        wining_matrix[k].remove(elem)
        wining_matrix = [int(a) for b in wining_matrix for a in b]
        return sum(wining_matrix) * int(win_number)

def bingo(bingo_numbers, bingo_data):
    c = 0
    i = 0
    wining_order = []
    win_condition = []
    grid_list = [[]]
    for x in bingo_data:
        if x != '':
            if c < 5:
                grid_list[i].append([r for r in x.split()])
                c += 1
            else:
                c = 1
                i += 1
                grid_list.append([[r for r in x.split()], ])
    transpose_grid = []
    for m in grid_list:
        transpose_grid.append([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))])
    res_dict_row, res_dict_col, marked_stat_dict = dict(), dict(), dict()
    for m in range(len(grid_list)):
        res_dict_row[m] = dict()
        res_dict_col[m] = dict()
        for c in range(5):
            res_dict_row[m][c] = [False] * 5
            res_dict_col[m][c] = [False] * 5
    for n in bingo_numbers:
        for matrix_num in range(len(grid_list)):
            for r in range(5):
                for c in range(5):
                    if grid_list[matrix_num][r][c] == n:
                        res_dict_row[matrix_num][r][c] = True
                    if transpose_grid[matrix_num][r][c] == n:
                        res_dict_col[matrix_num][r][c] = True
        marked_stat_dict[n] = {'r': copy.deepcopy(res_dict_row), 'c': copy.deepcopy(res_dict_col)}

        # pprint.pprint(marked_stat_dict["99"])
        # first task
        # 
        # win = check_first_win(res_dict_row, res_dict_col)
        # if win:
        #     return count_prize(win[2], int(win[1]), win[0], grid_list, transpose_grid, (res_dict_row, res_dict_col),
        #      n)
        # second task
        # 
        
        win = check_first_win(res_dict_row, res_dict_col)
        if win:
            if win[0] not in wining_order:
                wining_order.append(win[0])
                win_condition.append((win, n), )
    win = win_condition[-1]
    pprint.pprint(marked_stat_dict[win[1]]['r'])
    return count_prize(win[0][2], int(win[0][1]), win[0][0], grid_list, transpose_grid,
     (marked_stat_dict[win[1]]['r'], marked_stat_dict[win[1]]['c']), win[1])



if __name__ == "__main__":
    data = read_data("..\input\input.txt")
    numbers = data[0].split(',')
    print(bingo(numbers, data[2:]))