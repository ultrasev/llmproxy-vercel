#!/usr/bin/env python3
from public.usage import USAGE as html
from api.hello import router as hello_router
from fastapi import FastAPI
from fastapi.responses import Response
from api.servers.generic import router as generic_router
from api.servers.gemini import router as gemini_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(hello_router, prefix="/hello")
app.include_router(gemini_router, prefix="/gemini")
app.include_router(generic_router, prefix="")  # put generic last

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # this is needed for streaming data header to be read by the client
    expose_headers=["X-Experimental-Stream-Data"],
)


@app.get("/")
def _root():
    return Response(content=html, media_type="text/html")
