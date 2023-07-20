def f(num=0):
    if num == 0:
        day = "水曜日"
    elif num == 1:
        day = "木曜日"
    elif num == 2:
        day = "金曜日"
    elif num == 3:
        day = "土曜日"
    elif num == 4:
        day = "日曜日"
    elif num == 5:
        day = "月曜日"
    elif num == 6:
        day = "火曜日"
    else:
        day = "今日より１日を超えて離れた日"
    return day


n = int(input())
print(f(n))
