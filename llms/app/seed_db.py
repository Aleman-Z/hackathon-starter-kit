import sqlite3

DB_FILE = "learning_app.db"

# Define aquí los artículos para tu base de conocimiento
ARTICLES = [
    {
        "topic": "historia_de_roma",
        "title": "La Historia de la Antigua Roma",
        "content": "La Antigua Roma fue una de las civilizaciones más influyentes de la historia, comenzando como una pequeña aldea en la península itálica en el siglo VIII a.C. Se expandió para convertirse en un vasto imperio que dominó el Mediterráneo. Su legado incluye el derecho romano, la arquitectura monumental como el Coliseo, y la lengua latina."
    },
    {
        "topic": "agujeros_negros",
        "title": "Agujeros Negros",
        "content": "Un agujero negro es una región del espacio con una fuerza gravitatoria tan inmensa que nada, ni siquiera la luz, puede escapar de ella. Se forman cuando estrellas muy masivas colapsan al final de su ciclo de vida. La frontera de no retorno se llama horizonte de sucesos."
    }
]

def seed_knowledge_base():
    """
    Añade o actualiza los artículos en la tabla knowledge_articles.
    Se ejecuta manualmente cuando quieres añadir nuevo contenido.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for article in ARTICLES:
        cursor.execute("""
        INSERT OR REPLACE INTO knowledge_articles (topic, title, content)
        VALUES (?, ?, ?)
        """, (article["topic"], article["title"], article["content"]))
    
    conn.commit()
    conn.close()
    print(f"Se han añadido/actualizado {len(ARTICLES)} artículos en la base de conocimiento.")

if __name__ == "__main__":
    seed_knowledge_base()
