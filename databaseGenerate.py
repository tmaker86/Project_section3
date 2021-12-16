import pandas as pd
import sqlite3
import os

data = pd.read_csv (r'./heart.csv')   
df = pd.DataFrame(data)

conn = sqlite3.connect("heartData.db")

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS heart_data(id INTEGER PRIMARY KEY AUTOINCREMENT, Age INT, Sex TEXT, ChestPainType TEXT, RestingBP INT, Cholesterol INT, FastingBS INT, RestingECG TEXT, MaxHR INT, ExerciseAngina TEXT, Oldpeak INT, ST_Slope TEXT, HeartDisease INT)')



cnt = 0
for row in df.itertuples():
    cur.execute('''
                INSERT INTO heart_data(Age , Sex , ChestPainType , RestingBP , Cholesterol , FastingBS , RestingECG , MaxHR, ExerciseAngina , Oldpeak , ST_Slope , HeartDisease )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row[1:]
                )
    cnt = cnt + 1
conn.commit()