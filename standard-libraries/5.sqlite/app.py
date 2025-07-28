
import sqlite3
import json
from pathlib import Path

parent = Path(__file__).parent


# * Read the JSON file and print the movies and insert them into the SQLite database

# movies = json.loads(Path(parent / "movies.json").read_text(encoding="utf-8"))

# with sqlite3.connect(parent / "Movies.db") as conn:
#     create_table = "CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER NOT NULL)"
#     conn.execute(create_table)
#     conn.commit()
#     command = "INSERT OR IGNORE INTO Movies (id, title, year) VALUES (?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# * Read the movies from the SQLite database and print them

with sqlite3.connect(parent / "Movies.db") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # * Way 1: Using a for loop to iterate over the cursor
    for row in cursor:
        print(f"Movie {row[0]}: {row[1]} ({row[2]})")
    # * Way 2: Using fetchall() to get all rows at once
    # movies = cursor.fetchall()
    # for movie in movies:
    #     print(f"Movie {movie[0]}: {movie[1]} ({movie[2]})")
