# REQUIREMENTS
1. sqlite3

# DB USED
- SQLITE3

# HOW TO RUN
- Run ```python main.py``` to start

# METHODOLGY ETL
- The data files are cleaned for comemnts.
- If DB file does not exist, it is created.
- If DB file exits, songs and artist tables are checked for existence. If they do not exist, tables are created.
- The songs and artist records are inserted into tables.
- Artist name is taken from user and is used to find artist ID, which in turn is used t lookup for songs.
- I didnot use joins due to increasing complexity of joins. Indexes can also be used to retreive the data faster. 