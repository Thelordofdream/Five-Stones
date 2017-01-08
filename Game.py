from play_chess import *
from tree import *
import sys


print "Choose the first hand oreder you want."
print "0 for you first, 1 for AI first."
set = int(sys.stdin.readline())
former_add = "former.txt"
later_add = "later.txt"

N = 100000
map = []
for i in range(64):
    map.append(0)
history = []
choice = []
learning_rate = 0.1
learning_rate = 1 / learning_rate
for a in range(64):
    choice.append(N / 2)

if set == 0:
    print "Loading AI program......"
    AI = grabVecs(later_add)
    AI0 = AI["-1"]["next"]
    over = 0
    round = 0
    while over == 0:
        print_result(map)
        round += 1
        print "===== Round %d =====" % round
        print "raw:"
        raw = int(sys.stdin.readline())
        while raw is None:
            print "raw:"
            raw = int(sys.stdin.readline())
        print "column"
        column = int(sys.stdin.readline())
        while column is None:
            print "column"
            column = int(sys.stdin.readline())
        next_step = (raw - 1) * 8 + (column - 1)
        while next_step >= 64 or next_step in history:
            print "raw:"
            raw = int(sys.stdin.readline())
            while raw is None:
                print "raw:"
                raw = int(sys.stdin.readline())
            print "column"
            column = int(sys.stdin.readline())
            while column is None:
                print "column"
                column = int(sys.stdin.readline())
            next_step = (raw - 1) * 8 + (column - 1)
        former_last_state = next_step
        map[next_step] = 3
        history.append(next_step)
        print_result(map)
        print ""

        # print_result(former_last_state, map)
        over, winner = check_over(map)
        if over == 1:
            update_loser(AI, history, learning_rate, N)
            storeTree(AI, later_add)
            print "Game Over, You win!"
            break
        if not AI0.has_key(str(former_last_state)):
            AI0[str(former_last_state)] = {"next": {}, "pro": N / 2}
        AI0 = AI0[str(former_last_state)]["next"]

        next_step = make_decision(choice, history, AI0, N)
        later_last_state = next_step
        map[next_step] = 4
        history.append(next_step)

        if not AI0.has_key(str(next_step)):
            AI0[str(next_step)] = {"next": {}, "pro": N / 2}
        AI0 = AI0[str(later_last_state)]["next"]

        over, winner = check_over(map)
        if over == 1:
            update_winner(AI, history, learning_rate, N)
            storeTree(AI, later_add)
            print "Game Over, AI win!"
            break

elif set == 1:
    print "Loading AI program......"
    AI = grabVecs(former_add)
    AI0 = AI
    over = 0
    later_last_state = -1
    round = 0
    while over == 0:
        round += 1
        print "===== Round %d =====" % round
        AI0 = AI0[str(later_last_state)]["next"]
        next_step = make_decision(choice, history, AI0, N)
        former_last_state = next_step
        map[next_step] = 3
        history.append(next_step)

        if not AI0.has_key(str(next_step)):
            AI0[str(next_step)] = {"next": {}, "pro": N / 2}
        AI0 = AI0[str(former_last_state)]["next"]

        # print_result(former_last_state, map)
        over, winner = check_over(map)
        if over == 1:
            update_winner(AI, history, learning_rate, N)
            storeTree(AI, former_add)
            print "Game Over, AI win!"
            break
        print_result(map)
        print "raw:"
        raw = int(sys.stdin.readline())
        while raw is None:
            print "raw:"
            raw = int(sys.stdin.readline())
        print "column"
        column = int(sys.stdin.readline())
        while column is None:
            print "column"
            column = int(sys.stdin.readline())
        next_step = (raw - 1) * 8 + (column - 1)
        while next_step >= 64 or next_step in history:
            print "raw:"
            raw = int(sys.stdin.readline())
            while raw is None:
                print "raw:"
                raw = int(sys.stdin.readline())
            print "column"
            column = int(sys.stdin.readline())
            while column is None:
                print "column"
                column = int(sys.stdin.readline())
            next_step = (raw - 1) * 8 + (column - 1)
        later_last_state = next_step
        map[next_step] = 4
        history.append(next_step)
        print_result(map)
        print ""
        over, winner = check_over(map)
        if over == 1:
            print history
            update_loser(AI, history, learning_rate, N)
            storeTree(AI, former_add)
            print "Game Over, You win!"
            break
        if not AI0.has_key(str(later_last_state)):
            AI0[str(later_last_state)] = {"next": {}, "pro": N / 2}
