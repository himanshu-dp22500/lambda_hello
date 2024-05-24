from abc import ABC
from abc import abstractmethod
from typing import Dict

from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO


class PresenterInterface(ABC):
    def get_unknown_server_error_response_dict(self) -> Dict:
        pass

    def get_message_created_successfully_response_dict(self, message_dto:MessageDTO) -> Dict:
        pass