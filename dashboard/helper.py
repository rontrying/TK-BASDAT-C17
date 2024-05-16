from utils import *

def get_context_data(cursor, query):
    cursor.execute(query)
    return parse(cursor)

def append_unique_items(source, target, key):
    for item in source:
        if item[key] and item[key] not in target:
            target.append(item[key])