def select_all():
    return f"""
        SELECT nama,id FROM label;
    """
def select_album_artist(id):
    return f"""
        select distinct a.judul, l.nama, jumlah_lagu, total_durasi, a.id from album a 
        join label l on a.id_label = l.id join song s on a.id = s.id_album join artist a2 
        on a2.id = s.id_artist where a2.id = '{id}';
    """
def select_album_songwriter(id):
    return f"""
        select distinct a.judul, l.nama, jumlah_lagu, total_durasi, a.id from album a 
        join label l on a.id_label = l.id join song s on a.id = s.id_album join songwriter_write_song sws  
        on sws.id_song = s.id_konten where sws.id_songwriter = '{id}';
    """
def select_lagu(id):
    return f"""
        select k.judul, k.durasi, s.total_play, s.total_download, k.id from konten k, song s, album a 
        where k.id = s.id_konten and a.id = s.id_album and a.id = '{id}';
    """

def select_artist():
    return f"""
        select nama, a.id from artist a, akun ak where a.email_akun = ak.email;
    """

def select_songwriter():
    return f"""
        select nama, s.id  from songwriter s, akun ak where s.email_akun = ak.email ;
    """

def select_nama_album(id_album):
    return f"""
        select judul from album a where a.id = '{id_album}' ;
    """

def select_genre():
    return f"""
    select distinct genre from genre g ;
    """

def get_id_artist(email):
    return f"""
        select id from artist a where a.email_akun = '{email}' ;
    """

def get_id_songwriter(email):
    return f"""
        select id from songwriter s where s.email_akun = '{email}' ;
    """
def get_nama(email):
    return f"""
        select nama from akun a where a.email = '{email}';
    """

def insert_new_album(id,title,jumlah_lagu,id_label,total_durasi):
    return f"""
        INSERT INTO ALBUM VALUES (
        '{id}',
        '{title}',
        '{jumlah_lagu}',
        '{id_label}',
        '{total_durasi}'
        );
        """

from datetime import datetime

def insert_new_konten(id, judul, durasi):
    current_date = datetime.now().strftime('%Y-%m-%d')  # Mendapatkan tanggal saat ini
    current_year = datetime.now().year  # Mendapatkan tahun saat ini
    
    return f"""
    INSERT INTO KONTEN (id, judul, tanggal_rilis, tahun, durasi) VALUES (
        '{id}',
        '{judul}',
        '{current_date}',
        '{current_year}',
        '{durasi}'
    );
    """

def insert_konten_genre(id,genre):
    return f"""
    INSERT INTO GENRE VALUES (
        '{id}',
        '{genre}'
        );
    """

def insert_song(id_konten,id_artist,id_album,total_play=0,total_download=0):
    return f"""
    INSERT INTO SONG VALUES (
        '{id_konten}',
        '{id_artist}',
        '{id_album}',
        '{total_play}',
        '{total_download}'
    )
    """

def insert_songwriter_write_song(id_songwriter,id_song):
    return f"""
    INSERT INTO SONGWRITER_WRITE_SONG VALUES (
        '{id_songwriter}',
        '{id_song}'
    )
    """

def album_delete(id):
    return f"""
        delete from album where id = '{id}';
    """

def lagu_delete(id):
    return f"""
        delete from konten where id = '{id}';
    """