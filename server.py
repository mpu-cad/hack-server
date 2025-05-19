from fastapi import FastAPI
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio

app = FastAPI()
executor = ThreadPoolExecutor(max_workers=200)  # Пул на 200 потоков

@app.post("/compute")
async def compute():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, time.sleep, 0.01)  # Не блокируем event loop
    return {"result": "ok"}