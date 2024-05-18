

def select_playlist(id):
    return f"""
        SELECT * FROM playlist WHERE id = '{id}';
    """

def select_all_user_playlist(email):
    return f"""
        SELECT up.judul, p.id
        FROM user_playlist up
        JOIN playlist p ON up.id_playlist = p.id
        JOIN akun a ON a.email = up.email_pembuat
        WHERE up.email_pembuat = '{email}';
    """

def select_user_playlist_by_id(id):
    return f"""
        SELECT * from user_playlist where id_user_playlist = '{id}';
    """

def select_user_playlist_by_root_id(id):
    return f"""
        SELECT * from user_playlist where id_playlist = '{id}';
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

def get_songs(id_user_playlist):
    return f"""
        SELECT k.judul, a.nama, k.durasi, k.id
        FROM user_playlist up
        INNER JOIN playlist_song ps ON up.id_playlist = ps.id_playlist
        INNER JOIN song s ON ps.id_song = s.id_konten
        INNER JOIN konten k ON s.id_konten = k.id
        INNER JOIN artist t ON s.id_artist = t.id
        INNER JOIN akun a ON t.email_akun = a.email
        WHERE up.id_user_playlist = '{id_user_playlist}';
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

def insert_playlist_song(id_playlist, id_song):
    return f"""
        INSERT INTO playlist_song (id_playlist, id_song) 
        VALUES ('{id_playlist}', '{id_song}');
    """

def delete_song_from_playlist_song(id_playlist, id_song):
    return f"""
        DELETE FROM playlist_song
        WHERE id_playlist = '{id_playlist}' AND id_song = '{id_song}';
    """

def update_user_playlist_count(id_playlist):
    return f"""
        UPDATE user_playlist
        SET jumlah_lagu = (
            SELECT COUNT(*) FROM playlist_song WHERE id_playlist = '{id_playlist}'
        )
        WHERE id_playlist = '{id_playlist}';
    """

def update_user_playlist_duration(id_playlist):
    return f"""
        UPDATE USER_PLAYLIST
        SET total_durasi = COALESCE((
            SELECT SUM(k.durasi)
            FROM PLAYLIST_SONG ps
            JOIN SONG s ON ps.id_song = s.id_konten
            JOIN KONTEN k ON s.id_konten = k.id
            WHERE ps.id_playlist = '{id_playlist}'
        ), 0)
        WHERE id_playlist = '{id_playlist}';
    """