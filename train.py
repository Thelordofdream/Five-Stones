# coding=utf-8
from play_chess import *
from tree import *

former_add = "former.txt"
later_add = "later.txt"
learning_rate = 0.5
learning_rate = 1 / learning_rate
former = {"-1": {"next": {}, "pro": 0}}
later = {"-1": {"next": {}, "pro": 0}}
round = 32
iteration = 10000
N = 100000
display = 2000
former_count = 0
later_count = 0

choice = []
for a in range(64):
    choice.append(N / 2)

map = []
for i in range(64):
    map.append(0)

for t in range(iteration):
    if t % display == 0:
        print "Iteration: %d" % t
        print "Former: %d" % former_count
        print "Later : %d" % later_count
        former_count = 0
        later_count = 0
    former_last_state = -1
    later_last_state = -1

    for a in range(64):
        map[a] = 0

    history = []
    temp1 = former
    temp2 = later["-1"]["next"]
    winner = 0

    for i in range(round):
        # while over == 1:
        # print "------- round %d -------" % (i + 1)
        temp1 = temp1[str(later_last_state)]["next"]
        next_step = make_decision(choice, history, temp1, N)
        former_last_state = next_step
        map[next_step] = 3
        history.append(next_step)

        if not temp1.has_key(str(next_step)):
            temp1[str(next_step)] = {"next": {}, "pro": N / 2}
        temp1 = temp1[str(former_last_state)]["next"]

        # print_result(former_last_state, map)
        over, winner = check_over(map)
        if over == 1:
            break

        if not temp2.has_key(str(former_last_state)):
            temp2[str(former_last_state)] = {"next": {}, "pro": N / 2}

        temp2 = temp2[str(former_last_state)]["next"]
        next_step = make_decision(choice, history, temp2, N)
        later_last_state = next_step
        map[next_step] = 4
        history.append(next_step)
        # print_result(later_last_state, map)
        # print ""

        if not temp2.has_key(str(next_step)):
            temp2[str(next_step)] = {"next": {}, "pro": N / 2}
        temp2 = temp2[str(later_last_state)]["next"]

        over, winner = check_over(map)
        if over == 1:
            break

        if not temp1.has_key(str(later_last_state)):
            temp1[str(later_last_state)] = {"next": {}, "pro": N / 2}

    # print history
    finished_thread = [0]
    if winner == 3:
        update_winner(former, history, learning_rate, N)
        update_loser(later, history, learning_rate, N)
        former_count += 1
    if winner == 4:
        update_winner(later, history, learning_rate, N)
        update_loser(former, history, learning_rate, N)
        later_count += 1

print former_count
print later_count
storeTree(former, former_add)
storeTree(later, later_add)
