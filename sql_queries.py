CHECK_TABLE = ''' 
    SELECT COUNT(name) FROM sqlite_master
    WHERE TYPE='table' AND name=?; 
'''

CREATE_SONGS_TABLE = '''
    CREATE TABLE SONGS (
    song_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name VARCHAR2 (255),
    TID VARCHAR2 (255),
    AID VARCHAR2 (255),
    perf NUMERIC (10)
    )
'''

CREATE_ARTIST_TABLE = '''
    CREATE TABLE ARTIST (
    AID VARCHAR2 (255) PRIMARY KEY,
    SOMEID VARCHAR2 (255),
    TID VARCHAR2 (255),
    ANAME VARCHAR2 (255)
    )
'''

INSERT_SONGS = '''
    INSERT INTO SONGS(song_name,TID,AID,perf) 
    VALUES (?, ?, ?, ?);
'''

INSERT_ARTIST = '''
    INSERT INTO ARTIST(AID,SOMEID,TID,ANAME) 
    VALUES (?, ?, ?, ?);
'''

SELECT_AID = ''' 
    SELECT AID FROM ARTIST 
    WHERE ANAME=?;
'''

SELECT_SONGS_BY_AID = '''
    SELECT SONG_NAME FROM SONGS 
    WHERE AID=?;
'''
