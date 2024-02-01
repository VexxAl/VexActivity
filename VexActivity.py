from VexActivityConect import sp
from VexActivityFunc import msg_activity

# Obtengo los dispositivos en los que se esta ejecutando Spotify y compruebo que haya activos
devices = sp.devices()

if devices['devices']:
    active_device = False
    is_playing = False

    # Encuentro el primer dispositivo activo y guardo su estado
    for device in devices['devices']:
        if device['is_active'] == True:
            active_device = device['is_active']
            break
    
    # Obtengo los datos de la reproduccion de mi usuario
    current_track = sp.currently_playing()

    # Compruebo que no este la reproducción pausada y guardo el estado de reproducción
    if active_device == True:
        is_playing = current_track['is_playing']

    if current_track is not None and is_playing != False:

        # Inicializo y guardo los valores que me interesan, como nombre del track, artista y nombre de la playlist
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        if current_track['context']['type'] == 'playlist':
            playlist_href = current_track['context']['href']
            playlist_id = playlist_href[playlist_href.rfind('/') + 1:]
        
        msg_activity(track_name, artist_name, playlist_id)

    else:
        print("\nValen probablemente está durmiendo en este momento -_-")

else:
    print("\nNadie está reproduciendo nada :o")

