vote_num = 0


def vote():
    print("投票します")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0


def check_box():
    global vote_num
    print("票の数は {} です".format(vote_num))


vote()
check_box()
vote()
check_box()
for i in range(3):
    vote()
check_box()
reset_box()
check_box()
