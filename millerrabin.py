##Miller-Rabin##
import rand

def  MillerRabin(number,test=20):
	INTMAX = 2147483647
	initset = [2,3,5,7,11,13]
	if number in initset: return True;
	if number<10: return False;
	for x in initset:
		if number%x==0:return False;
	m = number-1
	k = 0
	while m&1 == 0:
		k += 1
		m >>= 1
	for i in range(test):
		a = rand.GetRand(2,min(number-1,INTMAX));
		x = pow(a,m,number)
		y = 0
		for j in range(k):
			y = pow(x,2,number)
			if y==1 and x!=1 and x!=number-1: return False;
			x = y
		if y!=1: return False;
	return True

def IsPrime(number):
	return MillerRabin(number,20)
	