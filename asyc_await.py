import time
import asyncio
from fastapi import FastAPI


app = FastAPI()


"""async def task():
    await asyncio.sleep(3)
    return "done" 
"""

@app.get("/task")
async def task():
    await asyncio.sleep(3)
    return{
        "message":"successfully loaded"
    }