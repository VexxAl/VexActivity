# Según lo que mi usuario este escuchando muestro en pantalla un mensaje gracioso
def msg_activity(track_name, artist_name, playlist_id):
        if artist_name == "Taylor Swift":
            print(f"\nAlfonsina está reproduciendo '{track_name}' con la cuenta del bastardo :/")
        elif artist_name == "Tan Bionica" or artist_name == "Chano":
            print(f"\nValen está feliz, está escuchando '{track_name}' de Chanito :)")
        elif artist_name == "Mac Miller":
            print(f"\nValen está de chill escuchando '{track_name}' de Mac Miller -.-")
        elif playlist_id == '5vYatZ359LmD6DxhFoXgwr':
            print(f"\nValentín está en modo gaucho escuchando '{track_name}' de {artist_name} ¬.¬")
        else:
            print(f"\nValen se está haciendo el lindo mientras escucha '{track_name}' de {artist_name}, re ¿?")