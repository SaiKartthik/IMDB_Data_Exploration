# NumPy -> To perform the Mathematical operation
import numpy as np

# Pandas -> Data Manipulation tool
import pandas as pd

# SQLite -> Server-less Databse
import sqlite3 as sq

"""Step 1: Connect your Database (or create a connection) -> sqlite3.connect(database_name)
Step 2: Use the cursor function -> database_variable.cursor()

# Workflow

1. You need to establish a connection to the SQLite Database by creating a connection object
2. Then, you need to create a cursor object using cursor() method
3. Then, execute the query -> cursor_variable.execute('query')
4. To fetch the data, then use fetchall() method of the cursor variable/object
5. You have to create a DataFrame w.r.t. the SQLite Database
6. Data Exploration, Data Manipulation, Data Cleaning, Data Visualisation
7. Conclusion at every step
"""


# Establishing the Database connection
db = "./movies.sqlite"
conn = sq.Connection(db)
print(conn)
cur = conn.cursor()
cur.execute('select * from movies')
movies = cur.fetchall()
# print(movies)

movies_df = pd.DataFrame(movies, columns=['id', 'original_title', 'budget', 'popularity', 'release_date',
                                          'revenue', 'title', 'vote_average', 'vote_count', 'overview', 'tagline',
                                          'uid', 'director_id'])
print(movies_df)
print(movies_df.info())
print(movies_df['vote_average'])

cur.execute("Select * from directors")
directors = cur.fetchall()
# print(directors)

directors_df = pd.DataFrame(directors, columns=['name', 'director_id', 'gender', "uid", "department"])
print(directors_df.info())

print(directors_df.shape)

#1 How many movies are present in Movies table
cur.execute("Select count(original_title) from movies")
no_movies = cur.fetchall()
print("\nNo of movies present in the table are : ", no_movies[0][0])

#2 Find these three directors : James Cameron, Luc Besson and John Woo
cur.execute("Select * from directors where directors.name in ('James Cameron', 'Luc Besson', 'John Woo')")
directs = cur.fetchall()
print("\nHere is the info about directors : ", directs)

#3 Find all the directors with names starting with Steven
cur.execute("Select * from directors where name like 'Steven%'")
alikeName = cur.fetchall()
print("\nNames starting with Steven", alikeName)

#4 Count all the Female directors (Gender = 1)
cur.execute("Select count(name) from directors where Gender == 1")
FemaleDirs = cur.fetchall()
print('\nFemale directors are', FemaleDirs[0][0])

#5 Name of 10th first female director
cur.execute("Select name from directors where Gender = 1")
fm10 = cur.fetchall()
print("\n10th Female director is ", fm10[9][0])


#6 Find top three popular movies
cur.execute("Select original_title from movies order by popularity Desc limit 3")
pops = cur.fetchall()
print('\npopular movies are', pops[0][0], pops[1][0], pops[2][0])

#7 Find the top most bankable movies
cur.execute("Select original_title from movies order by budget desc limit 1")
bud = cur.fetchall()
print("\nTop bankable movie is",bud[0][0])

#8 Find the most awarded movie
cur.execute("Select original_title from movies where release_date > '2000-01-01' order by vote_average desc limit 10")
awarded = cur.fetchall()
print('\nTop awarded movie', awarded[0][0])

#9 Find all the movies that has been directed by Brenda Chapman
cur.execute('Select movies.original_title from movies left join directors on movies.director_id = directors.id where name == "Brenda Chapman"')
brenda = cur.fetchall()
print("\nMovies directoed by Brenda Chapman is/are ", brenda[0][0])

#10 Find who has made the most number of movies
cur.execute('Select directors.name from directors join movies where directors.id = movies.director_id group by director_id order by count(name) desc limit 1')
mstNum = cur.fetchall()
print("\nMost no of movies are made by ", mstNum[0][0])

#11 Find out Director who is most bankable
cur.execute('Select directors.name from directors join movies where directors.id = movies.director_id group by directors.id order by sum(revenue) desc limit 1')
bankable = cur.fetchall()
print("\nMost bankable director is ", bankable[0][0])

#12 Find high budget movies
cur.execute('Select original_title from movies order by budget desc limit 10')
highBudget = cur.fetchall()
print("\nTop 10 high budget movies are ", highBudget)




























#
