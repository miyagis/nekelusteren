import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def get_data(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data


def delete_tupples_from_list(data):
    l = []
    for i in range(len(data)):
        if data[i][0] is not None:
            l.append(data[i][0])
    return l


if __name__ == '__main__':
    db_file = "/home/bart/Projects/nekelusteren/data.db"
    conn = create_connection(db_file=db_file)
    twitter_IDs = get_data(conn, "SELECT twitter_ID FROM politicians;")
    l = delete_tupples_from_list(twitter_IDs)

