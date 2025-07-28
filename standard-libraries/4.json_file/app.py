
import json
from pathlib import Path
parent = Path(__file__).parent

# movies = [
#     {
#         "id": 1,
#         "title": "Inception",
#         "year": 2010,
#     },
#     {
#         "id": 2,
#         "title": "The Matrix",
#         "year": 1999,
#     },
#     {
#         "id": 3,
#         "title": "Interstellar",
#         "year": 2014,
#     },
#     {
#         "id": 4,
#         "title": "The Shawshank Redemption",
#         "year": 1994,
#     },
#     {
#         "id": 5,
#         "title": "Pulp Fiction",
#         "year": 1994,
#     }
# ]

# data = json.dumps(movies)
# Path(parent / "movies.json").write_text(data, encoding="utf-8")

# * Read the JSON file and print the movies
data = Path(parent / "movies.json").read_text(encoding="utf-8")
movies = json.loads(data)
for index, movie in enumerate(movies):
    print(f"Movie {index + 1}: {movie['title']} ({movie['year']})")
