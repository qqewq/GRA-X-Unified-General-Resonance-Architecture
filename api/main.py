from fastapi import FastAPI
from pydantic import BaseModel
from gra_math.nullification import Nullifier
from gra_swarm.consensus import Consensus

app = FastAPI()
nullifier = Nullifier()

class NullifyRequest(BaseModel):
    data: list[float]

@app.post("/nullify")
def nullify(req: NullifyRequest):
    result = nullifier.forward(req.data)
    return {"result": result.tolist()}

@app.get("/health")
def health():
    return {"status": "ok"}
