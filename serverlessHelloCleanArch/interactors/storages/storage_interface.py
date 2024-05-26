from abc import ABC, abstractmethod

from serverlessHelloCleanArch.constants.enums import MessageType
from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO


class StorageInterface(ABC):
    @abstractmethod
    def create_message(
        self, text: str, message_type: MessageType
    ) -> MessageDTO:
        pass
