# Uses python3
import sys

def get_change(m):
    coins = [10,5,1]
    change = []
    for coin in coins:
        while m-coin >= 0:
            m -= coin
            change.append(coin)
    return len(change)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
