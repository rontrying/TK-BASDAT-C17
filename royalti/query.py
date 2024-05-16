def get_list_royalti_artist(email):
    return f"""
        SELECT k.judul, a.judul, s.total_play, s.total_download, 
        s.total_play * phc.rate_royalti AS royalties 
        FROM KONTEN k
        JOIN SONG s ON s.id_konten = k.id
        JOIN ALBUM a ON s.id_album = a.id
        JOIN ARTIST r ON s.id_artist = r.id
        JOIN PEMILIK_HAK_CIPTA phc ON phc.id = r.id_pemilik_hak_cipta
        JOIN ROYALTI rt ON rt.id_pemilik_hak_cipta = phc.id AND rt.id_song = s.id_konten
        WHERE r.email_akun = '{email}';
    """

def get_list_royalti_songwriter(email):
    return f"""
       SELECT k.judul, a.judul, s.total_play, s.total_download, 
        s.total_play * phc.rate_royalti AS royalties 
        FROM KONTEN k
        JOIN SONG s ON s.id_konten = k.id
        JOIN ALBUM a ON s.id_album = a.id
        JOIN SONGWRITER_WRITE_SONG sw ON sw.id_song = s.id_konten
        join songwriter s2 on s2.id = sw.id_songwriter 
        JOIN PEMILIK_HAK_CIPTA phc ON phc.id = s2.id_pemilik_hak_cipta
        JOIN ROYALTI rt ON rt.id_pemilik_hak_cipta = phc.id AND rt.id_song = s.id_konten
        WHERE s2.email_akun = '{email}';
    """

def get_list_royalti_label(email):
    return f"""
        SELECT k.judul, a.judul, s.total_play, s.total_download, 
        s.total_play * phc.rate_royalti AS royalties 
        FROM KONTEN k
        JOIN SONG s ON s.id_konten = k.id
        JOIN ALBUM a ON s.id_album = a.id
        JOIN LABEL l ON a.id_label = l.id
        JOIN PEMILIK_HAK_CIPTA phc ON l.id = a.id_label
        JOIN ROYALTI rt ON rt.id_pemilik_hak_cipta = phc.id AND rt.id_song = s.id_konten
        WHERE l.email = '{email}';
    """