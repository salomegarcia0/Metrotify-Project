from User import User

class Listener(User):
    def __init__(self, id, name, email, username, user_type):
        super().__init__(id, name, email, username, user_type)
        self.liked_albums = []
        self.liked_songs = []
        self.playlist_listener = []

    def add_playlist(self, playlist):
        self.playlist_listener.append(playlist)

    def add_liked_albums(self, album):
        self.liked_albums.append(album)

    def add_liked_songs(self, songs):
        self.liked_songs.append(songs)

    #Mostrar perfil
    def show(self):
        print(f"""
        **** PERFIL ****
            {self.name}
            {self.username}
            Álbumes gustados:
        {', '.join([f"{i+1}. {album}" for i, album in enumerate(self.liked_albums)])}
        
        Canciones Gustadas:
        {', '.join([f"{i+1}. {song}" for i, song in enumerate(self.liked_songs)])}

        Playlists:
        {', '.join([f"{i+1}. {playlist}" for i, playlist in enumerate(self.playlist_listener)])}
        """)

