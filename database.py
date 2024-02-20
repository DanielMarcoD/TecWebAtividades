import sqlite3
from dataclasses import dataclass
class Database():
    def __init__(self,nome):
        self.conn = sqlite3.connect(nome + '.db')
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS note (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            content TEXT NOT NULL
                            )''')
        self.conn.commit()
    def add(self,note):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO note (title,content) VALUES (?,?)', (note.title, note.content))
        self.conn.commit()
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        notas = []
        for linha in cursor:
            id, title, content = linha
            notas.append(Note(id=id, title=title, content=content))
        return notas
    def update(self,entry):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE note SET title = ?, content = ? WHERE id = ?", (entry.title,entry.content,entry.id))
        self.conn.commit()
    def delete(self,note_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))
        self.conn.commit()

   
       

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''        
       
      
       
   

     
