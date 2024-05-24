from abc import ABC
from abc import abstractmethod

from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO


class StorageInterface(ABC):
    @abstractmethod
    def create_message(self, text:str) -> MessageDTO:
        pass