import pygame
from PIL import Image
import cv2
import moviepy
import numpy
import soundfile

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", Image.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    
    try:
        print("✅ MoviePy version:", moviepy.__version__)
    except AttributeError:
        print("✅ MoviePy version:", moviepy.__version__)

    print("✅ NumPy version:", numpy.__version__)
    print("✅ SoundFile version:", soundfile.__version__)

if __name__ == "__main__":
    check_installation()
