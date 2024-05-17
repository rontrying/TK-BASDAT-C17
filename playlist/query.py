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

def select_all_songs():
    return f"""
        SELECT k.id, k.judul, a.nama
        FROM konten k, song s, akun a, artist t
        WHERE k.id = s.id_konten AND
              s.id_artist = t.id AND
              t.email_akun = a.email;
    """

def get_songs(id_playlist):
    return f"""
        SELECT k.judul, a.nama, k.durasi
        FROM playlist_song ps, konten k, akun a, song s, artist t
        WHERE ps.id_playlist = '{id_playlist}' AND
              ps.id_song = s.id_konten AND
              s.id_konten = k.id AND
              s.id_artist = t.id AND
              t.email_akun = a.email;
    """

def count_songs(id_playlist):
    return f"""
        SELECT COUNT(*) FROM playlist_song WHERE id_playlist = '{id_playlist}';
    """



def get_label_profile(email):
    return f"""
            SELECT * FROM label WHERE email = '{email}';
            """

def get_user_profile(email):
    return f"""
            SELECT * FROM akun WHERE email = '{email}';
            """