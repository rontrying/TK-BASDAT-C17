def is_user(email):
    return f"""
            SELECT * FROM akun WHERE email = '{email}';
            """

def is_artist(email):
    return f"""
            SELECT * FROM artist WHERE email_akun = '{email}';
            """

def is_podcaster(email):
    return f"""
            SELECT * FROM podcaster WHERE email = '{email}';
            """

def is_label(email):
    return f"""
            SELECT * FROM label WHERE email = '{email}';
            """

def is_songwriter(email):
    return f"""
            SELECT * FROM songwriter WHERE email_akun = '{email}';
            """