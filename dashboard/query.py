def get_user_data(email):
    return  f"""
        SELECT a.email ,
                a.nama, 
                a.kota_asal,
                a.tempat_lahir,
                a.tanggal_lahir,
                up.judul AS judul_playlist,
                k.judul AS judul,
                'lagu' AS tipe
        FROM akun a
        LEFT JOIN podcaster p ON p.email = a.email
        LEFT JOIN user_playlist up ON up.email_pembuat = a.email 
        LEFT JOIN songwriter sw ON sw.email_akun = a.email 
        LEFT JOIN songwriter_write_song sws ON sw.id = sws.id_songwriter 
        LEFT JOIN konten k ON k.id = sws.id_song 
        WHERE a.email = '{email}'
        UNION
        SELECT a.email ,
                a.nama, 
                a.kota_asal,
                a.tempat_lahir,
                a.tanggal_lahir,
                up.judul AS judul_playlist,
                k.judul AS judul,
                'podcast' AS tipe
        FROM akun a
        LEFT JOIN podcaster pr ON pr.email = a.email
        LEFT JOIN user_playlist up ON up.email_pembuat = a.email  
        LEFT JOIN podcast p ON p.email_podcaster = pr.email
        LEFT JOIN konten k ON k.id = p.id_konten 
        WHERE a.email = '{email}';
    """


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

