import json

def validate_json(json_text):

    try:
        json.loads(json_text)
        return True

    except Exception:
        return False