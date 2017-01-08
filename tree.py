def update_winner(temp0, history, learning_rate, N):
    temp = temp0["-1"]["next"]
    m = len(history)
    for i in history[:-1]:
        temp = temp[str(i)]["next"]
    temp[str(history[-1])]["pro"] = N
    G = N / 2
    for j in range(1, m):
        temp = temp0["-1"]["next"]
        rate = int((64 - m + j) / learning_rate)
        if rate < 3:
            rate = 3
        G /= rate
        for i in history[:- (j + 1)]:
            temp = temp[str(i)]["next"]
        temp[str(history[- (j + 1)])]["pro"] += G


def update_loser(temp0, history, learning_rate, N):
    temp = temp0["-1"]["next"]
    m = len(history) - 1
    for i in history[:-2]:
        temp = temp[str(i)]["next"]
    temp[str(history[-2])]["pro"] = 0
    G = N / 2
    for j in range(1, m):
        temp = temp0["-1"]["next"]
        rate = int((64 - m + j) / learning_rate)
        if rate < 3:
            rate = 3
        G /= rate
        for i in history[:- (j + 2)]:
            temp = temp[str(i)]["next"]
        temp[str(history[- (j + 2)])]["pro"] -= G


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabVecs(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)