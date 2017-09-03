count = 0

def conflict(pos, chess):
    len_chess = len(chess)
    for i in range(len_chess):
        # if chess[i]-pos==0 or abs(chess[i] - i)==abs(pos-len_chess):
        if abs(chess[i] - pos) in (0, len_chess - i):
            return True
    return False


def Queens(num,chess):
    global count

    if len(chess) == 8:
        count += 1
        print(chess)
    else:
        for pos in range(num):
            if not conflict(pos, chess):
                chess1 = []
                for i in chess:
                    chess1.append(i)
                chess1.append(pos)
                Queens(num,chess1)





board = []
Queens(8,board)
print(count)