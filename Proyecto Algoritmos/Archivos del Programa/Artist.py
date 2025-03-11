from User import User

class Artist(User):
    def __init__(self, id, name, email, username, user_type):
        super().__init__(id, name, email, username, user_type)
        self.albums = []
        self.top_songs = []
        self.streams = 0
        self.songs = []
        self.likes = []

    def add_songs(self, track):
        self.songs.append(track)

    def add_like():
        pass
    #Mostrar perfil
    def show(self):
        print(f"""
        **** PERFIL ****
            {self.name}
            {self.username}
            Álbumes de música:
        {', '.join([f"{i+1}. {album}" for i, album in enumerate(self.albums)])}
        
        Top 10 de canciones más escuchadas:
        {', '.join([f"{i+1}. {song}" for i, song in enumerate(self.top_songs)])[:10]}
        
        Cantidad de reproducciones totales: {self.streams}
        """)
