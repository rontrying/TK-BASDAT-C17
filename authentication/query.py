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

# TODO: ID SAMA PEMILIK HAK CIPTA BLM TAU
def insert_artist(id, email_akun, id_pemilik_hak_cipta):
    return f"""
        INSERT INTO podcaster (id, email_akun, id_pemilik_hak_cipta)
        VALUES ('{id}', '{email_akun}', '{id_pemilik_hak_cipta}');
    """

# TODO: ID SAMA PEMILIK HAK CIPTA BLM TAU
def insert_songwriter(id, email_akun, id_pemilik_hak_cipta):
    return f"""
        INSERT INTO songwriter (id, email_akun, id_pemilik_hak_cipta)
        VALUES ('{id}', '{email_akun}', '{id_pemilik_hak_cipta}');
    """

# TODO: UUID belom dibikin
def insert_label(id, nama, email, password, kontak, id_pemilik_hak_cipta):
    return f"""
        INSERT INTO label (id, nama, email, password, kontak, id_pemilik_hak_cipta)
        VALUES ('{id}', '{nama}', '{email}', '{password}', '{kontak}', {id_pemilik_hak_cipta}');
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
