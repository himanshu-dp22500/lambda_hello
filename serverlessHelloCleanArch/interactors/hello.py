from typing import Dict

from serverlessHelloCleanArch.interactors.storages.storage_interface import StorageInterface


class HelloInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def hello_wrapper(self, text: str) -> Dict:
        pass

    def hello(self, text: str) -> Dict:
        pass
