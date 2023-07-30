import platform

if platform.system() == "Windows":
    import winsound
else:
    import playsound


AUDIO = "./assets/cell_phone.wav"


def play(filename):
    # sudo apt install mpg321
    #  mpg321 -w cell_phone.wav cell_phone.mp3

    if platform.system() == "Windows":
        winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        playsound.playsound(filename, False)


def stop():
    if platform.system() == "Windows":
        winsound.PlaySound(None, winsound.SND_PURGE)
