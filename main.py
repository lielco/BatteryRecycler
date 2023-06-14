import uvicorn

if __name__ == "_main_":
    uvicorn.run(app="app:app", host="127.0.0.1", port="8000")