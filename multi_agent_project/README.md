# Multi-Agent FastAPI Project

This project demonstrates a modular FastAPI application with multiple agents and tools.

## Structure
- `agents/`: Contains agent classes (e.g., support, dashboard)
- `tools/`: Contains utility/tool classes (e.g., MongoDB, external API)
- `data/`: Mock data for collections
- `api/`: API route definitions
- `schemas/`: Pydantic models
- `main.py`: FastAPI entrypoint

## Running the App
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Visit [http://localhost:8000](http://localhost:8000)

## Example Endpoints
- `/support/{ticket}`
- `/dashboard/{data}`

---

This is a minimal example. Extend agents, tools, and models as needed.
