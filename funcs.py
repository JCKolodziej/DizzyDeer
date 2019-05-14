import pygame


def init_and_load_song(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)


def play_song(song):
    PLAY_SONG_ONCE = 0
    init_and_load_song(song)
    pygame.mixer.music.play(PLAY_SONG_ONCE)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def stop_song():
    pygame.mixer.music.stop()


def pause_song():
    pygame.mixer.music.pause()


def unpause_song():
    pygame.mixer.music.unpause()


def rewind_song():
    pygame.mixer.music.rewind()


def repeat_song(song):
    PLAY_SONG_INFINITELY = -1
    init_and_load_song(song)
    pygame.mixer.music.play(PLAY_SONG_INFINITELY)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def play_next_song(song):
    stop_song()
    # get from dir the next one. Waiting for playlist


def play_previous_song(song):
    stop_song()
    # get from dir the next one. Waiting for playlist


def volume():
    pass

def get_songs_from_dir(directory):
    import os
    songs = []
    if '.mp3' in directory:
        songs.append(directory)
    else:
        # r=root, d=directories, f = files
        for r, d, f in os.walk(directory):
            for file in f:
                if '.mp3' in file:
                    songs.append(os.path.join(r, file))
    return songs

def play_playlist(songs):
    for i in range(len(songs)):
        play_song(songs[i])
        '''
        if event = next song
            stop song
            i += 1
        elif event = previous song
            stop song
            i -= 1 or 2 -> needs testing
        '''

def shuffle(songs):
    import random
    random.shuffle(songs)
    print(songs)
    return songs


#print(get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/'))
#play_song(get_songs_from_dir('/home/jck//Documents/python/dizzydeer/DizzyDeer/songs')[0])


play_playlist(shuffle(get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/')))

