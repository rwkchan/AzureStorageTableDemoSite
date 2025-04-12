from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/jobs")
def get_jobs():
    return {"jobs": ["Job1", "Job2", "Job3"]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)