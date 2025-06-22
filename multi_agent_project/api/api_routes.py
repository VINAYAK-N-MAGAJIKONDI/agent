from fastapi import APIRouter, Request
from agents.support_agent_crewai import run_support_task
from agents.dashboard_agent_crewai import run_dashboard_task
from utils.translator import translate_prompt_to_english

router = APIRouter()

@router.post("/support")
async def support_handler(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")


    translated_prompt = translate_prompt_to_english(prompt)

    response = run_support_task(translated_prompt)
    return {"response": response}


@router.post("/dashboard")
async def dashboard_handler(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    
    response = run_dashboard_task(prompt)
    return {"response": response}
