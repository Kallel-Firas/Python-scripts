#modify so that if a number is very big, use log(a*b)=log(a)+log(b)
#DONE :)

def newton_log(x:float,n:float=1.0) -> float:
	try:
		for _ in range(1000):
			n = f(n,x)
		return n
	except:
		return newton_log(x/1000)+a 


f = lambda n,x : n - (e**n-x)/(e**n)
e=2.718281828459045
a:float = newton_log (1000)
for _ in range(1,1000):
	p:float=newton_log( _ )

print('done')