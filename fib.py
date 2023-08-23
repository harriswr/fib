#!/home/harriswr/codes/anaconda3/bin/python

cache = {0:0, 1:1}

def fib(n):
	if n in cache:
		return cache[n]
	res = fib(n-1) + fib(n-2)
	cache[n] = res
	return res

if __name__ == "__main__":
	print("The 20th Fibonacci number is: ", fib(20))
