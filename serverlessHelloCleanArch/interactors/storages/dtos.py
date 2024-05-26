from dataclasses import dataclass
from datetime import datetime

from serverlessHelloCleanArch.constants.enums import MessageType


@dataclass
class MessageDTO:
    id: str
    created_at: datetime
    text: str
    message_type: MessageType
