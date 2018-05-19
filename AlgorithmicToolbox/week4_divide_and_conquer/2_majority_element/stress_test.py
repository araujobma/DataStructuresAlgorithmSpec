import numpy as np
from majority_element_sorted_first import get_majority_element
from majority_element_naive import get_majority_element_naive


def stress_test(N,M,n_rep):

        import random
        random.seed(a=3)
         
        count = 0
        while count <= n_rep :
            count += 1
            if count % 100 == 0:
                print('iteration: ' + str(count))
            
            n = random.randrange(1,N+1)
            A = list(np.random.randint(low=0,high=M+1,size=n))
    
            #for i in range(0,n):
            #    A.append(random.randrange(0,M+1))
            #print(' '.join(str(x) for x in A))
	      
            result1 = get_majority_element_naive(A,n)
            result2 = get_majority_element(A,n)
            if result1 == result2:
                pass
            else:
                print(' '.join(str(x) for x in A))			
                print("Wrong answer: " + str(result1) +' '+ str(result2) )	
                break
				
				
if __name__ == "__main__":

  params = [int(x) for x in input().split()]
    
  stress_test(params[0],params[1],params[2])
  

				
