from app.agents.intent_extractor import extract_intent
from app.agents.system_designer import design_system
from app.agents.schema_generator import generate_schema

from app.repair.repair_engine import repair_json
from app.validator.validator import validate_json
from app.validator.consistency_checker import check_consistency

from app.runtime.executor import execute
from app.metrics.logger import Metrics


# Start Metrics
metrics = Metrics()

# User Input
user_prompt = """
Build a CRM with login, contacts, dashboard and payments
"""

# Stage 1 - Intent Extraction
intent = extract_intent(user_prompt)

print("\n===== INTENT =====")
print(intent)

# Stage 2 - System Design
system_design = design_system(intent)

print("\n===== SYSTEM DESIGN =====")
print(system_design)

# Stage 3 - Schema Generation
schema = generate_schema(system_design)

print("\n===== GENERATED SCHEMA =====")
print(schema)

# Stage 4 - Repair Engine
schema = repair_json(schema)

# Stage 5 - Validation
if validate_json(schema):

    print("\nVALID JSON")

    # Stage 6 - Consistency Check
    issues = check_consistency(schema)

    print("\n===== CONSISTENCY CHECK =====")

    if len(issues) == 0:
        print("PASS")
    else:
        print("ISSUES FOUND:")
        for issue in issues:
            print("-", issue)

    # Stage 7 - Execution
    execute(schema)

    # Stage 8 - Save Generated Schema
    with open("output/generated_schema.json", "w", encoding="utf-8") as f:
        f.write(schema)

    print("\nSchema saved to output/generated_schema.json")

else:

    print("\nINVALID JSON")

# Stage 9 - Metrics
metrics.report()