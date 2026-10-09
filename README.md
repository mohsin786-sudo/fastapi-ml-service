# FastAPI Machine Learning Prediction API

A machine learning web service built using FastAPI. It accepts input data, generates predictions using a trained ML model, and stores prediction records in a database.

## Features

* REST API built with FastAPI
* Machine learning predictions using a trained model
* Model loading using Joblib/Pickle
* Database integration
* Prediction history storage
* Automatic API documentation using Swagger UI

## Technologies Used

* Python
* FastAPI
* Scikit-learn
* NumPy
* SQLAlchemy
* SQLite / configured database
* Uvicorn

## Project Structure

```text
fastapi-ml-service/
├── main.py
├── model.py
├── model.pkl
├── train_model.py
├── database.py
├── create_table.py
├── db_test.py
├── .env
├── README.md
└── venv/
```

## Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fastapi-ml-service
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn scikit-learn joblib numpy sqlalchemy python-dotenv
```

### 4. Configure environment variables

Create a `.env` file and add the environment variables required by your application.

Never upload passwords, secret keys, or other sensitive values to GitHub.

### 5. Start the API

```bash
uvicorn main:app --reload
```

### 6. Open API documentation

Visit:

http://127.0.0.1:8000/docs

## Example Prediction

Input:

```json
{
  "input_value": 15
}
```

Example response:

```json
{
  "id": 3,
  "input_value": 15,
  "predicted_value": 30.000000000000007
}
```

The actual response depends on the model and database state.

## Future Improvements

* Deploy the API to a cloud platform
* Add automated tests
* Improve input validation and error handling
* Add monitoring and logging
