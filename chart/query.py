def get_chart():
    return """
        SELECT * FROM chart;
        """

def get_chart_detail(chart_type):
    return f"""
        SELECT ak.nama AS nama_penyanyi,
                k.judul AS judul_lagu,
                k.tanggal_rilis,
                s.total_play 
        FROM playlist_song ps 
        LEFT JOIN konten k ON k.id = ps.id_song   
        LEFT JOIN song s ON s.id_konten = k.id
		LEFT JOIN artist a ON s.id_artist = a.id 
		LEFT JOIN akun ak ON ak.email = a.email_akun 
		WHERE ps.id_playlist = '3170f437-a8f7-ef5a-060e-df5b39118497'
        ORDER BY s.total_play DESC;
        """


def update_chart_detail(chart_type):
    return f"""BEGIN;

        DELETE FROM playlist_song
        WHERE id_playlist = '3170f437-a8f7-ef5a-060e-df5b39118497';

        INSERT INTO playlist_song (id_playlist, id_song)
        SELECT '3170f437-a8f7-ef5a-060e-df5b39118497' AS id_playlist,
                s.id_konten AS id_song
        FROM konten k
        RIGHT JOIN song s ON s.id_konten = k.id 
        ORDER BY total_play DESC
        LIMIT 20;
        
        COMMIT;"""