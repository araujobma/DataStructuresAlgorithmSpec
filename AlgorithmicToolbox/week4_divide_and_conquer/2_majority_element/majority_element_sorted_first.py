# Uses python3
import sys

def get_majority_element(a,n):
    sorted_a = sorted(a)
    prev_elem = a[0]
    count = 0
    for i in range(0,n):
        if prev_elem == sorted_a[i]:
            count += 1
        else:
            count = 0
        if count == int(n/2) + 1:
            for j in range(0,n):
                if a[j] == sorted_a[i]:
                    return j+1
    return 0					

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a,n))