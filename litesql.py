import sqlite3
from sqlite3 import Error, connect
from datetime import date

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"Error '{e}'")
    return connection

connection = create_connection("C:\\Users\\79522\\Desktop\\steam.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  age INTEGER,
  gender TEXT,
  email TEXT UNIQUE NOT NULL
);
"""
execute_query(connection, create_users_table)

create_games_table = """
CREATE TABLE IF NOT EXISTS games (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tittle TEXT NOT NULL,
  genre TEXT,
  date DATE NOT NULL,
  author TEXT NOT NULL
);
"""
execute_query(connection, create_games_table)
create_ratings_table = """
CREATE TABLE IF NOT EXISTS ratings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  player_id INTEGER NOT NULL,
  game_id INTEGER NOT NULL,
  rating INTEGER CHECK(rating BETWEEN 1 AND 10) NOT NULL,
  date DATE NOT NULL,
  FOREIGN KEY (player_id) REFERENCES users(id),
  FOREIGN KEY (game_id) REFERENCES games(id)
);
"""
execute_query(connection, create_ratings_table)
create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  player_id INTEGER NOT NULL,
  game_id INTEGER NOT NULL,
  date DATE NOT NULL,
  comment TEXT NOT NULL,
  FOREIGN KEY (player_id) REFERENCES users(id),
  FOREIGN KEY (game_id) REFERENCES games(id)
);
"""
execute_query(connection, create_comments_table)

create_users= """
INSERT INTO
  users (username, age, gender, email)
VALUES
  ('Hatsune_Miku', 23 , 'female', 'pochta@yandex.ru'),
  ('LegoshiTop228', 19 , 'female', 'Odas@gmail.com'),
  ('proGamer', 14 , 'male', 'asdaf@yandex.ru'),
  ('casssssss', 20 , 'female', 'fasfa@gmail.com'),
  ('good_jamperr', 30 , 'female', 'fsafaf@gmail.com'),
  ('kodaka', 30 , 'male', 'jyj@yandex.ru');
"""
execute_query(connection, create_users)

create_games = """
INSERT INTO
  games (tittle, genre, date, author)
VALUES
  ('Danganronpa 2: Goodbye Dispair', 'visual novel', '2012-7-26' , 'Kazutaka Kodaka'),
  ('Baldurs gate 3', 'RPG', '2023-08-03' , 'Larian Studio'),
  ('The Elder Scrolls V: Skyrim', 'RPG', '2010-12-11', 'Bethesda Softworks'),
  ('Danganronpa 1: Trigger Happy Havoc', 'visual novel', '2010-11-25', 'Kazutaka Kodaka'),
  ('The Witcher 3: Wild Hunt', 'RPG', '2023-07-19', 'CD Projekt RED'),
  ('Brawl Stars', 'MOBA', '2018-12-12', 'Supercell');
"""
execute_query(connection, create_games)
create_comments = """
INSERT INTO
  comments (player_id, game_id, date, comment)
VALUES
  (4, 1, '2024-11-30', 'Super game!!!!! I love it!'),
  (1, 2, '2024-10-02', 'Astarion is top!'),
  (3, 3, '2024-09-15', 'It was...boring'),
  (6, 3, '2024-01-01', 'Players are very bad.'),
  (2, 5, '2024-06-16', 'Best game 4ever'),
  (2, 2, '2024-06-16', 'Best game 4ever'),
  (2, 5, '2024-06-16', 'Danganronpa 2: Goodbye Dispair');
"""
execute_query(connection, create_comments)

create_ratings = """
INSERT INTO
  ratings (player_id, game_id, rating, date)
VALUES
  (4, 1, 10, '2024-11-30'),
  (1, 2, 9, '2024-10-02'),
  (3, 3, 3, '2024-09-15'),
  (6, 3, 1, '2024-01-01'),
  (2, 5, 8, '2024-06-16');
"""

execute_query(connection, create_ratings)


#добавление по одной новой записи

create_user = """
INSERT INTO
  users (username, age, gender, email)
VALUES
  ('nicejumper', 14 , 'female', 'error@yandex.ru');
"""
execute_query(connection, create_user)

create_game = """
INSERT INTO
  games (tittle, genre, date, author)
VALUES
  ('Sally Face', 'horror', '2016-01-21', 'Portable Moose');
"""
execute_query(connection, create_game)
create_comment = """
INSERT INTO
  comments (player_id, game_id, date, comment)
VALUES
  (7, 7, '2024-06-22', 'Super!!!');
"""
execute_query(connection, create_comment)

