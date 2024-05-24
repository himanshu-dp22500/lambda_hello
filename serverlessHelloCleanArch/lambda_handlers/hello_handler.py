import json
from typing import Dict


def hello_lambda_handler(event, context):
    print("Request Body: ", event)
    body = event["body"]
    validate_body(body=body)

    from serverlessHelloCleanArch.interactors.hello import HelloInteractor
    from serverlessHelloCleanArch.storages.storage_implementation import StorageImplementation
    from serverlessHelloCleanArch.presenters.presenter_implementation import PresenterImplementation

    storage = StorageImplementation()
    interactor = HelloInteractor(storage=storage)
    presenter = PresenterImplementation()

    return interactor.hello_wrapper(text=body["text"], presenter=presenter)

def validate_body(body:Dict):
    required_keys = ["text"]
    received_keys = list(body.keys())

    missing_keys = [
        key
        for key in required_keys
        if key not in received_keys
    ]

    if missing_keys:
        body = {
            "missing_keys":missing_keys
        }

        return {
            "statusCode": 200, "body": json.dumps(body)
        }