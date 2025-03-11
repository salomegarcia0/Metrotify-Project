import re
import uuid
from datetime import datetime
from User import User
from Artist import Artist 
from Listener import Listener
from Album import Album
from Playlist import Playlist
from Track import Track
from Like import Like

class Metrotify:
    def __init__(self):
        self.users = []
        self.albums = []
        self.playlists = []
        self.tracks = []

    def administrar(self, users, albums, playlists):
        self.users = users
        self.albums = albums
        self.playlists = playlists

###################### GESTION DE PERFIL #######################
    #validar el formato del correo
    def validar_correo(self):
        correo_valido = False
    
        while not correo_valido:
            correo = input('Ingrese el correo electrónico: ')
            patron_correo = r"^[\w\.\+\-]+\@([\w]+\.)+[\w]+$"
            
            if re.match(patron_correo, correo):
                correo_valido = True
            else:
                print("Correo electrónico inválido, intente nuevamente")

        return correo
        
    #validar strings 
    def validar_str(self, dato):
        while not dato.isalpha():
            x = input('Ingrese un dato valido, recuerde que solo debe contener letras\n--->  ')
            dato = x

        return dato

    #Validar que el username no esté tomado
    def validar_usernamme(self, nuevo_username):
        for user in self.users:
            while user.username == nuevo_username:
                x = input('Username no disponible, por favor escoger uno nuevo\n--->   ') #esta repetido
                nuevo_username = x
            return nuevo_username
        return nuevo_username #no esta repetido
            
    #funcion registro de usuarios desde API
    def registro_users_api(self, usuarios):
        for user in usuarios:
            id = user['id']
            name = user['name']
            email = user['email']
            username = user['username']
            type = user['type']
            if 'musician' in user:
                artist = Artist(id, name, email, username, type)
                self.users.append(artist)
            if 'listener' in user:
                listener = Listener(id, name, email, username, type)
                self.users.append(listener)

    #funcion para registrar un usuario manualmente
    def registro(self):
        id = str(uuid.uuid4())
        name = self.validar_str(input('Ingresa tu nombre:  '))
        email = self.validar_correo()
        username = self.validar_usernamme(input('Ingresa tu username:  '))

        while True:
            user_type = input('Tipo de usuario:\na. Escucha\nb. Artista\n->  ').lower()
            if user_type == 'a':
                user_type = 'listener'
                listener =  Listener(id, name, email, username, user_type)
                self.users.append(listener)
                print(f'Usuario creado con exito!\n {listener.show()}')
                return self.users
            
            elif user_type == 'b':
                user_type = 'musician'
                artist = Artist(id, name, email, username, user_type)
                self.users.append(artist)
                print(f"""Usuario creado con exito!\n {artist.show()}""")
                return self.users
            
            else:
                print('Respuesta incorrecta, por favor elija una de las opciones.')
    
    #buscador
    def busqueda_por_nombre(self, name):
        for user in self.users:
            if user.name == name:
                return user
        
        print(f'{name} no encontrado.')
        return None


    #Borrar Perfil 
    def borrar(self, user_to_delete, name_to_delete):
        if user_to_delete is not None:
            confirmacion = input(f"¿Estás seguro de que deseas eliminar la cuenta de {name_to_delete}? (S/N):\n->   ")
            
            if confirmacion.upper() == 'S':
                self.users.remove(user_to_delete)
                print(f"La cuenta de {name_to_delete} ha sido eliminada.")
            elif confirmacion.upper() == 'N':
                print('Volviendo al menú principal...')
            else:
                print('Opción incorrecta, por favor inténtelo de nuevo.')
        else:
            print("Usuario no encontrado.")

    #Mostrar lista de users
    def show_users(self):
        for idx, user in enumerate(self.users):
            print(f'{idx}. {user}')

    #Editar Perfil #problema con el replace
    def edit(self, name_to_find):
        user_to_change = self.busqueda_por_nombre(name_to_find)

        if user_to_change is not None:
            print("Datos del usuario:")
            print(f"Nombre: {user_to_change.name}")
            print(f"Email: {user_to_change.email}")
            print(f"ID: {user_to_change.id}")
            print(f"Username: {user_to_change.username}")

            while True:
                confirmacion = input(f'¿Estás seguro de que deseas cambiar los datos de la cuenta {user_to_change.name}? (S/N):\n->  ')
                if confirmacion.upper() == 'S':
                    if isinstance(user_to_change, Artist):
                        user_to_change.name = self.validar_str(input('Ingrese el nombre: '))
                        user_to_change.email = self.validar_correo(input('Ingrese el email: '))
                        user_to_change.username = self.validar_username(input('Ingrese el username: '))
                        self.users.remove(user_to_change)
                        self.users.append(user_to_change)
                        return self.users

                    elif isinstance(user_to_change, Listener):
                        user_to_change.name = self.validar_str(input('Ingrese el nombre: '))
                        user_to_change.email = self.validar_correo(input('Ingrese el email: '))
                        user_to_change.username = self.validar_username(input('Ingrese el username: '))
                        self.users.remove(user_to_change)
                        self.users.append(user_to_change)
                        return self.users
                    
                elif confirmacion.upper() == 'N':
                    print('Cancelando acción.')
                    break
                else:
                    print('Opción inválida. Por favor, escoja una opción válida.')
        else:
            print("Usuario no encontrado.")


