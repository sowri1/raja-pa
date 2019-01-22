import random
small="abcdefghijklmnopqrstuvwxyz"
cpt="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
no="1234567890"
chr="~`!@#$%^&*()_\|.,<>/?;:'"
def genpasswd():
	passwd=""
	n=int(input("How many characters does your password possess "))
	a=input("Would you like to add capital letters to your password(y/n): ")
	b=input("Would you like to add numbers to your password(y/n): ")
	c=input("Would you like to add special characters to your password(y/n): ")
	reqpass=small
	if a=="y":
		reqpass+=cpt
	if b=="y":
		reqpass+=no
	if c=="y":
		reqpass+=chr
	for i in range(n):
		passwd+=reqpass[random.randint(0,len(reqpass)-1)]
	print("The generated password is:",passwd)
	return passwd
if __name__=="__main__":
	genpasswd()