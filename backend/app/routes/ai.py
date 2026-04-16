from fastapi import APIRouter, HTTPException
import random
import os
from groq import Groq
from ..schemas.schemas import AIResponse, ChatRequest
from ..core.config import settings
from ..core.constants import AI_SYSTEM_PROMPT_IDEA_GEN, AI_SYSTEM_PROMPT_CHAT

router = APIRouter(prefix="/ai", tags=["ai"])

# Fallback ideas in case AI is unavailable
MOCK_IDEAS = [
    {
        "title": "AI-Powered Personal Chef",
        "description": "An app that generates recipes based on what's in your fridge using computer vision and suggests nutrition-balanced meals."
    },
    {
        "title": "Eco-Tracker Marketplace",
        "description": "A platform where users can track their carbon footprint and earn tokens to spend on sustainable products."
    },
    {
        "title": "Virtual Study Hall",
        "description": "A 24/7 moderated space for students to co-work with productivity features and peer tutoring integration."
    },
    {
        "title": "Skill-Swap Network",
        "description": "A local community platform for exchanging services (e.g., plumbing for piano lessons) without using money."
    }
]

if settings.GROQ_API_KEY:
    try:
        # Explicitly ignore proxies to avoid 'unexpected keyword argument proxies' 
        # which can happen when httpx is used in certain restricted environments.
        client = Groq(
            api_key=settings.GROQ_API_KEY,
        )
    except Exception as e:
        # Fallback for older versions or environment-specific proxy issues
        try:
            import httpx
            http_client = httpx.Client(proxies={})
            client = Groq(api_key=settings.GROQ_API_KEY, http_client=http_client)
        except Exception as e2:
            print(f"FAILED TO INITIALIZE GROQ: {e2}")
            client = None

@router.get("/generate", response_model=AIResponse)
async def generate_idea():
    if not client:
        return random.choice(MOCK_IDEAS)
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": AI_SYSTEM_PROMPT_IDEA_GEN},
                {"role": "user", "content": "Generate a new startup idea."}
            ],
            response_format={"type": "json_object"}
        )
        import json
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        print(f"Groq API error: {e}")
        return random.choice(MOCK_IDEAS)

@router.post("/chat")
async def ai_chat(request: ChatRequest):
    if not client:
        return {"response": "AI is currently resting. Try again later or check your API key configuration."}
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": AI_SYSTEM_PROMPT_CHAT},
                {"role": "user", "content": request.message}
            ]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        print(f"Groq API error: {e}")
        return {"response": "I'm having trouble connecting to my brain right now. Please try again in a moment."}

