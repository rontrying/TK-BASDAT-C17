def select_song_details(id_konten):
    return f"""
        SELECT 
            k.judul AS "title",
            array_agg(DISTINCT g.genre) FILTER (WHERE g.genre IS NOT NULL) AS "genres",
            ak.nama AS "artist",
            array_agg(DISTINCT ak.nama) FILTER (WHERE ak.nama IS NOT NULL) AS "songwriters",
            k.durasi AS "duration",
            TO_CHAR(k.tanggal_rilis, 'DD/MM/YY') AS "release_date",
            k.tahun AS "year",
            s.total_play AS "total_plays",
            s.total_download AS "total_downloads",
            al.judul AS "album"
        FROM 
            KONTEN k
        JOIN 
            SONG s ON k.id = s.id_konten
        JOIN 
            ARTIST ar ON s.id_artist = ar.id
        JOIN 
            AKUN ak ON ar.email_akun = ak.email
        LEFT JOIN 
            ALBUM al ON s.id_album = al.id
        LEFT JOIN 
            SONGWRITER_WRITE_SONG sws ON s.id_konten = sws.id_song
        LEFT JOIN 
            SONGWRITER sw ON sws.id_songwriter = sw.id
        LEFT JOIN 
            GENRE g ON k.id = g.id_konten
        WHERE 
            k.id = '{id_konten}'
        GROUP BY 
            k.judul, ak.nama, k.durasi, k.tanggal_rilis, k.tahun, s.total_play, s.total_download, al.judul
        ;
    """

def check_playlist_song(id_playlist, id_song):
    return f"""
        SELECT 1
        FROM playlist_song
        WHERE id_playlist = '{id_playlist}' AND id_song = '{id_song}';
    """

def select_downloaded_song(id_song, email_downloader):
    return f"""
        SELECT *
        FROM downloaded_song
        WHERE id_song = '{id_song}' AND email_downloader = '{email_downloader}'";
    """

def insert_song_to_downloaded_song(id_song, email_downloader):
    return f"""
        INSERT INTO downloaded_song (id_song, email_downloader) 
        VALUES ('{id_song}', '{email_downloader}');
    """

def select_one_playlist(id_song, email):
    return f"""
        SELECT 
            up.id_user_playlist
        FROM 
            playlist_song ps
        JOIN 
            user_playlist up ON up.id_playlist = ps.id_playlist
        WHERE
            up.email_pembuat = '{email}' AND
            ps.id_song = '{id_song}';  
    """

def insert_akun_play_song(email_pemain, id_song):
    return f"""
        INSERT INTO akun_play_song (email_pemain, id_song, waktu)
        VALUES ('{email_pemain}', '{id_song}', CURRENT_TIMESTAMP);
    """

def update_akun_play_song(id_song):
    return f"""
        UPDATE song
        SET total_play = (
            SELECT COUNT(*) FROM akun_play_song WHERE id_song = '{id_song}'
        )
        WHERE id_konten = '{id_song}';
    """

def update_download(id_song):
    return f"""
        UPDATE song
        SET total_download = (
            SELECT COUNT(*) FROM downloaded_song WHERE id_song = '{id_song}'
        )
        WHERE id_konten = '{id_song}';
    """