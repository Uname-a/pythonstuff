from tkinter import *
import pygame
import time
fields = ('hours', 'mins', 'sec')

def timer(ti):
	
	ch = ""
	if (ch == ""):#default sound
		wtime(ti,"/home/laptop/git/pythonstuff/sounds/bird.ogg")
	else:#sets the sound to what the user whants
		os.chdir("/home/laptop/git/pythonstuff/sounds/")
		wtime(ti,ch)
def wtime(ti,choice):#counts down the time and plays the song at the end
	pygame.mixer.init(0)
	if (ti <= 0):
		pygame.mixer.music.load(choice)
		pygame.mixer.music.play(-1)
		
		return 0
	else:
		time.sleep(1)
		ti = ti -1
		print ("time left in seconds",ti)
		wtime(ti,choice)
def cal(entries):
   # period rate:
   hi = (int(entries['hours'].get()) )
   mi = (int(entries['mins'].get()) )
   si = (int(entries['sec'].get()) )
   
   ti = hi * 3600 + mi * 60 + si
   timer(ti)
   



def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries
def restart():
	print("")
def main():
	if __name__ == '__main__':
	   root = Tk()
	   ents = makeform(root, fields)
	   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
	   #b1 = Button(root, text='restart',
	   #      command=(lambda e=ents: restart(e)))
	   #b1.pack(side=LEFT, padx=5, pady=5)
	   
	   b2 = Button(root, text='start',
	          command=(lambda e=ents: cal(e)))
	   b2.pack(side=LEFT, padx=5, pady=5)
	   b3 = Button(root, text='Quit', command=root.quit)
	   b3.pack(side=LEFT, padx=5, pady=5)
	   root.mainloop()
main()