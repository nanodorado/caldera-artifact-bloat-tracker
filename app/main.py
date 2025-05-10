from fastapi import FastAPI, HTTPException
from app.github_utils import get_release_deltas

app = FastAPI()

@app.get("/apache/airflow/bloat")
def airflow_bloat(start: str, end: str):
    try:
        # Calculate the size deltas between two semantic versions of Apache Airflow releases
        deltas = get_release_deltas("apache", "airflow", start, end)
        return {"deltas": deltas}
    except Exception as e:
        # Return a 500 error with the exception message if something goes wrong
        raise HTTPException(status_code=500, detail=str(e))