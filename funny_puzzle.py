import heapq
import copy
import math

def print_succ(state):
    succ_state = []
    succ_heuristic = []
    for i in range(9):
        if state[i] == 0:
            empty_index = i
    indexes = move_succ(empty_index)
    for i in indexes:
        new_state = copy.deepcopy(state)
        temp = new_state[i]
        new_state[i] = 0
        new_state[empty_index] = temp
        succ_state.append(new_state)
    succ_state = sorted(succ_state)
    for s in succ_state:
        succ_heuristic.append(heuristic(s))

    for i in range(len(succ_state)):
        if i != len(succ_state) - 1:
            print(succ_state[i], "h={}".format(succ_heuristic[i]))
        else:
            print(succ_state[i], "h={}".format(succ_heuristic[i]), end='')

    return succ_state, succ_heuristic


def solve(state):
    open = []
    closed = []
    count_closed = 0
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    ini_heuristic = heuristic(state)
    heapq.heappush(open, (ini_heuristic, state, (0, ini_heuristic, -1)))
    while True:
        if len(open) == 0:
            break

        out = heapq.heappop(open)
        closed.append(out)
        count_closed += 1
        out_state = out[1]
        if out_state == goal:
            path = []
            temp = closed[len(closed) - 1]
            while True:
                parent_index = temp[2][2]
                if parent_index == -1:
                    path.insert(0, temp)
                    break
                else:
                    path.insert(0, temp)
                    temp = closed[parent_index]
            for i in range(len(path)):
                if i != len(path) - 1:
                    print(path[i][1], "h={}".format(path[i][2][1]), "moves:", i)
                else:
                    print(path[i][1], "h={}".format(path[i][2][1]), "moves:", i, end='')
            break
        else:
            succ_state, succ_heuristic = succ(out_state)
            for i in range(len(succ_state)):
                index_open = -1
                index_closed = -1
                for m in range(len(open)):
                    if open[m][1] == succ_state[i]:
                        index_open = m
                for n in range(len(closed)):
                    if closed[n][1] == succ_state[i]:
                        index_closed = n

                g = out[2][0] + 1
                h = succ_heuristic[i]
                # if the successor is not in both open and closed, then put it on open
                if index_open == -1 and index_closed == -1:
                    heapq.heappush(open, (g + h, succ_state[i], (g, h, count_closed - 1)))
                elif index_open >= 0:
                    if (g+h) < open[m][0]:
                        open[m] = (g + h, succ_state[i], (g, h, count_closed - 1))
                elif index_open == -1 and index_closed >= 0:
                    if (g+h) < closed[n][0]:
                        heapq.heappush(open, (g + h, succ_state[i], (g, h, count_closed - 1)))


def succ(state):
    succ_state = []
    succ_heuristic = []
    for i in range(9):
        if state[i] == 0:
            empty_index = i
    indexes = move_succ(empty_index)
    for i in indexes:
        new_state = copy.deepcopy(state)
        temp = new_state[i]
        new_state[i] = 0
        new_state[empty_index] = temp
        succ_state.append(new_state)
        succ_heuristic.append(heuristic(new_state))

    return succ_state, succ_heuristic


def index_to_loc(index):
    row = index // 3
    col = index % 3
    return (row, col)


def loc_to_index(location):
    row = location[0]
    col = location[1]
    index = row * 3 + col
    return index


def move_succ(index):
    indexes = []
    location = index_to_loc(index)
    row = location[0]
    col = location[1]
    if row > 0:
        indexes.append(loc_to_index((row-1, col)))
    if col > 0:
        indexes.append(loc_to_index((row, col-1)))
    if row < 2:
        indexes.append(loc_to_index((row+1, col)))
    if col < 2:
        indexes.append(loc_to_index((row, col+1)))
    return indexes


def cal_distance(index, tile):
    origin_index = tile - 1
    origin_loc = index_to_loc(origin_index)
    loc = index_to_loc(index)
    dis = abs(origin_loc[0] - loc[0]) + abs(origin_loc[1] - loc[1])
    return dis


def heuristic(state):
    summary = 0
    for i in range(9):
        if state[i] != 0:
            summary += cal_distance(i, state[i])
    return summary
