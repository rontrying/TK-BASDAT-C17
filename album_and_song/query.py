def select_all():
    return f"""
        SELECT nama,id FROM label;
    """
def select_album():
    return f"""
        select judul, l.nama, jumlah_lagu, total_durasi, a.id from album a, label l where a.id_label = l.id;
    """

def select_lagu(nama_album):
    return f"""
        select k.judul, k.durasi, s.total_play, s.total_download from konten k, song s, album a 
        where k.id = s.id_konten and a.id = s.id_album and a.judul = '{nama_album}';
    """

def select_artist():
    return f"""
        select nama from artist a, akun ak where a.email_akun = ak.email ;
    """

def select_songwriter():
    return f"""
        select nama from songwriter a, akun ak where a.email_akun = ak.email ;
    """

def select_nama_album(id_album):
    return f"""
        select judul from album a where a.id = '{id_album}' ;
    """

def insert_new_album(id,title,jumlah_lagu,id_label,total_durasi):
    # album baru 0 saat lagu ditambah akan diupdate dengan trigger
    jumlah_lagu = 0
    total_durasi = 0
    return f"""
        INSERT INTO ALBUM VALUES (
        '{id}',
        '{title}',
        '{jumlah_lagu}',
        '{id_label}',
        '{total_durasi}'
        );
        """