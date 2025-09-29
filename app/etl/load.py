from transform import get_usuarios_df, get_posts_df
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).parent.parent / "db"
DB_PATH = BASE_DIR / "userpost.db"

def get_connection():
    """
    Retorna una nueva conexión a la base de datos.
    """
    return sqlite3.connect(DB_PATH)

def load_usuarios():
    """
    Carga datos en la tabla users de la bd
    """
    conn = get_connection()
    query = "INSERT OR REPLACE INTO users VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
    
    for usuario in get_usuarios_df().itertuples():
        conn.execute(query,(usuario.id, usuario.name, usuario.username, usuario.email, usuario.address, usuario.zipcode, usuario.geo, usuario.phone, usuario.website, usuario.company_name, usuario.company_carchPhase, usuario.company_bs))
        
    conn.commit()
    conn.close()

def load_posts():
    """
    Carga datos en la tabla posts de la bd
    """
    print(get_posts_df().columns)
    conn = get_connection()
    query = "INSERT OR REPLACE INTO posts VALUES(?,?,?,?)"
    
    for posts in get_posts_df().itertuples():
        conn.execute(query,(posts.id, posts.userId, posts.title, posts.body))
        
    conn.commit()
    conn.close() 

# load_usuarios()
# load_posts()