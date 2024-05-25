from dataclasses import dataclass
from datetime import datetime


@dataclass
class MessageDTO:
    id: str
    created_at: datetime
    text: str
