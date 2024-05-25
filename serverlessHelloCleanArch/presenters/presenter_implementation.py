import json
from typing import Dict

from serverlessHelloCleanArch.interactors.presenters.presenter_interface import (
    PresenterInterface,
)
from serverlessHelloCleanArch.interactors.storages.dtos import MessageDTO


class PresenterImplementation(PresenterInterface):
    def get_unknown_server_error_response_dict(self) -> Dict:
        response = {"statusCode": 500, "body": "server error"}
        return response

    def get_message_created_successfully_response_dict(
        self, message_dto: MessageDTO
    ) -> Dict:
        response_body = self._get_message_response_dict(
            message_dto=message_dto
        )
        response = {"statusCode": 200, "body": json.dumps(response_body)}

        return response

    def _get_message_response_dict(self, message_dto: MessageDTO) -> Dict:
        return {
            "id": message_dto.id,
            "text": message_dto.text,
            "created_at": str(message_dto.created_at),
        }
