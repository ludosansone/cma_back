from fastapi import APIRouter, HTTPException
from typing import List
from ..models.instrument_model import Instrument
from ..services.instrument_service import InstrumentService

router = APIRouter()
instrument_service = InstrumentService()

@router.get("/instrument", response_model=List[Instrument])
async def get_all_instruments():
    return instrument_service.get_all_instruments()

@router.get("/instrument/{instrument_id}", response_model=Instrument)
async def get_instrument_by_id(instrument_id: int):
    instrument = instrument_service.get_instrument_by_id(instrument_id)
    if instrument is None:
        raise HTTPException(status_code=404, detail="Instrument not found")
    return instrument
