import json

def normalize(name):
    return name.lower().rstrip("s")

def check_consistency(schema_json):

    data = json.loads(schema_json)

    issues = []

    db_tables = []

    for table in data["db_schema"]["tables"]:
        db_tables.append(
            normalize(table["name"])
        )

    for endpoint in data["api_schema"]["endpoints"]:

        path = endpoint["path"].lower()

        if "/contacts" in path:
            if "contact" not in db_tables:
                issues.append(
                    "Contacts endpoint has no matching table"
                )

        if "/payments" in path:
            if "payment" not in db_tables:
                issues.append(
                    "Payments endpoint has no matching table"
                )

        if "/users" in path:
            if "user" not in db_tables:
                issues.append(
                    "Users endpoint has no matching table"
                )

    return issues