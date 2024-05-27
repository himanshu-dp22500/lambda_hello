from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from serverlessHelloCleanArch.constants.enums import MessageType
from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO
from serverlessHelloCleanArch.interactors.storages.storage_interface import (
    StorageInterface,
)
from serverlessHelloCleanArch.database.models.Message import Message


class StorageImplementation(StorageInterface):
    @staticmethod
    def get_session() -> Session:
        from serverlessHelloCleanArch.interactors.get_database_url import (
            GetDatabaseURLInteractor,
        )

        interactor = GetDatabaseURLInteractor()

        database_url = interactor.get_database_url()
        engine = create_engine(database_url)
        session = Session(bind=engine)

        return session

    def create_message(
        self, text: str, message_type: MessageType
    ) -> MessageDTO:
        session = self.get_session()
        new_message = Message(text=text, message_type=message_type)

        session.add(new_message)
        session.commit()

        return self._get_message_dto(message=new_message)

    @staticmethod
    def _get_message_dto(message: Message) -> MessageDTO:
        return MessageDTO(
            id=message.id,
            text=message.text,
            created_at=message.created_at,
            message_type=message.message_type,
        )

    def get_message(self, message_id:str) -> MessageDTO:
        pass
