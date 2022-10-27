import uvicorn, json, os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

origins = [
    "*",
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/echo")
async def get_service(request: Request):
    r = await request.json()
    print("Processing text={}".format(r))
    return r    

@app.get("/")
async def root():
    return {"message": "Arcturus Echo Service"}
