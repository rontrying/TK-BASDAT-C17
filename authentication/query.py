def select_all():
    return f"""
        SELECT * FROM akun;
    """

def insert_akun(email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal):
    return f"""
        INSERT INTO akun (email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal)
        VALUES ('{email}', '{password}', '{nama}', {gender}, '{tempat_lahir}', '{tanggal_lahir}', {is_verified}, '{kota_asal}');
    """

def insert_podcaster(email):
    return f"""
        INSERT INTO podcaster (email)
        VALUES ('{email}');
    """

def insert_artist(id, email_akun, id_pemilik_hak_cipta):
    return f"""
        INSERT INTO artist (id, email_akun, id_pemilik_hak_cipta)
        VALUES ('{id}', '{email_akun}', '{id_pemilik_hak_cipta}');
    """

def insert_songwriter(id, email_akun, id_pemilik_hak_cipta):
    return f"""
        INSERT INTO songwriter (id, email_akun, id_pemilik_hak_cipta)
        VALUES ('{id}', '{email_akun}', '{id_pemilik_hak_cipta}');
    """

def insert_label(id, nama, email, password, kontak, id_pemilik_hak_cipta):
    return f"""
        INSERT INTO label (id, nama, email, password, kontak, id_pemilik_hak_cipta)
        VALUES ('{id}', '{nama}', '{email}', '{password}', '{kontak}', '{id_pemilik_hak_cipta}');
    """

def insert_pemilik_hak_cipta(id, rate_royalti):
    return f"""
        INSERT INTO pemilik_hak_cipta (id, rate_royalti)
        VALUES ('{id}', {rate_royalti});
    """

def insert_non_premium(email):
    return f"""
        INSERT INTO nonpremium (email)
        VALUES ('{email}');
    """

def get_pemilik_hak_cipta(id):
    return f"""
        SELECT * from pemilik_hak_cipta WHERE id = '{id}';
    """

def get_label(id):
    return f"""
        SELECT id FROM label WHERE id = '{id}';
    """

def get_user_role(email, password):
    return f"""
        WITH roles AS (
            SELECT 'User' AS role, email FROM akun WHERE email = '{email}' AND password = '{password}'
            UNION ALL
            SELECT 'Artist' AS role, email_akun AS email FROM artist WHERE email_akun = '{email}'
            UNION ALL
            SELECT 'Podcaster' AS role, email FROM podcaster WHERE email = '{email}'
            UNION ALL
            SELECT 'Label' AS role, email FROM label WHERE email = '{email}' AND password = '{password}'
            UNION ALL
            SELECT 'Songwriter' AS role, email_akun AS email FROM songwriter WHERE email_akun = '{email}'
            UNION ALL
            SELECT 'Premium' AS role, email FROM premium WHERE email = '{email}'
        )

        SELECT *
        FROM roles;
    """

def get_nonpremium(email):
    return f"""
        SELECT email FROM nonpremium WHERE email = '{email}';
    """

def get_email(email):
    return f"""
        SELECT email FROM akun WHERE email = '{email}'
        UNION ALL
        SELECT email FROM label WHERE email = '{email}';
    """

def get_podcaster(email):
    return f"""
        SELECT email FROM podcaster WHERE email = '{email}';
    """

def get_artist(email):
    return f"""
        SELECT email_akun FROM artist WHERE email_akun = '{email}';
    """

def get_artist_by_id(id):
    return f"""
        SELECT id FROM artist WHERE id = '{id}';
    """

def get_songwriter(email):
    return f"""
        SELECT email_akun FROM songwriter WHERE email_akun = '{email}';
    """

def get_songwriter_by_id(id):
    return f"""
        SELECT id FROM songwriter WHERE id = '{id}';
    """

def delete_akun(email):
    return f"""
        DELETE FROM akun WHERE email = '{email}';
    """

def delete_podcaster(email):
    return f"""
        DELETE FROM podcaster WHERE email = '{email}';
    """

def delete_artist(email):
    return f"""
        DELETE FROM artist WHERE email_akun = '{email}';
    """

def delete_songwriter(email):
    return f"""
        DELETE FROM songwriter WHERE email_akun = '{email}';
    """