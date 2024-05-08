from fastapi import FastAPI


#1234 
app = FastAPI()

@app.get("/")
async def test_root():
    return {"Hello":"world"}

