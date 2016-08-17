import json
from collections import Counter
import threading

DB_FILE_NAME = 'db.json'
write_lock = threading.Lock()


def add_pozor(item):
    write_lock.acquire()
    try:
        current = json.load(open(DB_FILE_NAME))
    except FileNotFoundError:
        current = {}

    current['pozor'] = current.get('pozor', []) + [item]
    with open(DB_FILE_NAME, 'w') as db_file:
        json.dump(current, db_file)

    write_lock.release()


def list_pozor():
    try:
        current = json.load(open(DB_FILE_NAME))
    except FileNotFoundError:
        current = {}
    return current.get('pozor', [])


def get_pozor_rating():
    incidents = list_pozor()
    counts = Counter(map(lambda x: x['name'], incidents))
    rating = []
    for (name, count) in counts.most_common():
        rating.append({
            'name': name,
            'count': count
        })
    return rating
