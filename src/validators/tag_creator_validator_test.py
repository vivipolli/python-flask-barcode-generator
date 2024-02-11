from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockResponse:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    req = MockResponse(json={ "product_code": "1234" })
    tag_creator_validator(req)

def test_tag_creator_validator_error():
    req = MockResponse(json={ "product_code": 1235 })

    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
  