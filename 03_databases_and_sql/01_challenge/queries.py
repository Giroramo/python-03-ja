
# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# アーティストの数
def number_of_artists(db):
    query = "SELECT COUNT(*) FROM artists;"
    db.execute(query)
    results = db.fetchone()[0]  # ここで数値を直接取得
    return results

# アーティストのリスト
def list_of_artists(db):
    query = "SELECT Name FROM artists;" 
    db.execute(query)
    results =  [row[0] for row in db.fetchall()]
    return results

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    query = "SELECT Title FROM albums WHERE Title LIKE '%love%';" 
    db.execute(query)
    results = [row[0] for row in db.fetchall()]
    return results

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = "SELECT COUNT(*) FROM tracks WHERE Milliseconds > ?;"  
    db.execute(query, (duration,))
    results = db.fetchone()[0]  # ここで数値を直接取得
    return results

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = """
    SELECT genres.name, COUNT(tracks.TrackId) as track_count
    FROM genres
    JOIN tracks ON genres.GenreId = tracks.GenreId
    GROUP BY genres.name
    ORDER BY track_count DESC;
    """
    db.execute(query)
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()
