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

def get_podcast_list(email_account):
    return f"""
        SELECT k.judul, 
        p.id_konten AS podcast_id,
        COALESCE(COUNT(e.id_episode), 0) AS total_episode,
        COALESCE(SUM(e.durasi), 0) AS total_durasi
        FROM konten k 
        RIGHT JOIN podcast p ON p.id_konten = k.id 
        LEFT JOIN episode e ON p.id_konten = e.id_konten_podcast
        LEFT JOIN podcaster pr ON p.email_podcaster = pr.email 
  		WHERE pr.email = '{email_account}'
        GROUP BY k.judul, p.id_konten ;
        """

def get_episode_list(podcast_id):
    return f"""
        SELECT e.id_episode AS episode_id,
                e.id_konten_podcast AS podcast_id,
                k.judul AS judul_podcast,
                e.judul,
                deskripsi,
                e.durasi,
                e.tanggal_rilis
        FROM podcast p 
        LEFT JOIN episode e ON p.id_konten = e.id_konten_podcast 
        LEFT JOIN konten k ON p.id_konten = k.id
        WHERE p.id_konten ='{podcast_id}';"""

def insert_podcast_to_konten(podcast_id, judul, tanggal_rilis, tahun, durasi):
    return f"""
        INSERT INTO konten (id, judul, tanggal_rilis, tahun, durasi) 
        VALUES ('{podcast_id}', '{judul}', '{tanggal_rilis}', '{tahun}', '{durasi}');
        """

def insert_podcast_to_genre(podcast_id, genre):
    return f"""
        INSERT INTO genre (id_konten, genre) 
        VALUES ('{podcast_id}', '{genre}');
        """

def insert_podcast_to_podcast(podcast_id, email_podcaster):
    return f"""
        INSERT INTO podcast (id_konten, email_podcaster) 
        VALUES ('{podcast_id}', '{email_podcaster}');
        """

def insert_episode(episode_id, podcast_id, judul, deskripsi, durasi, tanggl_rilis):
    return f"""
        INSERT INTO episode (id_episode, id_konten_podcast, judul, deskripsi, durasi, tanggal_rilis) 
        VALUES ('{episode_id}', '{podcast_id}', '{judul}', '{deskripsi}', '{durasi}', '{tanggl_rilis}');
        """

def delete_podcast_from_genre(podcast_id):
    return f"""
        DELETE FROM genre 
        WHERE id_konten = '{podcast_id}';
        """

def delete_podcast_from_podcast(podcast_id):
    return f"""
        DELETE FROM podcast 
        WHERE id_konten = '{podcast_id}';
        """

def delete_podcast_from_konten(podcast_id):
    return f"""
        DELETE FROM konten 
        WHERE id = '{podcast_id}';
        """

def delete_episode_from_episode(episode_id):
    return f"""
        DELETE FROM episode 
        WHERE id_episode = '{episode_id}';
        """
