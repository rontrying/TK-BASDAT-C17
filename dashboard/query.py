def get_user_profile(email):
    return f"""
            SELECT * FROM akun WHERE email = '{email}';
            """

def get_label_profile(email):
    return f"""
            SELECT * FROM label WHERE email = '{email}';
            """