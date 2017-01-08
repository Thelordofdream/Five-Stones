# coding=utf-8
import numpy as np
cutting_depth =0.5

def getPro(subtree, history, N):
    m = 64 - len(history) - 1
    delta = 0
    for i in subtree.keys():
        delta += subtree[str(i)]["pro"] - N / 2
    result = delta / m + N / 2
    return result


def make_decision(choice, history, temp_tree, N):
    for a in range(64):
        if a in history:
            choice[a] = 0
        else:
            choice[a] = N / 2
    if not temp_tree == {}:
        for b in temp_tree.keys():
            m = getPro(temp_tree[b]["next"], history, N)
            if m <= int(N * cutting_depth / 2):
                choice[int(b)] = 0
            else:
                choice[int(b)] = m
    s = sum(choice)
    next_num = np.random.randint(s)
    s = 0
    next_step = 0
    for a in range(64):
        s += choice[a]
        if s > next_num:
            next_step = a
            break
    return next_step


def print_result(map):
    # raw = state / 8
    # column = state % 8
    # print "------ former ------"
    # print raw + 1, column + 1
    for x in range(8):
        line = ""
        for y in range(8):
            line += str(map[x * 8 + y]) + " "
        print line


def check_over(map):
    winner = 0
    over = 0
    # 行检测
    for i in range(8):
        for j in range(4):
            if map[i * 8 + j] == 4:
                if map[i * 8 + j + 4] == 4:
                    if sum(map[i * 8 + j + 1:i * 8 + j + 4]) == 12:
                        over = 1
                        winner = 4
                        # print i + 1, j + 1, 1
                        # print over, winner
                        return over, winner
    for i in range(8):
        for j in range(4):
            if map[i * 8 + j] == 3:
                if map[i * 8 + j + 4] == 3:
                    if sum(map[i * 8 + j + 1:i * 8 + j + 4]) == 9:
                        over = 1
                        winner = 3
                        # print i + 1, j + 1, 1
                        # print over, winner
                        return over, winner
    # 列检测
    for i in range(8):
        for j in range(4):
            if map[i + j * 8] == 4:
                if map[i + (j + 4) * 8] == 4:
                    s = 0
                    for x in range(3):
                        s += map[i + (j + 1 + x) * 8]
                    if s == 12:
                        over = 1
                        winner = 4
                        # print j + 1, i + 1, 2
                        # print over, winner
                        return over, winner
    for i in range(8):
        for j in range(4):
            if map[i + j * 8] == 3:
                if map[i + (j + 4) * 8] == 3:
                    s = 0
                    for x in range(3):
                        s += map[i + (j + 1 + x) * 8]
                    if s == 9:
                        over = 1
                        winner = 3
                        # print j + 1, i + 1, 2
                        # print over, winner
                        return over, winner
    # 右斜检测
    for i in range(4):
        for j in range(4):
            if map[i + j * 8] == 4:
                if map[i + 4 + (j + 4) * 8] == 4:
                    s = 0
                    for x in range(3):
                        s += map[i + x + 1 + (j + 1 + x) * 8]
                    if s == 12:
                        over = 1
                        winner = 4
                        # print j + 1, i + 1, 3
                        # print over, winner
                        return over, winner
    for i in range(4):
        for j in range(4):
            if map[i + j * 8] == 3:
                if map[i + 4 + (j + 4) * 8] == 3:
                    s = 0
                    for x in range(3):
                        s += map[i + x + 1 + (j + 1 + x) * 8]
                    if s == 9:
                        over = 1
                        winner = 3
                        # print j + 1, i + 1, 3
                        # print over, winner
                        return over, winner
    # 左斜检测
    for i in range(4, 8):
        for j in range(4):
            if map[i + j * 8] == 4:
                if map[i - 4 + (j + 4) * 8] == 4:
                    s = 0
                    for x in range(3):
                        s += map[i - x - 1 + (j + 1 + x) * 8]
                    if s == 12:
                        over = 1
                        winner = 4
                        # print j + 1, i + 1, 4
                        # print over, winner
                        return over, winner
    for i in range(4, 8):
        for j in range(4):
            if map[i + j * 8] == 3:
                if map[i - 4 + (j + 4) * 8] == 3:
                    s = 0
                    for x in range(3):
                        s += map[i - x - 1 + (j + 1 + x) * 8]
                    if s == 9:
                        over = 1
                        winner = 3
                        # print j + 1, i + 1, 4
                        # print over, winner
                        return over, winner
    return over, winner
