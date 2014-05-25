from tkinter import *
from tkinter import filedialog
import pygame
import time
import os
fields = ('hours', 'mins', 'sec',)
Ch = ('choice')

def timer(ti,entries):
	
	ch = ""
   
	if (ch == ""):#default sound
		wtime(ti,"/home/laptop/git/pythonstuff/sounds/frog.mp3")
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
   timer(ti,entries)
   



def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=10, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries
def restart(entries):
	pygame.mixer.music.stop()


def choice(entries):
	filename = filedialog.askopenfilename()
	return()


def count():
    
    self.label = tkinter.Label(self, text="", width=10)
    self.label.pack()
    self.remaining = 0
    self.countdown(10)

def countdown(self, remaining = None):
    if remaining is not None:
        self.remaining = remaining

    if self.remaining <= 0:
        self.label.configure(text="time's up!")
    else:
        self.label.configure(text="%d" % self.remaining)
        self.remaining = self.remaining - 1
        self.after(1000, self.countdown)



if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   it()  
   #b3 = Button(root, text='Quit', command=root.quit)
   #b3.pack(side=LEFT, padx=5, pady=5)
   #b4 = Button(root, text='song', command=(lambda e=ents: choice(e)))
   #b4.pack(side=LEFT, padx=5, pady=5)



   b1 = Button(root, text='restart',
         command=(lambda e=ents: restart(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   


   b2 = Button(root, text='start',
          command=(lambda e=ents: cal(e)))
   b2.pack(side=RIGHT, padx=5, pady=5)
   
   root.mainloop()
