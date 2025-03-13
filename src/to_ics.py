import icalendar
from pathlib import Path
import json
from datetime import datetime
from dataclasses import dataclass
from typing import Iterable

# Data paths
DATA = Path(__file__).resolve().parent / 'json' / 'aPC.json'
print(DATA)
ICAL = Path(__file__).resolve().parent / 'ics' / 'aPC.ics'
print(ICAL)


# Pre-calculations
CURRENT_DATE = datetime.now()
CURRENT_YEAR = CURRENT_DATE.year
IS_LEAP = not (CURRENT_YEAR % 4)

@dataclass
class Record:
    id: str
    title: str
    slugTitle: str
    otd: str
    description: str
    imgAltText: str
    NSFW: bool
    imgSrc: str
    date: str
    links: list[str]
    tags: list[str]
    day: int
    month: int
    
    @property
    def on_date(self) -> datetime:
        if self.month == 2 and self.day == 29 and not IS_LEAP:
            return datetime(CURRENT_YEAR, 3, 1).date()
        else:
            return datetime(CURRENT_YEAR, self.month, self.day).date()
            
    def to_event(self) -> icalendar.Event:
        event = icalendar.Event()
        event.add('summary', self.title)
        event.add('comment', self.otd)
        event.add('description', self.description)
        event.add('dtstart', self.on_date)
        event.add('dtend', self.on_date)
        event.add('dtstamp', CURRENT_DATE)
        event.add('resources', self.links)
        event.add('categories', self.tags)
        return event

def merge_events(events: Iterable[icalendar.Event]) -> icalendar.Calendar:
    cal = icalendar.Calendar()
    cal.add('version', '2.1')
    cal.add('prodid', '-//aPC//aPC//EN')
    [
        cal.add_component(event) 
        for event in events
    ]
    return cal
  
def main():
    ICAL.open('wb').write(
        merge_events(
            (
                Record(**record).to_event() 
                for record in json.loads(DATA.open(encoding="utf-8").read(), strict=False)
            )
        ).to_ical()
    )
    
if __name__ == "__main__":
    main()