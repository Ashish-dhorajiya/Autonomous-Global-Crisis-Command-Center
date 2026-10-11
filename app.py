"""
AegisGlobal AI - Core Server & Swarm Orchestrator
FastAPI Backend serving the 3D Geopolitical Command Deck & Swarm Engine.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from simulation_data import GLOBAL_PORTS, GLOBAL_CHOKEPOINTS, ACTIVE_FLEET, CRISIS_PRESETS
from agents import MultiAgentCrisisCoordinator

app = FastAPI(
    title="AegisGlobal AI - Autonomous Geopolitical Command Deck",
    version="1.0.0",
    description="Multi-Agent Maritime & Supply Chain Crisis Simulation Engine"
)

# Enable CORS for local cross-origin development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Multi-Agent Coordinator
coordinator = MultiAgentCrisisCoordinator()

class CrisisRequest(BaseModel):
    preset_id: Optional[str] = None
    custom_prompt: Optional[str] = None

@app.get("/api/initial-state")
def get_initial_state():
    """Returns ports, chokepoints, active fleet, and preset crises."""
    return {
        "ports": GLOBAL_PORTS,
        "chokepoints": GLOBAL_CHOKEPOINTS,
        "fleet": ACTIVE_FLEET,
        "presets": CRISIS_PRESETS
    }

@app.post("/api/simulate-crisis")
def simulate_crisis(req: CrisisRequest):
    """Executes the 4-Agent Swarm against a preset or custom crisis."""
    target_crisis = None

    if req.preset_id:
        for p in CRISIS_PRESETS:
            if p["id"] == req.preset_id:
                target_crisis = p
                break

    if not target_crisis and req.custom_prompt:
        # Construct dynamic crisis from natural language prompt
        prompt_lower = req.custom_prompt.lower()
        if "suez" in prompt_lower or "egypt" in prompt_lower:
            chokepoint = "Suez Canal"
            lat, lng = 30.5852, 32.2654
        elif "arabian" in prompt_lower or "cyclone" in prompt_lower or "mumbai" in prompt_lower:
            chokepoint = "Bab-el-Mandeb Strait"
            lat, lng = 16.5000, 63.5000
        elif "taiwan" in prompt_lower or "china" in prompt_lower:
            chokepoint = "Taiwan Strait"
            lat, lng = 24.5000, 119.8000
        elif "panama" in prompt_lower:
            chokepoint = "Panama Canal"
            lat, lng = 9.0800, -79.6800
        elif "hormuz" in prompt_lower or "oil" in prompt_lower or "iran" in prompt_lower:
            chokepoint = "Strait of Hormuz"
            lat, lng = 26.5667, 56.2500
        else:
            chokepoint = "Bab-el-Mandeb Strait"
            lat, lng = 12.5833, 43.3333

        target_crisis = {
            "id": "custom_user_incident",
            "title": f"Live Incident: {req.custom_prompt[:60]}...",
            "chokepoint": chokepoint,
            "severity": "CRITICAL - MULTI-AGENT SWARM ACTIVE",
            "lat": lat,
            "lng": lng,
            "radius_km": 650,
            "description": req.custom_prompt,
            "affected_vessels": ["VSL-701", "VSL-804", "VSL-319"]
        }

    if not target_crisis:
        # Default to first preset
        target_crisis = CRISIS_PRESETS[0]

    # Execute Swarm
    result = coordinator.execute_crisis_swarm(target_crisis)
    return JSONResponse(content=result)

# Ensure static directory exists
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def serve_index():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "AegisGlobal AI Backend Running. Frontend is compiling..."}

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("  [*] AegisGlobal AI - 3D Autonomous Crisis Command Deck")
    print("  [*] System live at: http://127.0.0.1:8000")
    print("="*60 + "\n")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
