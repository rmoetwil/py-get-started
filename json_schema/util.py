import json
import logging

import jsonschema
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from jsonschema import FormatChecker


def load_schema(path):
    with open(path, "r") as schema_file:
        return json.loads(schema_file.read())


def load_schemas():
    schemas = {}

    for file in sorted(os.listdir(__location__)):
        if file.endswith(".schema"):
            schema = load_schema(os.path.join(__location__, file))

            schemas[file.split(".")[0]] = schema

    return schemas


def validate_json(json_message):
    schemas = load_schemas()

    validator = jsonschema.Draft7Validator(schemas["example"], format_checker=FormatChecker())

    errors = validator.iter_errors(json_message)

    for error in errors:
        logging.warning('{}'.format(error))

    return validator.is_valid(json_message)
