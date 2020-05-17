#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:04:12 2020

@author: binhnguyen, jcr179
"""


import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

from tkinter import ttk
from ttkthemes import themed_tk as tk
from ttkthemes.themed_tk import ThemedTk

from mutagen.mp3 import MP3
from pygame import mixer

# Changes
import tkinter as tk1
from tkinter import simpledialog
from scipy.io import wavfile
import shutil

# Carlo adds: (For reading data in)
import pickle

# Carlo adds: (Reading data in)
data_directory = os.getcwd()
distances = pickle.load(open(os.path.join(data_directory, 'cosine_distances.pkl'), 'rb'))
summaries = pickle.load(open(os.path.join(data_directory, 'summaries.pkl'), 'rb'))
metadata = pickle.load(open(os.path.join(data_directory, 'metadata.pkl'), 'rb'))

root = tk.ThemedTk()
root.get_themes()                 # Returns a list of all themes that can be set
root.set_theme("radiance")         # Sets an available theme

# Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
# MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
#
# Styles - normal, bold, roman, italic, underline, and overstrike.


# opr - change this for changing title
statusbar = ttk.Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)

playlist = []


# playlist - contains the full path + filename
# playlistbox - contains just the filename
# Fullpath + filename is required to play the music inside play_music load function

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

    mixer.music.queue(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)




def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player build using Python Tkinter by @attreyabhatt')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

mixer.init()  # initializing the mixer

root.title("Melody")
root.iconbitmap(r'images/melody.ico')

# Root Window - StatusBar, LeftFrame, RightFrame
# LeftFrame - The listbox (playlist)
# RightFrame - TopFrame,MiddleFrame and the BottomFrame

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30, pady=30)

playlistbox = Listbox(leftframe)
playlistbox.pack()





addBtn = ttk.Button(leftframe, text="+ Add", command=browse_file)
addBtn.pack(side=LEFT)


def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)




delBtn = ttk.Button(leftframe, text="- Del", command=del_song)
delBtn.pack(side=RIGHT)

####################### OPR #######################

def decr():
    W = Tk()
    W.geometry("450x500")
    S = tk1.Scrollbar(W)
    T = tk1.Text(W, height=4, width=50)
    T.pack(ipady=220, ipadx=30)

    
    # Get Text file
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    play_it = playlist[selected_song]
    target = int(play_it[1+play_it.rindex('/'):play_it.rindex ('.')])
    
    
    #print ('TARGET: ', target)
    """
    # Read Text file
    f = open(target, "r")
    # f  = open ('art_A journey through the mind of an artist Dustin Yellin.mp3.txt', 'r')
    text = f.read()
    f.close()
    """
    title, author = metadata[target]
    text = title + ' by ' + author + ' (' + str(target) + ')\n\n' + summaries[target]
    
    # art_A journey through the mind of an artist Dustin Yellin.mp3.txt
    T.insert(tk1.END, text)
    mainloop()
    
    

descBtn = ttk.Button(leftframe, text="Generate Summary", command=decr)
descBtn.pack(side= BOTTOM)

## CARLO
# Create a function in sim to show the similarities of the functions
# I created a gui for you already
# Search of functions related to tk gui 

# Carlo adds: knn function 
def knn(query_id, k, distances):
    d = sorted(distances[query_id])
    closest = []
    for dist in d:
        closest.append(distances[query_id].index(dist))
    return closest[1:k+1]

def sim (query_id):
    # to do : figure out how to pass argument to it 
    # to do : figure out how to get currently selected playlist 
    
    W = Tk()
    W.geometry("450x500")
    
    # Carlo modifies: return k=2 most similar 
    S = tk1.Scrollbar(W)
    T = tk1.Text(W, height=4, width=50)
    T.pack(ipady=220, ipadx=30)
    
    closest = knn(query_id, 2, distances)
    
    textToShow = ""
    for i in range(len(closest)):
        title, author = metadata[closest[i]]
        
        textToShow += title + ' by ' + author + ' (' + str(closest[i]) + ')'
        
        if i < len(closest) - 1:
            textToShow += '\n\n'
    
    text = (textToShow)
    
    T.insert(tk1.END, text)
    
    mainloop()
    
def get_target():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    play_it = playlist[selected_song]
    target = int(play_it[1+play_it.rindex('/'):play_it.rindex ('.')])
    
    sim(target)
    

    
simBtn = ttk.Button(leftframe, text="Similar Podcasts", command=get_target)
simBtn.pack(side= BOTTOM)

####################### OPR #######################


rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()

lengthlabel = ttk.Label(topframe, text='Total Length : --:--')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text='Current Time : --:--', relief=GROOVE)
currenttimelabel.pack()




def show_details(play_song):
    file_data = os.path.splitext(play_song)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


global current_time
def start_count(t):
    global paused,current_time
    # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
    # Continue - Ignores all of the statements below it. We check if music is paused or not.
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
            time.sleep(1)
            current_time += 1
            
        print (current_time)




####################### OPR #######################



def snip(target):    
    global start, end, filename_path
    print (target)
    fs, data = wavfile.read(target) # change
    snipped = data [start*fs:end*fs]
    wavfile.write(target,fs,snipped) #change 
    filename_path = target
    add_to_playlist(filename_path)
    

def save_file (f):
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    play_it = playlist[selected_song]
    
    
    
    target = (play_it[0:play_it.rindex ('/')+1] + f + '.wav')
    original = (play_it)    
    shutil.copyfile(original, target) # make a copy of the file 
    snip(target) # snip the new file saved
    
    
def save_snippet():
    WINDOW = tk1.Tk()
    WINDOW.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Save Snippet", prompt='Enter Filename')
    WINDOW.destroy() 
    return USER_INP


global start, end, record 
record = False

def record_music ():
    global record,start,end
    print ("Record Toggle")


    record = not record
    if record:
        statusbar['text'] = "Start Record Toggle"
        start =  current_time
    else:
        statusbar['text'] = "End Record Toggle"
        end = current_time
        pause_music() # pause music
        f = save_snippet() # get user to input filename
        save_file (f) # save file under new name
        print ('You typed in this: ', f)        

####################### OPR #######################




def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(play_it)
            show_details(play_it)
        except:
            tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewinded"


def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


muted = FALSE


def mute_music():
    global muted
    if muted:  # Unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE




##### MAIN FUNCTION #####

middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)

playPhoto = PhotoImage(file='images/play.png')
# playPhoto= playPhoto.zoom(25)
# playPhoto = playPhoto.subsample(32)
playBtn = ttk.Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=5)


stopPhoto = PhotoImage(file='images/stop.png')
stopBtn = ttk.Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=1, padx=5)

pausePhoto = PhotoImage(file='images/pause.png')
pauseBtn = ttk.Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=5)

recordPhoto = PhotoImage(file='images/record.png')
recordBtn = ttk.Button(middleframe, image=recordPhoto, command=record_music)
recordBtn.grid(row=0, column=3, padx=5)


# Bottom Frame for volume, rewind, mute etc.

bottomframe = Frame(rightframe)
bottomframe.pack()

rewindPhoto = PhotoImage(file='images/rewind.png')
rewindBtn = ttk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0, column=0)

mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volumeBtn = ttk.Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0, column=1)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)  # implement the default value of scale when music player starts
mixer.music.set_volume(0.7)
scale.grid(row=0, column=2, pady=15, padx=30)

# OPR - Initially start with some files in the library
filename_path = os.getcwd()+'/art_A journey through the mind of an artist Dustin Yellin.wav'
add_to_playlist(filename_path)


def on_closing():
    stop_music()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()