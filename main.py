from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

app = FastAPI()

class EnterprisePayload(BaseModel):
    client_name: str
    agent_action: str
    payload_data: dict
    status: str

@app.get("/")
def home():
    return {"status": "Enterprise AI Brain is online and running smoothly!"}

@app.post("/webhook-receiver")
async def receive_data(data: EnterprisePayload):
    print(f"Received data for client: {data.client_name}")
    return {
        "status": "success",
        "message": "Data successfully processed by Python AI Brain",
        "received_client": data.client_name
    }
