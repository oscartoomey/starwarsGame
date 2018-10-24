from sound import play_music
import time
              #to stop the music 
#stop_music()

              #to play music asynchronously
#play_music("filename")


def intro():
    play_music('titlemusic.wav')
    for _ in range(100):
        print("")
    time.sleep(1)
    string = "  STAR WARS "
    print(string.center(70, '*'))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "THERE HAVE BEEN REPORTS THAT PRINCESS LEIA"
    print(string.center(70))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "HAS BEEN CAPTURED BY THE GALACTIC EMPIRE"
    print(string.center(70))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "IT IS UP TO YOU TO SAVE HER"
    print(string.center(70))
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    string = "PICK A CHARACTER, BUT BE WARNED, A DARK PATH LIES AHEAD."
    print(string.center(70))
    time.sleep(0.5)
    print()
    for _ in range(36):
        time.sleep(0.5)
        print("")

def canteena():
    play_music('canteena.wav')

def ending():
    play_music('victorymusic.wav')

def stopmusic():
    play_music(None)