###################### GESTION MUSICAL #######################
    #Creacion de albums desde api
    def crear_album_api(self, albums):
        for alb in albums:
            id = alb['id']
            name = alb['name']
            description = alb['description']
            cover = alb['cover']
            published = alb['published']
            genre = alb['genre']
            artist = alb['artist']

            #tracklist
            tracklist = []
            for track in alb['tracklist']:
                track_id = track['id']
                track_name = track['name']
                duration = track['duration']
                link = track['link']

                new_track = Track(track_id, track_name, duration, link)

                tracklist.append(new_track)
                self.tracks.append(new_track)
                
                album = Album(id, name, description, cover, published, genre, artist, tracklist)
                self.albums.append(album)

                return self.tracks, self.albums
    
    #crear album manualmente (SOLO ARTISTAS)
    def crear_album(self):
        id = str(uuid.uuid4()) # Genera un ID único en formato UUID
        name = input('Ingrese el nombre del álbum:  ')
        description = input('Ingrese la descripción del álbum:  ')
        cover = input('Ingrese el link de la portada del álbum:  ')
        published = datetime.now().strftime("%Y-%m-%d") #genera la fecha actual
        genre = input('Ingrese el género del álbum:  ')
        artist = input('Ingrese el nombre del artista:  ')
        tracklist = []

        while True:
            selection = input('Desea agregar una canción? (S/N)  ').upper()
            if selection == 'S':
                new_track = self.crear_track()
                tracklist.append(new_track)
                artist = Artist()
                artist.add_songs(new_track)
            elif selection == 'N':
                print('Acción cancelada.')
                break
            else:
                print('Error, por favor ingrese una opción correcta')
   
        new_album = Album(id, name, description, cover, published, genre, artist, tracklist)
        self.albums.append(new_album)
        
        return new_album

    #crear cancion
    def crear_track(self):
        id = str(uuid.uuid4())
        name = input('Ingrese el nombre de la canción:  ')
        duration = input('Ingrese la duración de la cancion:   ')
        link = input('Ingrese el link de la cancion:  ')

        artist = input('Indique el username del autor de la canción:  ')
        for user in self.users:
            if isinstance(user, Artist):
                if artist == user.username:
                    Track.set_artist(artist)
        new_track = Track(id, name, duration, link)
        self.tracks.append(new_track)
        Artist.add_songs(new_track)

    def show_tracks(tracks):
        for idx, track in enumerate(tracks):
            print(f'{idx + 1}. {track}')

    #Creacion de playlists desde api 
    def crear_playlist_api(self, playlists):
        for playlist in playlists:
            id = playlist['id']
            name = playlist['name']
            description = playlist['description']
            creator = playlist['creator']
            tracks = playlist['tracks']
            
            # Crear un objeto Playlist con la lista de IDs de pistas
            new_playlist = Playlist(id, name, description, creator, tracks)
            
            self.playlists.append(new_playlist)
            
            if creator == Listener.id:
                Listener.add_playlist(new_playlist)

        return self.playlists

    #crear playlist manualmente (SOLO ESCUCHAS)
    def crear_playlist(self):
        id = str(uuid.uuid4())
        name = input('Ingrese el nombre de la playlist: ')
        description = input('Ingrese la descripción de la playlist: ')
        creator = input("Ingrese el username del creador: ")

        for user in self.users:
            if creator == user.username:
                creator = user.id
                break
            else:
                print("Usuario no encontrado.")
                return None

        tracks = []

        while True:
            search_tracks = input('Ingrese el nombre de la canción o del artista (o "e" para salir): ').lower()
            if search_tracks == 'e':
                break

            found_tracks = [track for track in self.tracks if search_tracks in track.name.lower() or search_tracks in track.artist.lower()]
            
            if found_tracks:
                print("Canciones encontradas:")
                for i, found_track in enumerate(found_tracks, 1):
                    print(f"{i}. {found_track.name} - {found_track.artist}")
                
                selection = input('Ingrese el número de la canción para agregar a la playlist: ')
                
                try:
                    index = int(selection) - 1
                    selected_track = found_tracks[index]
                    tracks.append(selected_track)
                    print(f'"{selected_track.name}" agregada a la playlist.')
                except (ValueError, IndexError):
                    print("Selección inválida. Intente de nuevo.")
            else:
                print("No se encontraron canciones que coincidan con el término de búsqueda.")

        new_playlist = Playlist(id, name, description, creator, tracks)
        self.playlists.append(new_playlist)

        if creator in [listener.id for listener in self.listeners]:
            for listener in self.listeners:
                if listener.id == creator:
                    Listener.add_playlist(new_playlist)

        return new_playlist


    def buscar(self):
        resultados = []
        while True:
            criterio_busqueda = input('''
                                Escoja el m'etodo de busqueda que desee:
                                1. Nombre del artista
                                2. Nombre del album
                                3. Nombre de la cancion
                                4. Nombre del playlist
                                5. Salir
                                --->   ''')

            if criterio_busqueda == '1':
                nombre = input('Ingrese el nombre del artista:  ')
                for user in self.users:
                    if isinstance(user, Artist):
                        if user.name == nombre:
                            resultados.append(user.name)
                            #like = input('Desea darle like a este artista? (S/N):  ').upper()
                            #if like == 'S':
                                #user = input('Escribe tu username: ')
                            return resultados
                             
            elif criterio_busqueda == '2':
                nombre = input('Ingrese el nombre del album:  ')
                for album in self.albums:
                        if album.name == nombre:
                            resultados.append(album.name)
                            return resultados
                        
            elif criterio_busqueda == '3':
                nombre = input('Ingrese el nombre de la canción:  ')
                for track in self.tracks:
                        if track.name == nombre:
                            resultados.append(track.name)
                            return resultados
                        
            elif criterio_busqueda == '4':
                nombre = input('Ingrese el nombre de la playlist:  ')
                for playlist in self.playlists:
                        if playlist.name == nombre:
                            resultados.append(playlist.name)
                            return resultados
                        
            elif criterio_busqueda == '5':
                break
            else:
                print("Repuesta no válidoa.")
                return resultados

            return resultados
        
    def eescoger_y_ver_detalles(self, resultados):
        if not resultados:
            print("No se encontraron resultados.")
            return

        if len(resultados) == 1:
            result = resultados[0]
            if isinstance(result, Album):
                result.show_album()
            elif isinstance(result, Track):
                result.show_track()
            elif isinstance(result, Playlist):
                result.show_playlist()
        else:
            print("Se encontraron varios resultados:")
            for i, result in enumerate(resultados, 1):
                print(f"{i}. {result.name}")

            selection = int(input("Seleccione el número del resultado para ver detalles: "))
            if 0 < selection <= len(resultados):
                result = resultados[selection - 1]
                if isinstance(result, Album):
                    result.show_album()
                elif isinstance(result, Track):
                    result.show_track()
                elif isinstance(result, Playlist):
                    result.show_playlist()
            else:
                print("Selección inválida.")

    def escuchar(self, song):
        print(f'Se está reproduciendo {song}')


###################### GESTIÓN DE INTERACIÓN #######################

    # Agregar likes a un item:   
    def dar_like(self, user, x):
        encontrado = False
        for like in self.likes:
                if like.usuario == x:
                    self.likes.remove(like)
                    print("Le has quitado el like a la publicación.")
                    encontrado = True
                    break
            
        if not encontrado:
            like = Like(user, x)
            self.likes.append(like)
            print("Le has dado like al item.")


    

    
