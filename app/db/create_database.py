from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "userpost.db"

def get_connection():
    """
    Retorna una nueva conexión a la base de datos.
    """
    return sqlite3.connect(DB_PATH)

def init_db():
    """
    Crea la BD y las tablas de 'users' y 'posts'.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name VARCHAR(30),
            username VARCHAR(20),
            email VARCHAR(50),
            address VARCHAR(100),
            zipcode VARCHAR(20),
            geo VARCHAR(100),
            phone VARCHAR(30),
            website VARCHAR(30),
            company_name VARCHAR(30),
            company_carchPhase VARCHAR(30),
            company_bs VARCHAR(30) 
        );
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            title VARCHAR(50),
            body VARCHAR(200),
            FOREIGN KEY (userId) REFERENCES users(id) ON DELETE CASCADE
        );
        """)
    
    conn.commit()
    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    init_db()