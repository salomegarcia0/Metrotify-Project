class Track:
    def __init__(self, id, name, duration, link):
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.likes = []
        self.streams = 0
        self.artist = None

    def set_artist(self, artist):
        self.artist = artist

    def show_track(self):
        print(f'''
        **** CANCIÓN ****
        Id: {self.id}
        Name: {self.name}
        Duration: {self.duration}
        Link: {self.link}''')