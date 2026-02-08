# validator.py

from jsonschema import validate

def validate_output(data: dict, schema: dict):
    validate(instance=data, schema=schema)
