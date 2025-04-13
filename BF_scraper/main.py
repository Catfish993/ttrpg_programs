import requests
from bs4 import BeautifulSoup as bs4
import json

url = "https://www.basicfantasy.org/srd/monstersAll.html"
response = requests.get(url)

if response.status_code == 200:
    soup = bs4(response.text, 'html.parser')
    monsters = soup.find_all('section', class_='level2 monster')

    all_monsters = []

    for monster in monsters:
        monster_entry = {}

        # Get the monster's name from <h2>
        name_tag = monster.find('h2')
        name = name_tag.text.strip() if name_tag else "Unknown"
        monster_entry["name"] = name

        table = monster.find('table')
        if not table:
            continue

        stats = {}
        header_labels = []

        # Try to extract headers (if present)
        thead = table.find('thead')
        if thead:
            ths = thead.find_all('th')
            header_labels = [th.text.strip() for th in ths if th.text.strip()]

        # Go through table rows
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')

            if len(cols) == 2:
                label = cols[0].text.strip().rstrip(':')
                value = cols[1].text.strip()
                stats[label] = value

            elif len(cols) == 3 and len(header_labels) == 2:
                label = cols[0].text.strip().rstrip(':')
                value1 = cols[1].text.strip()
                value2 = cols[2].text.strip()
                stats[label] = {
                    header_labels[0]: value1,
                    header_labels[1]: value2
                }

        monster_entry["stats"] = stats
        all_monsters.append(monster_entry)

    # Save to JSON
    with open("monsters_a.json", "w", encoding="utf-8") as f:
        json.dump(all_monsters, f, indent=2)

    print(f"✅ Saved {len(all_monsters)} monsters to monsters_a.json")

else:
    print("❌ Failed to load the page.")
