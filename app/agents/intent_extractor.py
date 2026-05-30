from app.agents.llm_client import generate_response
import json

def extract_intent(user_prompt):

    prompt = f"""
You are an AI system.

Convert the user's request into VALID JSON.

Return ONLY JSON.

Schema:

{{
  "app_type": "",
  "features": []
}}

User Request:
{user_prompt}
"""

    response = generate_response(prompt)

    return response