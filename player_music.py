import tkinter as tk
import os
import fnmatch

from pygame import mixer

canvas=tk.Tk()
canvas.title("Farrugia Player")
canvas.geometry("500x500")
canvas.config(bg="white")

rootpath="./chansons/"
pattern = "*.mp3"

#Initialisation du mixer----------------------------
mixer.init()

#Initialisation des boutons
prec_img=tk.PhotoImage(file="./images/prev.png")
stop_img=tk.PhotoImage(file="./images/stop.png")
play_img=tk.PhotoImage(file="./images/play.png")
pause_img=tk.PhotoImage(file="./images/pause.png")
suiv_img=tk.PhotoImage(file="./images/next.png")


#----------------------------LES FONCTIONS-----------------------------
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath +""+listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear("active")

def suiv():
    next_song =listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)

    label.config(text=next_song_name)

    mixer.music.load(rootpath +"\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,"end")
    listBox.activate(next_song)
    listBox.select_set(next_song)

def prec():
    prec_song =listBox.curselection()
    prec_song=prec_song[0]+1
    prec_song_name=listBox.get(prec_song)

    label.config(text=prec_song_name)

    mixer.music.load(rootpath +"\\" + prec_song_name)
    mixer.music.play()

    listBox.select_clear(0,"end")
    listBox.activate(prec_song)
    listBox.select_set(next)

def pause():
    if pauseButton["text"]=="pause":
        mixer.music.pause()
        pauseButton["text"]="play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="pause"


listBox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=("poppin",14))
listBox.pack(padx=15,pady=15)

#------------------------------LABEL------------------------------------
label = tk.Label(canvas,text="",bg="white",fg="black",font={"poppin",18})
label.pack(pady=15)

top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')

#-------------------------------LES BOUTONS------------------------------

#BOUTON PRECEDENT
precButton = tk.Button(canvas, text ="prev",image=prec_img,bg="white",borderwidth=0,command=prec)
precButton.pack(pady=15,in_=top,side="left")

#BOUTON STOP
stopButton = tk.Button(canvas, text ="stop",image=stop_img,bg="white",borderwidth=0,command=stop)
stopButton.pack(pady=15,in_=top,side="left")

#BOUTON PLAY
playButton = tk.Button(canvas, text ="play",image=play_img,bg="white",borderwidth=0,command=select)
playButton.pack(pady=15,in_=top,side="left")

#BOUTON PAUSE
pauseButton = tk.Button(canvas, text ="pause",image=pause_img,bg="white",borderwidth=0,command=pause)
pauseButton.pack(pady=15,in_=top,side="left")

#BOUTON SUIVANT
suivButton = tk.Button(canvas, text ="suiv",image=suiv_img,bg="white",borderwidth=0,command=suiv)
suivButton.pack(pady=15,in_=top,side="left")

#------------------------------------------------------------------------

#Boucle for -------------------------------------------------------
for root, dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):

        listBox.insert('end',filename)



canvas.mainloop()