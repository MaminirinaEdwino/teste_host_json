from fastapi import FastAPI
import json
app = FastAPI()
@app.get("/")
async def teste_function():
    return {"msg" : "api ok"}

@app.get("/create_file")
def create_file():
    with open('file.json', 'w') as file:
        json.dump(file, '["teste"]')