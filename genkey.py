#coding=UTF-8
import rand
import millerrabin

def KGCD(a,b,d,x,y):
	if b==0:
		d = a;
		x = 1;
		y = 0;
		return (d,x,y)
	else:
		p = KGCD(b,a%b,d,y,x)
		d = p[0]
		y = p[1]
		x = p[2]
		y -= x*(a/b)
		return (d,x,y)

def GetPQ(detect):
	while True:
		if(millerrabin.MillerRabin(detect)):return detect;
		detect+=1

def GetD(e,n,fn):
	e = e%fn
	d=0
	x=0
	y=0
	rs = KGCD(e,fn,d,x,y)
	d = rs[1]
	dlimit = (n>>2)+3
	while d<dlimit:
		d += fn
		fn <<= 1
	return d


#parameter length, I recommand the key length >= 1024.
#The key storage space is at least more than length+2a+3
#result <n,e,d>
def GenerateKey(length=1024):
	a = 2
	length += 2*a+1
	p = GetPQ(rand.GetRand((1<<length/2-a),1<<length/2+a))
	q = GetPQ(rand.GetRand((1<<length/2-a),1<<length/2+a))
	n = p*q
	fn = (p-1)*(q-1)
	e = (1<<16)+1
	d = GetD(e,n,fn)
	return {"n":n,"e":e,"d":d}

def GenerateKeyDebug(length=1024):
	a = 2
	length += 2*a+1
	p = GetPQ(rand.GetRand((1<<length/2-a),1<<length/2+a))
	q = GetPQ(rand.GetRand((1<<length/2-a),1<<length/2+a))
	n = p*q
	fn = (p-1)*(q-1)
	e = (1<<16)+1
	d = GetD(e,n,fn)
	return {"n":n,"e":e,"d":d,"fn":fn,"p":p,"q":q}

#p = GenerateKey()
#print(p)