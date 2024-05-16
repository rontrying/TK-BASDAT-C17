def get_user_data(email):
    query = """
        SELECT 
            a.email, 
            a.nama, 
            a.kota_asal, 
            a.gender, 
            a.tempat_lahir, 
            a.tanggal_lahir,
            up.judul AS judul_playlist,
            COALESCE(k_song.judul, k_podcast.judul) AS judul,
            CASE 
                WHEN k_podcast.id IS NOT NULL THEN 'podcast'
                WHEN k_song.id IS NOT NULL THEN 'lagu'
            END AS tipe
        FROM akun a
        LEFT JOIN user_playlist up ON up.email_pembuat = a.email
        LEFT JOIN podcaster pr ON pr.email = a.email
        LEFT JOIN podcast p ON p.email_podcaster = pr.email
        LEFT JOIN konten k_podcast ON k_podcast.id = p.id_konten
        LEFT JOIN songwriter sw ON sw.email_akun = a.email 
        LEFT JOIN songwriter_write_song sws ON sw.id = sws.id_songwriter 
        LEFT JOIN konten k_song ON k_song.id = sws.id_song 
        WHERE a.email = %s;
    """
    return query, [email] 


def get_label_data(email):
    query = """
        SELECT 
            l.email, 
            l.nama AS label_name, 
            l.kontak,
            a.judul AS judul_album
        FROM label l
        LEFT JOIN album a ON l.id = a.id_label
        WHERE l.email = %s;
    """
    return query, [email]


def get_user_profile(email):
    return f"""
            SELECT * FROM akun WHERE email = '{email}';
            """

def get_label_profile(email):
    return f"""
            SELECT * FROM label WHERE email = '{email}';
            """


def check_subscription_status(email):
    return f"SELECT check_subscription_status('{email}');"

