MOD = 10**9 + 7

def calculate_power(a, b):
    if b == 0:
        return 1

    tmp = calculate_power(a, b // 2)
    tmp = (tmp * tmp) % MOD

    if b % 2 == 1:
        tmp = (tmp * a) % MOD

    return int(tmp)