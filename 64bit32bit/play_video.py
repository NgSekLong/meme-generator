import vlc
# from threading import Thread
from multiprocessing import Process
from time import sleep


def play_video(file):

    process = Process(target=threaded_play_video, args=(file,))
    process.start()
    #process.join()

    # thread = Thread(target = threaded_play_video, args = (file, ))
    # thread.start()
    # thread.join()

def threaded_play_video(file):
    Instance = vlc.Instance('--fullscreen')
    player = Instance.media_player_new()
    Media = Instance.media_new(file)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    sleep(15) # Or however long you expect it to take to open vlc
    