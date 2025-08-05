import sqlite3

DB_FILE = "learning_app.db"

# --- Funciones de Usuario ---
def create_user(username: str, hashed_password: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

def get_user_by_username(username: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, hashed_password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# --- Funciones de Historial ---
def add_topic_to_history(username: str, topic: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO learning_history (user_id, topic) VALUES (?, ?)", (username, topic))
    conn.commit()
    conn.close()

def get_user_history(username: str) -> list:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT topic FROM learning_history WHERE user_id = ? ORDER BY learned_at DESC", (username,))
    temas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return temas

# --- Funciones de Conocimiento (RAG) ---
def get_knowledge_by_topic(topic_key: str) -> str | None:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM knowledge_articles WHERE topic = ?", (topic_key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
