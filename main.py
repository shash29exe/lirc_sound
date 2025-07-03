import subprocess
import pygame
import sys

pygame.mixer.init()
sound = pygame.mixer.Sound("./audio.mp3")

command = ["sudo", "mode2", "-d", "/dev/lirc0", "-m"]

process = subprocess.Popen(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print("ожидание")

try:
    while True:
        output = process.stdout.readline()
        if output:
            print("получено", output.strip())
            sound.play()
        if process.poll() is not None:
            break
except KeyboardInterrupt:
    process.terminate()
    sys.exit(0)



