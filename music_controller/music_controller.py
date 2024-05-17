class MusicControll:

    def __init__(self, file_name) -> None:
        import pygame

        file_list = [file_name[1], file_name[2], file_name[3]]

        pygame.mixer.init()

        self.music_init()

        pass

    def music_init(self, music_file):
        #기본 음악 불러오기

        pygame.mixer.music.load(music_file)

        pygame.mixer.music.play()
        pygame.mixer.music.pause()

    def music_stop(self):
        #음악 정지

        pygame.mixer.music.pause()

        return

    def music_start(self):
        #음악 시작

        pygame.mixer.music.play()

        return

    def next_song(self):

        #다음 곡 재생

        return

    def previous_song(self):

        #이전 곡 재생

        return
