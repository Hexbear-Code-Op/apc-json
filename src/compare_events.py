import json
import sys

def main():
    old_file, new_file = sys.argv[1], sys.argv[2]
    
    with open(old_file) as f:
        old_events = json.load(f)
    
    with open(new_file) as f:
        new_events = json.load(f)

    # Adjust these keys based on your JSON structure
    old_set = {(e['title'], e['date']) for e in old_events}
    new_set = {(e['title'], e['date']) for e in new_events}
    
    added = sorted(new_set - old_set, key=lambda x: x[1])
    
    if not added:
        print("No new events detected")
        return
    
    print("Added events:")
    for name, date in added:
        print(f"- {name} ({date})")

if __name__ == "__main__":
    main()