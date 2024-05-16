def select_playlist(id):
    return f"""
        SELECT * FROM playlist WHERE id = '{id}';
    """

def select_user_playlist_by_id(id):
    return f"""
        SELECT * from user_playlist where id_user_playlist = '{id}';
    """

def select_user_playlist(email):
    return f"""
        SELECT * FROM user_playlist WHERE email_pembuat = '{email}';
    """

def get_songs(id_playlist):
    return f"""
        SELECT id_song FROM playlist_song WHERE id_playlist = '{id_playlist}';
    """

def count_songs(id_playlist):
    return f"""
        SELECT COUNT(*) FROM playlist_song WHERE id_playlist = '{id_playlist}';
    """