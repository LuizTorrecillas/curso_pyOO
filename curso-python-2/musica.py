class Music:

    musics = []

    def __init__(self, name , artist, duration):
        self.name = name
        self.artist = artist
        self.duration = float(duration)
        Music.musics.append(self)

    def __str__(self):
        return self.name


music1 = Music("Outra vida", "maneva", 2.30)
music2 = Music("Wonderwall","Oasis", 3.14)

print (vars(music1))