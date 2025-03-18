class PlayList:
    def __init__(self, daftar_lagu):
        self.daftar_lagu = daftar_lagu
        self.current_position = 0

    def __switch_to_song(self, to_index):
        last_pos = len(self.daftar_lagu) - 1
        if to_index > last_pos: # geser ke awal
            self.current_position = 0
        elif to_index < 0: # geser ke akhir
            self.current_position = last_pos
        else: # geser ke index yang diminta
            self.current_position = to_index
        lagu = self.daftar_lagu[self.current_position]
        print("Judul lagu {} oleh {}".format(lagu.judul, lagu.penyanyi))

    def play_first_song(self):
        self.__switch_to_song(0)

    def play_last_song(self):
        last_pos = len(self.daftar_lagu) - 1
        self.__switch_to_song(last_pos)

    def play(self):
        self.__switch_to_song(self.current_position)

    def play_next_song(self):
        self.__switch_to_song(self.current_position+1)
    
    def play_prev_song(self):
        self.__switch_to_song(self.current_position-1)

class Lagu:
    def __init__(self, judul, penyanyi):
        self.judul = judul
        self.penyanyi = penyanyi