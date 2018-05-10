# Uses python3

def max_pairwise_product(n,a):

        index1 = 0

        for i in range(1, n):
          if a[i] > a[index1]:
            index1 = i
	
        if index1 == 0:
          index2 = 1
        else:
          index2 = 0

        for i in range(0, n):
            if i != index1 and a[i] > a[index2]:
                index2 = i

        return a[index1]*a[index2]


if __name__ == "__main__":

  n = int(input())
  a = [int(x) for x in input().split()]
  assert(len(a) == n)
  
  print(max_pairwise_product(n,a))