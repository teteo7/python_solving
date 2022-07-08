#제목: 터렛
"""
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
"""

import math

# 3
T = int(input("값입력: "))

# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input("입력: ").split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
            print(0)
        elif abs(r1 - r2) == distance or r1 + r2 == distance:
            print(1)
        else:
            print(2)

