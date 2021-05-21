import unittest
import etl
import sql_queries as query

class DBConnection():
    def __init__(self,dbname="datastore.db"):
        self.con = etl.create_connection(dbname)

class TestETL(unittest.TestCase):

    def test_table_exists(self):
        connection = etl.create_connection("datastore.db")
        self.assertTrue(etl.check_table("SONGS",connection))
        self.assertTrue(etl.check_table("ARTIST", connection))

    def test_songs_by_artist(self):
        connection = etl.create_connection("datastore.db")
        self.assertEqual(etl.find_songs_by_artist('bebe winans', connection),["My Sweet Lord","Hark! The Herald Angels Sing","Silent Night","O Come All Ye Faithful (Album Version)"])



if __name__ == '__main__':
    unittest.main()