import requests
from Metrotify import Metrotify
from Listener import Listener
from Artist import Artist
import pickle

def cargar_datos_api(url):
    'Carga directa de la API desde la URL'
    api = requests.get(url)
    return api.json()

rutaUsers = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json'
rutaAlbums = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json'
rutaPlaylists = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json'


def main():
    """PROGRAMA PRINCIPAL
    """
    # Se trata de cargar la base de datos de cada clase.
    # En caso de no existir, el programa se ejecutará y al finalizar el mismo se crearan y guardaran directamente en un .txt.

    metrotify = Metrotify()
    
    try:
        # Cargar Usuarios
        try:
            print("Intentando cargar usuarios desde 'users.txt'...")
            users = pickle.load(open("users.txt", "rb"))
            print("Usuarios cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo 'users.txt' no encontrado. Cargando desde la API...")
            users = cargar_datos_api(rutaUsers)
            
        
        #Cargar Albums
        
        try:
            print("Intentando cargar álbumes desde 'albums.txt'...")
            albums = pickle.load(open("albums.txt", "rb"))
            print("Álbumes cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo 'albums.txt' no encontrado. Cargando desde la API...")
            albums = cargar_datos_api(rutaAlbums)
            

        #Cargar Playlists

        try:
            print("Intentando cargar playlists desde 'playlist.txt'...")
            playlists = pickle.load(open("playlist.txt", "rb"))
            print("Playlists cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo 'playlist.txt' no encontrado. Cargando desde la API...")
            playlists = cargar_datos_api(rutaPlaylists)
            

    except Exception as e:
        print("Ocurrió un error:", e)


    while True:
        #MENU DEL PROGRAMA
        bienvenida = 'BIENVENIDO A METROTIFY'
        print(f'\033[1;37m|-----------------------------------------------------------|\n{bienvenida.center(60, " ")}\n|-----------------------------------------------------------|')

        menu = 'MENÚ'
        print(f'{menu.center(60, " ")}\n-------------------------------------------------------------')
        option = input('''
            1. Gestión de Perfil
            2. Música
            3. Estadísticas
            4. Salir
            --->  ''')

        if option == '1': #Perfil
            while True:
                b_gestion_p = 'BIENVENIDO A GESTIÓN PERFIL'
                print(f'-----------------------------------------------------------\n{b_gestion_p.center(60, " ")}\n-------------------------------------------------------------')
                op = input('''
            Qué acción desea realizar?
            1. Registrar nuevo usuario
            2. Buscar perfil
            3. Cambiar información de la cuenta
            4. Borrar cuenta 
            5. Salir de gestión de perfil
            --->   ''')
                
                if op == '1': #Registrar
                    b_resgitro = 'REGISTRO DE USUARIO'
                    print(f'-----------------------------------------------------------\n{b_resgitro.center(60, " ")}\n-------------------------------------------------------------')
                    metrotify.registro()
                    while True:
                        x = input('''
            ¿Desea crear otro perfil? (S/N)
            --->  ''').upper()
                        if x == 'S':
                            metrotify.registro()
                            metrotify.show_users()
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión de Perfil''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones aceptadas.''')
                        
                elif op == '2': #buscar **********
                    while True:
                        b_buscador_n = 'BUSCADOR'
                        print(print(f'-----------------------------------------------------------\n{b_buscador_n.center(60, " ")}\n-------------------------------------------------------------'))
                        name = input('''Ingrese el nombre del usuario que desea buscar:''')
                        metrotify.busqueda_por_nombre(name)
                        x = input('''¿Desea ver el perfil? (S/N)\n--->  ''').upper()
                        if x == 'S':
                            for user in metrotify.users:
                                if isinstance(user, Listener):
                                    Listener.show()
                                    break
                                elif isinstance(user, Artist):
                                    Artist.show()
                                    break
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión de Perfil''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones acceptadas.''')

                elif op == '3': #editar
                    b_editar = 'EDITAR PERFIL'
                    print(print(f'-----------------------------------------------------------\n{b_editar.center(60, " ")}\n-------------------------------------------------------------'))
                    name_to_find = input('''
            Ingrese el nombre del usuario que desea buscar:  ''')
                    metrotify.edit(name_to_find)
                    while True:
                        x = input('''
            ¿Desea cambiar la información de otro perfil? (S/N)\n--->  ''').upper()
                        if x == 'S':
                            name_to_find = input('''
            Ingrese el nombre del usuario que desea buscar:  ''')
                            metrotify.edit(name_to_find)
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión de Perfil''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones acceptadas.''')
    
                elif op == '4': #borrar
                    b_borrar = 'BORRAR PERFIL'
                    print(f'-----------------------------------------------------------\n{b_borrar.center(60, " ")}\n-------------------------------------------------------------')
                    name_to_delete = input('''
            Ingresa el nombre del usuario que deseas eliminar:\n->  ''')
                    user_to_delete = metrotify.busqueda_por_nombre(name_to_delete)
                    metrotify.borrar(user_to_delete, name_to_delete)
                    while True:
                        x == input('''
            ¿Desea borrar otro perfil? (S/N)\n--->  ''').upper()
                        if x == 'S':
                            name_to_delete = input('''
            Ingresa el nombre del usuario que deseas eliminar:\n->  ''')
                            user_to_delete = metrotify.busqueda_por_nombre(name_to_delete)
                            metrotify.borrar(user_to_delete, name_to_delete)
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión de Perfil''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones aceptadas.''')

                elif op == '5': #salir
                    print('''
            Volviendo al menú principal''')
                    break
                else: #error
                    print('''
            Error, opción inválida. Por favor escoja una de las opciones acceptadas.''')

        elif option == '2': #Musica
            while True:
                b_gestion_m = 'BIENVENIDO A GESTIÓN MÚSICAL'
                print(f'-----------------------------------------------------------\n{b_gestion_m.center(60, " ")}\n-------------------------------------------------------------')
                op = input('''
            Qué acción desea realizar?
            1. Crear Albúm (SOLO ARTISTAS)
            2. Crear Playlist (SOLO ESCUCHAS)
            3. Buscador
            4. Escuchar Música 
            5. Salir de gestión de música
            --->   ''')

                if op == '1': #crear Album
                    b_crear_a = 'CREAR ALBUM'
                    print(f'-----------------------------------------------------------\n{b_crear_a.center(60, " ")}\n-------------------------------------------------------------')
                    metrotify.crear_album()
                    while True:
                        x = input('''
            ¿Desea crear otro album? (S/N)
            --->  ''').upper()
                        if x == 'S':
                            metrotify.crear_album()
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión músical''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones aceptadas.''')

                elif op == '2': #crear Playlist
                    b_crear_p = 'CREAR PLAYLIST'
                    print(f'-----------------------------------------------------------\n{b_crear_p.center(60, " ")}\n-------------------------------------------------------------')
                    metrotify.crear_playlist()
                    while True:
                        x = input('''
            ¿Desea crear otra playlist? (S/N)
            --->  ''').upper()
                        if x == 'S':
                            metrotify.crear_playlist()
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión músical''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones aceptadas.''')
                elif op == '3': #BUSCADOR
                    b_crear_b = 'BUSCADOR'
                    print(f'-----------------------------------------------------------\n{b_crear_b.center(60, " ")}\n-------------------------------------------------------------')
                    
                    metrotify.buscar()
                    while True:
                        x = input('''
                ¿Desea realizar otra busqueda? (S/N)
                --->  ''').upper()
                        if x == 'S':
                            metrotify.buscar()
                        elif x == 'N':
                            print('''
            Volviendo al menú de Gestión musical''')
                            break
                        else:
                            print('''
            Error, opción inválida. Por favor escoja una de las opciones aceptadas.''')
                elif op == '4': #Escuchar
                    metrotify.escuchar()
                elif op == '5': #salir
                    print('''
            Volviendo al menú principal''')
                    break
                    
                else: #error
                    print('''
                Error, opción inválida. Por favor escoja una de las opciones acceptadas.''')



        elif option == '3': #estadisticas
            pass
        elif option == '4':
            # Al cerrar el programa se cargaran los datos de las bases de datos de cada clase, a su respectivo .txt.
            pickle.dump(users,open("users.txt","wb"))
            pickle.dump(albums,open("albums.txt","wb"))
            pickle.dump(playlists,open("playlists.txt","wb"))
            print('Gracias por usar Metrotify!')
            break
        else:
                print('Error, opción inválida. Por favor escoja una de las opciones acceptadas.')

    


    metrotify = Metrotify()
    metrotify.administrar(users, albums, playlists)
if __name__ == "__main__":
    main()
    

        