

if __name__ == '__main__':
	

	a=input("vnesi enacbo oblike &n(1,2,3,4...) ali Vn(6,5,4,4)"+"\n").strip()

	tip=a[0]
	stsprem=a[1]

	print(tip)

	zaporedje=[]

	zaporedje=a[3:-1].split(",")
	zaporedje = [int(i) for i in zaporedje]

	celozaporedje=[]
	celozaporedje=range(0,2**int(stsprem))

	l3 = [x for x in celozaporedje if x not in zaporedje]
	print(zaporedje)
	print("manjajoci"+str(l3))

	

	if tip=="&":
		print("pretvarjanje iz KNO v DNO")

		dvana=2**int(stsprem)
		lst=[]
		for x in l3:
			lst.append(dvana-1-int(x))
		
		ll=sorted(lst)
		ll = [str(i) for i in ll]
		print("result: "+"V"+str(stsprem)+"("+",".join(ll)+")")


	if tip=="V":
		print("pretvarjanje iz DNO v KNO")
		dvana=2**int(stsprem)
		lst2=[]
		for x in l3:
			lst2.append(dvana-1-int(x))

		ll=sorted(lst2)[::-1]

		ll = [str(i) for i in ll]
		
		print("result: "+"&"+str(stsprem)+"("+",".join(ll)+")")




#V3(0, 4, 5, 6, 7)