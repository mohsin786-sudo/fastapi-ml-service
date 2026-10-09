from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import get_connection
import numpy as np
import joblib

app = FastAPI(title="ML Prediction Service")

model = joblib.load("model.pkl")


class PredictionInput(BaseModel):
    input_value: float = Field(..., description="Value for prediction")


@app.get("/")
def home():
    return {"message": "ML Prediction Service is running"}


@app.post("/predict")
def predict(data: PredictionInput):
    input_value = data.input_value

    predicted_value = float(
        model.predict(np.array([[input_value]]))[0]
    )

    try:
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO predictions (input_value, predicted_value)
                    VALUES (%s, %s)
                    RETURNING id, input_value, predicted_value, created_at;
                    """,
                    (input_value, predicted_value)
                )

                result = cur.fetchone()

            conn.commit()

            return {
                "id": result[0],
                "input_value": result[1],
                "predicted_value": result[2],
                "created_at": result[3].isoformat()
            }

        finally:
            conn.close()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Prediction could not be saved to the database."
        ) from e


@app.get("/predictions")
def get_predictions():
    try:
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, input_value, predicted_value, created_at
                    FROM predictions
                    ORDER BY id DESC;
                """)

                rows = cur.fetchall()

            return [
                {
                    "id": row[0],
                    "input_value": row[1],
                    "predicted_value": row[2],
                    "created_at": row[3].isoformat()
                }
                for row in rows
            ]

        finally:
            conn.close()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Could not retrieve predictions from the database."
        ) from  e
