roles = {"User": "is_user", 
        "Artist": "is_artist", 
        "Podcaster": "is_podcaster", 
        "Label": "is_label", 
        "Songwriter": "is_songwriter", 
        "Premium": "is_premium"}


def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def parse_role(user_role):
    inverted_roles = {v: k for k, v in roles.items()}
    return ", ".join([inverted_roles[role] for role in user_role])
