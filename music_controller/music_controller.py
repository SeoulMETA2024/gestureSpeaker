class MusicControll:

    def __init__(self, file_name) -> None:
        import pygame

        self.file_list = file_name

        pygame.mixer.init()

        self.music_init(self.file_list[0])

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

        song = self.file_list.pop(0)
        self.music_init(self.file_list[0])

        self.file_list.append(song)

        return

    def previous_song(self):
        #이전 곡 재생

        Elen = len(self.file_list)

        PreviousSong = self.file_list.pop(Elen - 1)
        self.file_list.insert(0, PreviousSong)

        self.music_init(self.file_list[0])

        return
