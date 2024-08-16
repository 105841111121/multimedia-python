from pydub import AudioSegment
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Memuat file audio
audio = AudioSegment.from_file('epiken.mp3')

# Mendapatkan 10 detik pertama
clipped_audio = audio[:10000]
clipped_audio.export('clipped_chapter2_result.mp3', format='mp3')

# Menggabungkan audio asli dan audio yang dipotong
combined_audio = audio + clipped_audio
combined_audio.export('combined_chapter2_result.mp3', format='mp3')

# Meningkatkan volume sebesar 10dB
louder_audio = audio.apply_gain(10)
louder_audio.export('louder_chapter2_result.mp3', format='mp3')

# Mengonversi ke WAV
audio.export('resultChapter2audio.wav', format='wav')

# Membaca file WAV untuk pemutaran
def play_audio(file_path):
    # Membaca file WAV
    rate, data = wav.read(file_path)

    # Memutar audio
    sd.play(data, rate)
    sd.wait()  # Tunggu sampai audio selesai diputar

# Panggil fungsi untuk memutar audio
play_audio('resultChapter2audio.wav')
