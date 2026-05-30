from app.agents.llm_client import generate_response

def design_system(intent_json):

    prompt = f"""
You are a software architect.

Given this application intent:

{intent_json}

Generate ONLY valid JSON.

Schema:

{{
  "entities": [],
  "roles": [],
  "pages": []
}}

Return JSON only.
"""

    return generate_response(prompt)