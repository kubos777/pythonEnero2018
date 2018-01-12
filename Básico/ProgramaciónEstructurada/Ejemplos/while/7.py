n = 0
print("HATSA EL 100")
while(1):
	n += 1
	entrada = input()

	if entrada == "salir":
		break
	if n%7 == 0:
		print("clap")
	elif (n-7)%10 == 0:
		print("clap")
	else:
		print(n)