import json
import os

from json_schema.util import validate_json


def test_validate_json():
    assert validate_json(load_file_as_json('valid-example.json')) is True


def test_validate_json_empty_json():
    assert validate_json({}) is False


def test_validate_json_invalid_email():
    assert validate_json(load_file_as_json('invalid-email-example.json')) is False


def test_validate_json_invalid_group():
    assert validate_json(load_file_as_json('invalid-group-example.json')) is False


def load_file_as_json(json_file):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, json_file), "r") as file:
        return json.load(file)
