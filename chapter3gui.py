import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import threading

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection

def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.flac")])
    if file_path:
        audio = AudioSegment.from_file(file_path)
        threading.Thread(target=play, args=(audio,)).start()

root = tk.Tk()
root.title("Multimedia Application")

# Initial image setup
image = Image.open('sasuke.jpg')
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()

# Buttons
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

play_button = tk.Button(root, text="Play Music", command=play_music)
play_button.pack()

root.mainloop()
