from fastapi import FastAPI
import time

app = FastAPI()

# Эмулируем сложное вычисление (1.5-2 секунды)
def heavy_computation():
    time.sleep(1.5 + 0.5 * (hash(str(time.time())) % 10) / 10)  # Рандомно 1.5-2 сек
    return {"result": "ok"}

@app.post("/compute")
async def compute():
    result = heavy_computation()
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)