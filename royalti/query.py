def get_id_pemilik_hak_cipta(email,mode):
    if mode == "artist":
        return f"""
            select a2.id_pemilik_hak_cipta  from akun a, artist a2  where a.email = a2.email_akun and a2.email_akun = '{email}';
        """
    elif mode == "songwriter":
        return f"""
            select s.id_pemilik_hak_cipta  from akun a, songwriter s where a.email = s.email_akun and s.email_akun = '{email}';
        """
    else :
        return f"""
            select l.id_pemilik_hak_cipta from label l where l.email = '{email}';
        """

def get_list_royalti(id_pemilik_hak_cipta):
    return f"""
        select k.judul, a.judul, s.total_play, s.total_download, r.jumlah from konten k, song s, royalti r, album a 
        where r.id_song = s.id_konten and s.id_konten = k.id and a.id = s.id_album 
        and r.id_pemilik_hak_cipta  = '{id_pemilik_hak_cipta}';
    """