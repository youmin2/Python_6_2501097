#39
a = int(input("숫자 하나 입력: "))

def b():
    for i in range(0, a+1):
        if i % 2 != 0:
            print(i, end=' ')

b()

#40
c = int(input("숫자 하나 입력: "))

def d():
    for i in range(1, c+1):
        if i % 3 == 0:
            print(i, end=' ')

d()

#41
e, f, g, h = map(int, input("숫자 4개 입력: ").split())

def i(n1, n2, n3, n4):
    Max = max(n1, n2, n3, n4)
    Min = min(n1, n2, n3, n4)
    return Max, Min

MAX, MIN = i(e, f, g, h)

print("최댓값: ", MAX)
print("최솟값: ", MIN)

#42

#43
n = int(input("정수 입력: "))

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

print(factorial(n))

#44
i, j = map(int, input("양수 두개 입력: ").split())

def k(n1, n2):
    total = 0
    for a in range(1, n1 + 1):
        for b in range(1, n2 + 1):
            if a * b >= 30:
                total += a * b
    return total

result = k(i, j)

print("총 합: ", result)

#45
a = [1, 2, 3, 4, 5]

def total_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

result = total_sum(a)
print("누적 합: ", result)