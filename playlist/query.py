

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

def insert_user_playlist(email_pembuat, id_user_playlist, judul, deskripsi, jumlah_lagu, tanggal_dibuat, id_playlist, total_durasi):
    return f"""
        INSERT INTO USER_PLAYLIST (email_pembuat, id_user_playlist, judul, deskripsi, jumlah_lagu, tanggal_dibuat, id_playlist, total_durasi)
        VALUES ('{email_pembuat}', '{id_user_playlist}', '{judul}', '{deskripsi}', {jumlah_lagu}, '{tanggal_dibuat}', '{id_playlist}', {total_durasi});
    """

def insert_playlist(id):
    return f"""
        INSERT INTO PLAYLIST (id)
        VALUES ('{id}');
    """

def get_label_profile(email):
    return f"""
            SELECT * FROM label WHERE email = '{email}';
            """

def get_user_profile(email):
    return f"""
            SELECT * FROM akun WHERE email = '{email}';
            """

def delete_user_playlist_query(id_user_playlist):
    return f"""
        DELETE FROM user_playlist WHERE id_user_playlist = '{id_user_playlist}';
    """

def delete_playlist_query(id):
    return f"""
        DELETE FROM playlist WHERE id = '{id}';
    """

def delete_akun_play_user_playlist(id_user_playlist):
    return f"""
        DELETE FROM AKUN_PLAY_USER_PLAYLIST WHERE id_user_playlist = '{id_user_playlist}';
    """

def delete_playlist_song_query(id_playlist):
    return f"""
        DELETE FROM PLAYLIST_SONG WHERE id_playlist = '{id_playlist}';
    """

def set_judul_user_playlist(judul, id_user_playlist):
    return f"""
        UPDATE USER_PLAYLIST
        SET judul = '{judul}'
        WHERE id_user_playlist = '{id_user_playlist}';
    """

def set_deskripsi_user_playlist(deskripsi, id_user_playlist):
    return f"""
        UPDATE USER_PLAYLIST
        SET deskripsi = '{deskripsi}'
        WHERE id_user_playlist = '{id_user_playlist}';
    """