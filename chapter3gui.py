import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

# Definisikan fungsi untuk memutar musik
def play_music():
    # Membuat jendela Tkinter yang tidak terlihat
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama Tkinter

    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])

    if file_path:
        try:
            # Load file audio
            audio = AudioSegment.from_file(file_path)

            # Ubah lokasi penyimpanan file sementara ke direktori yang Anda tentukan
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False, dir="C:/Users/ASUS/") as temp_audio_file:
                temp_file_path = temp_audio_file.name
                audio.export(temp_file_path, format="wav")

            # Memutar audio menggunakan Pydub
            play(audio)

            # Menghapus file sementara setelah selesai
            os.remove(temp_file_path)

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Panggil fungsi untuk memutar musik
play_music()
