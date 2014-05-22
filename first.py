import time

def poop():# what will display when full
	print("smell")
	time.sleep(1)
	print("fart")
	time.sleep(1)
	print("poop runs out")
	time.sleep(1)
	print("flush toliet")
	time.sleep(1)
	print("WASH HANDS")
	
def filling(belly):# how the belly gets filled
	i = 0

	# while loop example 
	#while (belly < 101):
		#belly = belly + 1
		#i = i + 1
		#eat = 0
		#eat = int(input("enter how much food you ate number 0 -100 "))
		#belly = belly + eat

	#recursion loop example
	if ( belly >= 100):
		return 0
	else:
		
		i = i + 1
		eat = 0
		eat = int(input("enter how much food you ate number 0 -100 "))
		belly = belly + eat
		return filling(belly)


def main():
    filling(0)
    poop()
 
    return 0

 

main()