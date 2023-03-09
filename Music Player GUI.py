

import os
import pygame
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title('Music Player')
root.geometry('400x150')


button_frame = tk.Frame(root)
button_frame.pack(pady=20)


def select_music():
    file_path = filedialog.askopenfilename()
    pygame.mixer.music.load(file_path)
    song_label.config(text='Playing: ' + os.path.basename(file_path))
    play_button.config(text='Play')

select_button = tk.Button(button_frame, text='Select Music', command=select_music)
select_button.pack(side='left', padx=10)


def play_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        play_button.config(text='Resume')
    else:
        pygame.mixer.music.unpause()
        play_button.config(text='Pause')

play_button = tk.Button(button_frame, text='Play', command=play_music)
play_button.pack(side='left', padx=10)


song_label = tk.Label(root, text='Select a song to play')
song_label.pack()

root.mainloop()


pygame.mixer.init()


if __name__ == '__main__':
    root.mainloop()

    
    #himanshu 
    #install this first before execute this program
    #pip install pygame
