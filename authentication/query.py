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