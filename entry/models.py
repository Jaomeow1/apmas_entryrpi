from pydantic import BaseModel
from typing import Optional

class VerifyPayload(BaseModel):
    plate_text_verified: str

class SlotStatusPayload(BaseModel):
    status:     str            # "free" | "occupied"
    plate_text: Optional[str] = None   # ป้ายที่ Pi5 OCR ได้

class TicketResponse(BaseModel):
    ticket_id:           str
    plate_text_raw:      Optional[str]
    plate_text_verified: Optional[str]
    time_in:             Optional[str]
    time_out:            Optional[str]
    slot_id:             Optional[str]
    status:              Optional[str]
    image_car_url:       Optional[str]
    image_plate_url:     Optional[str]
    qr_url:              Optional[str]
    source:              Optional[str]
