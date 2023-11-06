import os
from transformers import pipeline, set_seed
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM

# import redis
import json
# import zlib
# from typing import Dict

app = FastAPI(title="Model Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GPT2_MODEL = os.environ.get("GPT2_MODEL", "GPT2")
print(f"loading model {GPT2_MODEL=}...")
generator = pipeline('text-generation', model="gpt2")
print(f"loaded model {GPT2_MODEL=}")

def predict(text):
    op = generator(text, max_length=30, num_return_sequences=1)
    print(op)
    return op[0]

@app.post("/infer")
async def infer(text):
    predictions = predict(text)   
    return predictions['generated_text']
