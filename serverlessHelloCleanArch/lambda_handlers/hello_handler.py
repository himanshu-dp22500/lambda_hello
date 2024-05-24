import json

def hello_lambda_handler(event, context):
    print("Request Body: ", event)
    body = event["body"]

    from serverlessHelloCleanArch.interactors.hello import HelloInteractor
    from serverlessHelloCleanArch.storages.storage_implementation import StorageImplementation
    from serverlessHelloCleanArch.presenters.presenter_implementation import PresenterImplementation

    storage = StorageImplementation()
    interactor = HelloInteractor(storage=storage)
    response = {"statusCode": 200, "body": json.dumps(body)}
    return interactor.hello_wrapper()
