import uvicorn
from generate import generate
from agent import Agent, CodeGenAgent, ValidationAgent, CleanupAgent
from fastapi import FastAPI

app = FastAPI()

@app.post("/generate/")
async def generate_text(codeGenAgent: CodeGenAgent):
    code = generate(codeGenAgent)

    cleanupAgent = CleanupAgent(prompt = code)
    clean_up_code = generate(cleanupAgent)

    code = generate(codeGenAgent)
    validationAgent = ValidationAgent(prompt = codeGenAgent.prompt + "\n" + clean_up_code)
    validation = generate(validationAgent)

    return {"response": clean_up_code + "\n" + validation}

