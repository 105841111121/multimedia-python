from pydub import AudioSegment
import simpleaudio as sa

# Memuat file audio
audio = AudioSegment.from_file('epiken.mp3')

# Mengonversi ke WAV (opsional, jika formatnya bukan WAV)
audio.export('result.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

audio.export('result.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')