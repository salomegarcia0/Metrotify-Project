class Playlist:
    def __init__(self, id, name, description, creator, tracks):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracks = tracks
        self.likes = []

    def show_playlist(self):
        print(f'''
        **** PLAYLIST ****
            {self.name}
            {self.description}
            {self.creator}

            Tracks:
            {self.tracks}
            ''')