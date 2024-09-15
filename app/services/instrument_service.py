from typing import List, Optional
from ..models.instrument_model import Instrument

class InstrumentService:
    def __init__(self):
        self.instruments: List[Instrument] = [
            Instrument(id=1, nameKey="instrument.acoustic-guitar", category="string", icon="acoustic-guitar-icon"),
            Instrument(id=2, nameKey="instrument.electric-guitar", category="string", icon="electric-guitar-icon"),
            Instrument(id=3, nameKey="instrument.bass", category="string", icon="bass-icon"),
            Instrument(id=4, nameKey="instrument.drums", category="percussion", icon="drums-icon"),
            Instrument(id=5, nameKey="instrument.piano", category="keyboard", icon="piano-icon"),
            Instrument(id=6, nameKey="instrument.violin", category="string", icon="violin-icon"),
            Instrument(id=7, nameKey="instrument.saxophone", category="wind", icon="saxophone-icon"),
            Instrument(id=8, nameKey="instrument.trumpet", category="wind", icon="trumpet-icon"),
            Instrument(id=9, nameKey="instrument.flute", category="wind", icon="flute-icon"),
            Instrument(id=10, nameKey="instrument.cello", category="string", icon="cello-icon"),
        ]

    def get_all_instruments(self) -> List[Instrument]:
        return self.instruments

    def get_instrument_by_id(self, instrument_id: int) -> Optional[Instrument]:
        return next((instrument for instrument in self.instruments if instrument.id == instrument_id), None)