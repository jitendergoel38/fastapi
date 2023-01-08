from fastapi import FastAPI

app = FastAPI()

@app.get("/")  #route/url/path  -------- get/post/put/patch/delete/
def root():
    return {"message":"Hello Goel!"}