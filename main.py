import uvicorn
from fastapi import FastAPI
from routers.addresses import router as addresses_router


app = FastAPI()

app.include_router(addresses_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)
