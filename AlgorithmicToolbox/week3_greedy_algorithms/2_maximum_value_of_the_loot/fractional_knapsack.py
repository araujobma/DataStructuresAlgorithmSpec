# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    ordered_values_weights = []
    j = 0
    for i in weights:
        ordered_values_weights.append({'weight': weights[j],'value': values[j]})
        j += 1
    ordered_values_weights.sort(key=lambda x: x['value']/x['weight'], reverse=True)
        
    for x in ordered_values_weights:
        if not (capacity > 0):
            return value		
		
        if x['weight'] <= capacity:
            value += x['value']
            capacity -= x['weight']
        else:
            fraction = float(capacity)/float(x['weight'])
            value += fraction * x['value']
            capacity -= fraction * x['weight']
	
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
