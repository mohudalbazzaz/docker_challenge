from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(
    host="localhost",
    port=6379,
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
