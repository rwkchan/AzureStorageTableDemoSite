import datetime
from time import timezone
import uuid
from fastapi import FastAPI
import uvicorn
from azure.data.tables.aio import TableServiceClient
from azure.core.exceptions import ResourceNotFoundError
from pydantic import BaseModel
import os

app = FastAPI()

# Define a Pydantic model for the job entity
class Job(BaseModel):
    job_id: str
    job_name: str

# Azure Storage Table connection string
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
#print("Connection string: ", connection_string)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/jobs")
async def get_jobs():
    try:
        # Create a TableServiceClient
        table_service = TableServiceClient.from_connection_string(conn_str=connection_string)

        # Get a reference to the table
        table_client = table_service.get_table_client(table_name="Jobs")

        # Query entities from the table with pagination
        entities = []
        async for entity in table_client.list_entities():
            entities.append(entity)

        return {"jobs": entities}
    except ResourceNotFoundError:
        return {"error": "Table not found."}
    except Exception as e:
        return {"error": str(e)}

@app.post("/job")
async def add_job(name: str):
    try:
        # Create a TableServiceClient
        table_service = TableServiceClient.from_connection_string(conn_str=connection_string)

        # Get a reference to the table (create it if it doesn't exist)
        table_client = table_service.get_table_client(table_name="Jobs")
        await table_client.create_table_if_not_exists()

        # Add the job entity to the table
        jobStartTime = datetime.now(timezone.utc)
        entity = {
            "PartitionKey": str(jobStartTime.seconds),
            "RowKey": str(uuid.uuid4()),
            "JobName": name
        }
        await table_client.create_entity(entity=entity)

        return {"message": "Job added successfully!"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)