from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO
from serverlessHelloCleanArch.interactors.storages.storage_interface import StorageInterface
from serverlessHelloCleanArch.models.Message import Message


class StorageImplementation(StorageInterface):
    def get_session(self) -> Session:
        import configparser

        # config = configparser.ConfigParser()
        # config.read('serverlessHelloCleanArch/alembic.ini')
        # database_url = config.get('alembic', 'sqlalchemy.url')
        database_url = "sqlite:///db.db"

        engine = create_engine(database_url)
        session = Session(bind=engine)

        return session

    def create_message(self, text:str) -> MessageDTO:
        session = self.get_session()
        new_message = Message(text=text)

        session.add(new_message)
        session.commit()

        return self._get_message_dto(message=new_message)

    def _get_message_dto(self,message: Message) -> MessageDTO:
        return MessageDTO(
            id=message.id,
            text=message.text,
            created_at=message.created_at
        )