create_rating = """
INSERT INTO
  ratings (player_id, game_id, rating, date)
VALUES
  (4, 7, 9, '2024-11-16');
"""
execute_query(connection, create_rating)

#вывод всего содержимого таблицы
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_games = "SELECT * from games"
games = execute_read_query(connection, select_games)
for game in games:
    print(game)
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)
select_comments = "SELECT * from comments"
comments = execute_read_query(connection, select_comments)
for comment in comments:
    print(comment)
select_ratings = "SELECT * from ratings"
ratings = execute_read_query(connection, select_ratings)
for rating in ratings:
    print(rating)


#используем JOIN - ќбъедин€ем вывод двух таблиц
def printDescriptions(connection, name):
    cursor = connection.cursor()
    cursor.execute(name)
    cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(column_names)

select_games_rate_user = """
SELECT 
  users.id,
  users.username,
  games.tittle, 
  ratings.rating
FROM 
  ratings
  JOIN users ON ratings.player_id = users.id
  JOIN games ON ratings.game_id = games.id
"""
print("JOIN:")
printDescriptions(connection, select_games_rate_user)
temp_ = execute_read_query(connection, select_games_rate_user)

for t in temp_:
    print(t)

select_games_comment_user = """
SELECT 
  users.id,
  users.username,
  games.tittle, 
  comments.comment,
  comments.date
FROM 
  comments
  JOIN users ON comments.player_id = users.id
  JOIN games ON comments.game_id = games.id
"""
print("JOIN 2:")
t_ = execute_read_query(connection, select_games_comment_user)
printDescriptions(connection, select_games_comment_user)

for t in t_:
    print(t)

# WHERE

  
selected_with_where = """
SELECT
  games.tittle,
  games.genre,
  ratings.rating
FROM 
  ratings
  JOIN games ON ratings.game_id = games.id
  WHERE ratings.rating > 5
"""
t_ = execute_read_query(connection, selected_with_where)
print("WHERE:")
printDescriptions(connection, selected_with_where)
for t in t_:
    print(t)
    
selected_with_where = """
SELECT
  games.genre,
  AVG(ratings.rating)
  AS average_rating
FROM 
  ratings
  JOIN games ON ratings.game_id = games.id
  WHERE ratings.rating > 5
  GROUP BY games.genre
"""
#avg - средн€€ оценка дл€ каждой игры определенного жанра, avarage_rating - новое название столбца
t_ = execute_read_query(connection, selected_with_where)
print("WHERE and CROUP BY:")
printDescriptions(connection, selected_with_where)
for t in t_:
    print(t)
    
users_selected = """
SELECT * 
FROM users
WHERE id = (SELECT player_id FROM ratings WHERE rating = 9 LIMIT 1)
"""
t_ = execute_read_query(connection, users_selected)
print("SELECT WHERE (1):")
for t in t_:
    print(t)




games_selected = """
SELECT tittle
FROM games
WHERE id IN (SELECT game_id FROM ratings WHERE player_id = 4)
"""
print("SELECT WHERE (2):")
t_ = execute_read_query(connection, games_selected)
for t in t_:
    print(t)
#printDescriptions(connection, games_selected)

# UNION запросы
user_and_aouthor = """
SELECT username AS name FROM users
UNION
SELECT author AS name FROM games
"""
print("UNION (1):")
t_ = execute_read_query(connection, user_and_aouthor)
for t in t_:
    print(t)

title_and_comm = """
SELECT tittle AS info FROM games
UNION
SELECT comment AS info FROM comments
"""
print("UNION (2):")
t_ = execute_read_query(connection, title_and_comm)
for t in t_:
    print(t)
    
# DISTINCT запрос
age_selected= '''
SELECT DISTINCT age FROM users
'''
t_ = execute_read_query(connection, age_selected)

for t in t_:
    print(t)
# ќбновление записей
update_users = "UPDATE users SET age = 30 WHERE id = 1"
update_games = "UPDATE games SET genre = 'horror' WHERE id = 1"
execute_query(connection, update_users)
execute_query(connection, update_games)
print("Update.")

delete_users = "DELETE FROM users WHERE id = 1"
delete_games = "DELETE FROM games WHERE id = 3"
delete_ratings = "DELETE FROM ratings WHERE id = 4"
delete_comments = "DELETE FROM comments WHERE id = 2"
execute_query(connection, delete_users)
execute_query(connection, delete_games)
execute_query(connection, delete_ratings)
execute_query(connection, delete_comments)
print("Deleted specific records.")

delete_all_comments = "DELETE FROM comments"
execute_query(connection, delete_all_comments)
print("All comments are deleted.")
connection.close()
print("Connection closed.")