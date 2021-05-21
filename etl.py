import sqlite3
import re
from sqlite3.dbapi2 import Error
import sql_queries as query


def create_connection(db_file):
    """
    @desc: Sqlite3 connection
    @param: DB file
    @returns: Connection

    """
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return con


def check_table(table_name,con):
    """
    @desc: Check if table exists in DB
    @param: table_name,connection
    @returns: True if exists
    """
    cur = con.cursor()
    cur.execute(query.CHECK_TABLE,(table_name,))

    #if the count is 1, then table exists
    if cur.fetchone()[0]==1:
        return True
    return False

def create_songs_table(con):
    """
    @desc: Create Table
    @param: connection
    @returns: None

    """
    cur = con.cursor()
    cur.execute(query.CREATE_SONGS_TABLE)

    print("Songs Table successfully created.")
    con.commit()

def clean_song_file(song_file):
    """
    @desc: Clean comments from file
    @param: Filename
    @returns: None

    """
    with open(song_file,"r") as f:
        data = f.read()

    data = re.sub(r'\n#.*', "", data)

    with open(song_file, "w") as f:
        f.write(data)

def load_song_data(song_file,con):
    """
    @desc: Insert songs in table
    @param: file,connection
    @returns: None
    """
    clean_song_file(song_file)
    create_songs_table(con)

    file_data = [i for i in open(song_file)]
    song_data = []
    for song in file_data:
        if song.startswith("#"):
            continue
        if song.startswith("%"):
            song_name = song.split(',')[-1].rstrip("\n").lstrip()
        else:
            song_info = song.split("<SEP>")
            song_info[-1] = song_info[-1].rstrip('\n')
            song_data.append([song_name]+song_info)

    cur = con.cursor()
    cur.executemany(query.INSERT_SONGS, song_data)
    con.commit()


def create_artist_table(con):
    """
    @desc: Create table
    @param: connection
    @returns: None
    """
    cur = con.cursor()
    cur.execute(query.CREATE_ARTIST_TABLE)
    print("Artist Table successfully created.")
    con.commit()


def load_artist_data(artist_file,con):
    """
    @desc: Insert artist in table
    @param: file, connection
    @returns: None
    """
    create_artist_table(con)
    cur = con.cursor()
    artist_data = []
    for row in open(artist_file):
        artist_info = row.rstrip('\n').split("<SEP>")
        artist_info[-1] = artist_info[-1].lower()
        artist_data.append(artist_info) 
    cur.executemany(query.INSERT_ARTIST, artist_data)
    con.commit()


def find_songs_by_artist(artist_name,con):
    """
    @desc: Get song by artist name
    @param: artist name, connection
    @returns: Song list
    """
    cur = con.cursor()
    cur.execute(query.SELECT_AID,(artist_name,))
    artist_id = cur.fetchone()

    if not artist_id:
        return []

    cur.execute(query.SELECT_SONGS_BY_AID,(artist_id[0],))
    song_list = cur.fetchall()

    return [song[0] for song in song_list]


