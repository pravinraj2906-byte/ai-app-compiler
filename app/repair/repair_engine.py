from app.validator.json_cleaner import clean_json

def repair_json(response):

    repaired = clean_json(response)

    return repaired