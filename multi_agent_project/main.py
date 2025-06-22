from fastapi import FastAPI, Request
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.support_agent_crewai import run_support_task
from agents.dashboard_agent_crewai import run_dashboard_task
from utils.translator import translate_prompt_to_english

app = FastAPI()

@app.post("/support")
async def support(request: Request):
    data = await request.json()
    prompt = translate_prompt_to_english(data.get("prompt", ""))
    value = run_support_task(prompt)
    return {"response": value}

@app.post("/dashboard")
async def dashboard(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    value = run_dashboard_task(prompt)
    return {"result": value}
