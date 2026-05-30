import json

def execute(schema):

    data = json.loads(schema)

    print("\n===== EXECUTION REPORT =====")

    if "ui_schema" in data:
        print("UI Generated")

    if "api_schema" in data:
        print("API Generated")

    if "db_schema" in data:
        print("Database Generated")

    if "auth_rules" in data:
        print("Authentication Generated")