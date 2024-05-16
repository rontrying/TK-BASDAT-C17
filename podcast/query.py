def get_podcast_detail(podcast_id):
    return f"""SELECT k.id AS id,
            k.judul AS judul_podcast,
            k.durasi AS durasi_podcast,
            k.tanggal_rilis AS tanggal_rilis_podcast,
            k.tahun AS tahun,
            g.genre AS genre,
            a.nama AS nama,
            e.judul AS judul_eps,
            e.deskripsi AS deskripsi_eps,
            e.durasi AS durasi_eps,
            e.tanggal_rilis AS tanggal_rilis_eps
        FROM konten k 
        LEFT JOIN genre g ON k.id = g.id_konten 
        LEFT JOIN podcast p ON k.id  = p.id_konten
        LEFT JOIN episode e ON p.id_konten  = e.id_konten_podcast
        LEFT JOIN akun a ON p.email_podcaster = a.email 
        WHERE k.id ='{podcast_id}';
        ;"""