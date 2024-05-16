def get_chart():
    return """
        SELECT * FROM chart;
        """

def get_chart_detail(period):
    return f"""
        SELECT a.nama AS nama_penyanyi,
                k.judul AS judul_lagu,
                k.tanggal_rilis,
                COUNT(aps.id_song) AS total_plays
        FROM akun_play_song aps
        LEFT JOIN konten k ON k.id = aps.id_song 
        LEFT JOIN akun a ON a.email =aps.email_pemain 
        LEFT JOIN song s ON s.id_konten = k.id 
        WHERE waktu >= NOW() - INTERVAL '{period}'
        GROUP BY a.nama, k.judul, k.tanggal_rilis 
        ORDER BY total_plays DESC
        LIMIT 20;
        """