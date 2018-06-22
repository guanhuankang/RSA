#coding=UTF-8

#Encrypt Block Size ----- EnBS <= len(str(n))-1
#The max length of Unicode ---- UniSize = 10(10)
#Every Block Encrypt Amount ---- EBEA = EnBS/UniSize
#Msg list ---- Mlist
#Standardization Msg list ---- SMlist
#Msg Block list ---- MBlist
#Ciphertext Blocks List---- CBlist
#Standardization Ciphertext Blocks List---- SCBlist
# Standardization Ciphertext Blocks Link---- SCB
#Length of Mstring ----- MSize
#Msg list Amount ----- MBSize
#Ciphertext Blocks Amount ----- CBSize
#Ciphertext Blocks Size ----- CBS

def Encrypt(dist,Mstring,charaterset="UTF-8"):
	#dist {n,e},initial
	n = dist["n"]
	e = dist["e"]
	UniSize = 10
	EBEA = (len(str(n))-1)/UniSize
	EnBS = EBEA*UniSize
	CBS = len(str(n))+7
	#Standardization
	Mstring = Mstring.decode(charaterset)
	Mlist = [str(ord(x)) for x in Mstring]
	SMlist = []
	for x in Mlist:
		t = UniSize - len(x)
		SMlist.append("0"*t+x)
	#Get MB
	MSize = len(SMlist)
	MBlist = []
	MBSize = (MSize+EBEA-1)/EBEA
	for i in range(MBSize):
		MBlist.append("".join(SMlist[i*EBEA:i*EBEA+EBEA]))
	#Encrypt
	CBlist = [str(pow(int(x),e,n)) for x in MBlist]
	#Standardization
	SCBlist = []
	SCB = ""
	for x in CBlist:
		t = CBS - len(x)
		#SCBlist.append("0"*t+x)
		SCB += "0"*t+x
	return SCB.encode("UTF-8")

def Decrypt(dist,SCB,charaterset="UTF-8"):
	#dist {n,e},initial
	n = dist["n"]
	d = dist["d"]
	UniSize = 10
	EBEA = (len(str(n))-1)/UniSize
	EnBS = EBEA*UniSize
	CBS = len(str(n))+7
	#Standardization
	CBSize = len(SCB)/CBS
	CBlist = []
	for i in range(CBSize):
		CBlist.append(int(SCB[i*CBS:i*CBS+CBS]))
	#Decrypt
	MBlist = [str(pow(x,d,n)) for x in CBlist]
	#Standardization
	SMBlist = []
	SMB = ""
	for x in MBlist:
		t = UniSize - len(x)%UniSize
		#SMBlist.append("0"*t+x)
		SMB += "0"*t+x
	#Dismantling
	MSize = len(SMB)/UniSize
	Mlist = []
	for i in range(MSize):
		Mlist.append(int(SMB[i*UniSize:i*UniSize+UniSize]))
	Mstring = [unichr(x) for x in Mlist]
	return ("".join(Mstring)).encode(charaterset)

#Test
def Demo():
	dist = {'e': 65537, 'd': 5660065639680531241932746640740477279806432482500491259925276210797498675433823468815802313645636767544318329017652866307220023015977572861386047343102011630467132545169051337128011514274331611501907084525742210478247072378493439359466350414106232581960528756110505908812356667458071222329259436810856867779857L, 'n': 6925630996951942196795175904001207212088537659969655079287594089487419403892878935714068748331698378195925959724984893843958825421446989276090016704782893248262352771521319170290115925459384185115744542924745086696303840811223227650558458546036006257442412635412719739738245386757396644917847810748040492783353L}
	C = Encrypt(dist,"世界杯 World Cup  Кубок мира  Το Παγκόσμιο Κύπελλο"*100)
	print(C)
	M = Decrypt(dist,C)
	print(M)