import requests
from bs4 import BeautifulSoup
import json

url_web = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url_web)
status_code = response.status_code
print(f'Status Code: {status_code}')

content = response.content
soup = BeautifulSoup(content, 'html.parser')

data = {
    'title': soup.title.get_text(),
    'url': url_web,
    'status_code': status_code
}
with open('scraped_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

url_1 = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url_1)
status_code = response.status_code
print(f'Status Code: {status_code}')

content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Find the main table
table = soup.find('table', {'border': '1'})

# Initialize list to store datasets
datasets = []

# Extract table rows
if table:
    rows = table.find_all('tr')[1:]  # Skip header row
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            dataset = {
                'name': cols[0].text.strip(),
                'data_types': cols[1].text.strip(),
                'task': cols[2].text.strip(),
                'attribute_types': cols[3].text.strip(),
                'instances': cols[4].text.strip(),
                'attributes': cols[5].text.strip(),
                'year': cols[6].text.strip()
            }
            datasets.append(dataset)

# Save to JSON file
with open('uci_datasets.json', 'w', encoding='utf-8') as f:
    json.dump(datasets, f, indent=4)

print(f"Saved {len(datasets)} datasets to uci_datasets.json")


url_2 = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url_2)
status_code = response.status_code
print(f'Status Code: {status_code}')

content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Find the main presidents table
presidents_table = soup.find('table', {'class': 'wikitable'})
presidents = []

# Extract data from table rows
if presidents_table:
    rows = presidents_table.find_all('tr')[1:]  # Skip header row
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 6:
            # Extract text and clean it
            president_data = {
                'number': cols[0].text.strip(),
                'name': cols[1].text.strip(),
                'term_start': cols[2].text.strip(),
                'term_end': cols[3].text.strip(),
                'party': cols[4].text.strip(),
                'vice_president': cols[5].text.strip()
            }
            
            # Try to get image URL if available
            img_tag = row.find('img')
            if img_tag and 'src' in img_tag.attrs:
                president_data['image_url'] = 'https:' + img_tag['src']
            
            presidents.append(president_data)

# Save to JSON file
with open('us_presidents.json', 'w', encoding='utf-8') as f:
    json.dump(presidents, f, indent=4, ensure_ascii=False)

print(f"Saved {len(presidents)} presidents to us_presidents.json")