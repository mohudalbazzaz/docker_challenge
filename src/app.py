from fastapi import FastAPI
import redis
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    db=0,
    decode_responses=True,
    socket_timeout=5,
    )

@app.get("/")
async def welcome():
    return "Welcome"

@app.get("/count")
async def visit_count():
    count = r.incr("visit_count")
    return {"visit_count": count}
