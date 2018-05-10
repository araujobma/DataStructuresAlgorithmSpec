from max_pairwise_product import max_pairwise_product
from max_pairwise_product_naive import max_pairwise_product_naive

def stress_test(N,M):

        import random
        random.seed(a=30)
  
        while True:
    
            
            n = random.randrange(2,N+1)
            A = []
    
            for i in range(0,n):
                A.append(random.randrange(0,M+1))
            print(' '.join(str(x) for x in A))
	      
            result1 = max_pairwise_product_naive(n,A)
            result2 = max_pairwise_product(n,A)
            if result1 == result2:
                print("OK\n")
            else:
                print("Wrong answer: " + str(result1) +' '+ str(result2) )	
                break
				
				
if __name__ == "__main__":

  params = [int(x) for x in input().split()]
    
  stress_test(params[0],params[1])
  

				
