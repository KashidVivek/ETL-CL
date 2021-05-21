import etl

def main(artist_name):
    database = "datastore.db"
    song_file = "data/shs_dataset_train.txt"
    artist_file = "data/unique_artists.txt"

    con = etl.create_connection(database)
    if not etl.check_table("SONGS",con):
        etl.load_song_data(song_file,con)

    if not etl.check_table("ARTIST",con):
        etl.load_artist_data(artist_file,con)
    
   
    songs = etl.find_songs_by_artist(artist_name.lower(),con)
    return songs
    


if __name__ == '__main__':
    print("Press CTRL + C to exit.")
    try: 
        while True:
            artist_name = input("Artist name: ")
            songs_by_band = main(artist_name)
            if not songs_by_band:
                print("No songs Found.")
            else:
                print(f'Songs by {artist_name}')
                print(50*"-")
                for i,song in enumerate(songs_by_band):
                    print(f'({i + 1}). {song}')
                    print(50*"-")
    except KeyboardInterrupt:
        pass
                
