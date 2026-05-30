from app.agents.llm_client import generate_response

def generate_schema(system_design):

    prompt = f"""
You are a software architect.

Given this system design:

{system_design}

Generate ONLY valid JSON.

Schema:

{{
  "ui_schema": {{
    "pages": []
  }},
  "api_schema": {{
    "endpoints": []
  }},
  "db_schema": {{
    "tables": []
  }},
  "auth_rules": {{
    "roles": []
  }}
}}

Return JSON only.
"""

    return generate_response(prompt)