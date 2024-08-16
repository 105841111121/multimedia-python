from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

# Muat video
video = VideoFileClip('cing.mp4').without_audio()

# Buat video pendek dari subclip
short_video = video.subclip(0, 10)
short_video.write_videofile('short_cing_result.mp4', audio=False)

# Gabungkan video asli dengan video pendek
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_cing_result.mp4', audio=False)

# Buat video yang dibalik
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('reversed_cing_result.mp4', audio=False)

# Buat video dengan kecepatan dipercepat
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('SpeedUp_cing_result.mp4', audio=False)

# Tulis video asli kembali tanpa audio
video.write_videofile('resultCING.mp4', audio=False)
