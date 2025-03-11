class Album:
    def __init__(self, id, name, description, cover, published, genre, artist, tracklist):
        self.id = id
        self.name = name
        self.description = description 
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist
        self.likes = []

    def show_album(self):
        print(f'''
        **** PLAYLIST ****
            {self.name}
            {self.description}
            {self.cover}
            {self.published}
            {self.genre}
            {self.artist}
            
            Tracklist:
            {self.tracklist}
            ''')