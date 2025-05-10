## Caldera API

This project is a FastAPI service that exposes an endpoint to track the change in artifact size between GitHub releases, using Apache Airflow as an example repository.

## 🚀 API Overview

**Endpoint:**
```
GET /apache/airflow/bloat?start=v<start_version>&end=v<end_version>
```

**Example:**
```
curl "http://localhost:8000/apache/airflow/bloat?start=v2.8.3&end=v2.9.2"
```

**Response format:**
```json
{
  "deltas": [
    {"previous_tag": "2.8.2", "tag": "2.8.3", "delta": 1.00006},
    {"previous_tag": "2.8.3", "tag": "2.8.4", "delta": 0.99999},
    ...
  ]
}
```

## 📦 Setup Instructions

### 1. Clone the Repo
```bash
git clone <this-repo-url>
cd caldera_api
```

### 2. Create a Virtual Environment (optional)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the API Server Locally
```bash
uvicorn app.main:app --reload
```
Then visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API docs.

## 🐳 Docker Instructions

### Build the Docker Image
```bash
docker build -t yourusername/caldera-api .
```

### Run the Docker Container
```bash
docker run -p 8000:80 yourusername/caldera-api
```

### Push to Docker Hub
```bash
docker login
docker tag yourusername/caldera-api yourusername/caldera-api:latest
docker push yourusername/caldera-api:latest
```

## 🔐 Notes
- The GitHub API used allows 60 unauthenticated requests per hour. To increase limits, use a GitHub token with authentication.
