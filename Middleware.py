from fastapi import FastAPI , middleware , Request
import time

app = FastAPI()

@app.middleware("http")
async def middleware(request:Request,call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time()-start_time
    
    print(f"Path:{request.url.path} | Time: {process_time}")
    
    return response