import traceback
from typing import Dict

from serverlessHelloCleanArch.interactors.presenters.presenter_interface import \
    PresenterInterface
from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO
from serverlessHelloCleanArch.interactors.storages.storage_interface import \
    StorageInterface


class HelloInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def hello_wrapper(self, text: str, presenter:PresenterInterface) -> Dict:
        try:
            message_dto = self.hello(text=text)
        except Exception as e:
            print("An Error : ", e)
            traceback.print_exc()
            return presenter.get_unknown_server_error_response_dict()
        else:
            return presenter.get_message_created_successfully_response_dict(message_dto=message_dto)

    def hello(self, text: str) -> MessageDTO:
        message_dto = self.storage.create_message(text=text)
        return message_dto
