import yaml
import requests
from pathlib import Path
import json
from operator import itemgetter

# Paths
CONFIG = Path(__file__).resolve().parent / 'config' / 'config.yml'
OUTPUT = Path(__file__).resolve().parent / 'json' / 'aPC.json'

cfg = yaml.safe_load(open(CONFIG))

allEvents = []

for x in range(1,12):
    headers = {'apiKey': cfg['key']}
    queryURL = "https://stahmaxffcqankienulh.supabase.co/rest/v1/events?select=*&month=eq.{}&order=day,title.asc".format(x)
    r = requests.get(queryURL, headers=headers)
    data = r.json()
    for event in data:
        print(event['title'])
        allEvents.append(event)


sortedEvents = sorted(allEvents, key=itemgetter('month','day','title'))

with open(OUTPUT, 'w') as events:
    json.dump(sortedEvents, events,indent=4)