from utils import *

def get_context_data(cursor, query):
    cursor.execute(query)
    return parse(cursor)

def append_unique_items(source, target, key):
    for item in source:
        if item[key] and item[key] not in target:
            target.append(item[key])


def parse_user_dashboard(user_content):
    judul_playlist, lagu_content, podcast_content  = {}, {}, {}

    for item in user_content:
        if item['judul_playlist'] and item["judul_playlist"] is not None:
            judul_playlist[item['id_playlist']] = item['judul_playlist']
        if item['judul'] and item["judul"] is not None:
            if item['tipe'] == 'lagu':
                lagu_content[item['id']] = item['judul']
            elif item['tipe'] == 'podcast':
                podcast_content[item['id']] = item['judul']

    return {
        'playlist_content': list(judul_playlist.values()),
        'song_content': list(lagu_content.values()),
        'podcast_content': list(podcast_content.values())
    }