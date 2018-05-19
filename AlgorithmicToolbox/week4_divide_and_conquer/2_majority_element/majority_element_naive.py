# Uses python3
import sys

def get_majority_element_naive(a,n):
    
    for i in range(0,n):
        curr_elem = a[i]
        count = 0
        for j in range(0,n):
            if a[j] == curr_elem:
                count += 1
            if count > n/2:
                return i+1		
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a,n))