# Uses python3
def calc_fib(n):
    F = []
    F.append(0)
    F.append(1)
    
    if n <= 1:
        return F[n]
		
    for i in range(2,n+1):
      F.append(F[i-2] + F[i-1])  
    return F[-1]
	
if __name__ == "__main__":
  n = int(input())
  print(calc_fib(n))
