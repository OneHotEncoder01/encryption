import sys
def split(Word): 
	return [char for char in Word] 
Word = input("enter text : ")
l = len(Word)
a = int(l / 2)

for i in range(0,a):
    sys.stdout.write(Word[i])
    sys.stdout.write(Word[(a+i)])
