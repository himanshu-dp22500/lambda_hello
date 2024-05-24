from datetime import datetime
from dataclasses import dataclass

@dataclass
class MessageDTO:
    id: str
    created_at: datetime
    text: str