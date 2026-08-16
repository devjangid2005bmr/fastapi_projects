import sqlite3 
from fastapi import FastAPI 

app = FastAPI()
conn = sqlite3.connect("test.db" , check_same_thread=False)

curser = conn.cursor()

curser.execute("""
 
CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY , 
        title TEXT , 
        completed TEXT
    )              
    
""")

conn.commit()


@app.get("/")
def home():
    curser.execute("SELECT * FROM todos")

    todos = curser.fetchall()

    return todos