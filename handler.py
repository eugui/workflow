import os, json

SCENARIO = os.environ.get("SCENARIO", "yaml_unsafe")

def _mod(name):
    return __import__(f"scenarios.{name}", fromlist=["run"])

def lambda_handler(event, context):
    try:
        mod = _mod(SCENARIO)
    except Exception as e:
        return {"error": f"unknown scenario '{SCENARIO}'", "detail": str(e)}
    try:
        return {"scenario": SCENARIO, "result": mod.run(event or {})}
    except Exception as e:
        return {"scenario": SCENARIO, "error": str(e)}
