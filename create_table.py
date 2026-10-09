from database import get_connection

def create_table():
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS predictions (
                    id SERIAL PRIMARY KEY,
                    input_value FLOAT NOT NULL,
                    predicted_value FLOAT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

        conn.commit()
        print("Predictions table created successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    create_table()
