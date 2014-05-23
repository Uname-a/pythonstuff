import sys
sys.path.append('/usr/lib/python2.7/site-packages/')
import pygame
import time
import os

def ftime():
	ti = int(input("how long in seconds do you want to wait? "))
	
	return (ti)
def wtime(ti,choice):
	if (ti <= 0):
		pygame.mixer.music.load(choice)
		pygame.mixer.music.play(-1)
		time.sleep(10)
		return 0
	else:
		time.sleep(1)
		ti = ti -1
		wtime(ti,choice)
def find():
	for file in os.listdir("/home/laptop/git/pythonstuff"):
		if file.endswith(".ogg"):
			print (file)
def main():
	find()
	choice = input("which sound you want? enter it exactly and press enter: ")
	pygame.mixer.init(0)
	ti = ftime()
	wtime(ti,choice)
main()