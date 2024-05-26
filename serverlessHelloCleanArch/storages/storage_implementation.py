from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from serverlessHelloCleanArch.constants.enums import MessageType
from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO
from serverlessHelloCleanArch.interactors.storages.storage_interface import (
    StorageInterface,
)
from serverlessHelloCleanArch.models.Message import Message


class StorageImplementation(StorageInterface):
    def get_session(self) -> Session:
        # database_url ="postgresql+psycopg2://postgres:N]2j$zati:qf7U9@cleanarch.c7kui26ientd.ap-south-1.rds.amazonaws.com:5432/clean_arch_hello"
        database_url = "postgresql+psycopg2://postgres:somePassword@localhost:5432/clean_arch_hello"
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

    def _get_message_dto(self, message: Message) -> MessageDTO:
        return MessageDTO(
            id=message.id,
            text=message.text,
            created_at=message.created_at,
            message_type=message.message_type,
        )
