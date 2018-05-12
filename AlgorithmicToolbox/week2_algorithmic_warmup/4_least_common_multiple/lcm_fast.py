# Uses python3
import sys

def gcd_fast(a, b):
    if b == 0:
        return a

    return gcd_fast(b, a % b)


def lcm_fast(a, b):
    if b % a == 0:
        return b

    return (a * b) // gcd_fast(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    if b >= a:
        print(lcm_fast(a, b))
    else:
        print(lcm_fast(b, a))