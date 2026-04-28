from pydantic import BaseModel
from datetime import datetime

class SymptomeCreate(BaseModel):
    user_id: str
    toux: bool
    respiration_difficile: bool
    headacke: bool
    caugh :bool
    fatigue: bool
    date: datetime = datetime.utcnow()

   