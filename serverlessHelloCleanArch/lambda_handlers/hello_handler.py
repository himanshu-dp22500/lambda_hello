import json
from typing import Dict


def hello_lambda_handler(event, context):
    # print("Request Body: ", event)
    body = json.loads(event["body"])
    validate_body(body=body)

    from serverlessHelloCleanArch.interactors.hello import HelloInteractor
    from serverlessHelloCleanArch.presenters.presenter_implementation import (
        PresenterImplementation,
    )
    from serverlessHelloCleanArch.storages.storage_implementation import (
        StorageImplementation,
    )

    storage = StorageImplementation()
    interactor = HelloInteractor(storage=storage)
    presenter = PresenterImplementation()
    return interactor.hello_wrapper(
        text=body["body"]["text"], presenter=presenter
    )


def validate_body(body: Dict):
    required_keys = ["text"]
    received_keys = list(body.keys())

    missing_keys = [key for key in required_keys if key not in received_keys]

    if missing_keys:
        body = {"missing_keys": missing_keys}

        return {"statusCode": 200, "body": json.dumps(body)}


print(
    hello_lambda_handler(
        event={
            "body": '{\n    "body":{\n        "text":"Hello yo Himanshu again"\n    }\n}'
        },
        context="",
    )
)
