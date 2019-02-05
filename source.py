n=int(raw_input("enter the number where you want to stop"))
for i in range(1,n+1):
	if(i%3==0 and i%5==0):
			print("fuzzbuzz")
	elif(i%3==0):
		print("fuzz")
	elif(i%5==0):
		print("buzz")
	else:
		print(i)


