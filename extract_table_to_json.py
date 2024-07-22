import requests
from bs4 import BeautifulSoup
import json
import argparse
import os

def extract_table(url, file_path, selector_type, selector_value):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    if selector_type == 'class':
        table = soup.find('table', {'class': selector_value})
    elif selector_type == 'id':
        table = soup.find('table', {'id': selector_value})
    else:
        print("Selector type must be 'class' or 'id'.")
        return

    if table is None:
        print("Table not found on the page.")
        return

    headers = [th.text.strip() for th in table.find_all('th')]

    lines = []
    for line in table.find_all('tr')[1:]: 
        columns = line.find_all('td')
        if columns:
            line_data = {headers[i]: columns[i].text.strip() for i in range(len(columns))}
            lines.append(line_data)

    json_data = json.dumps(lines, ensure_ascii=False, indent=4)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json_data)

    print(f"Data saved in {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Extract table from an HTML page and save in JSON.')
    parser.add_argument('url', type=str, help='URL of the page with the table')
    parser.add_argument('file_path', type=str, help='Full path of the JSON file to save the data')
    parser.add_argument('selector_type', type=str, choices=['class', 'id'], help="Type of selector: 'class' or 'id'")
    parser.add_argument('selector_value', type=str, help='Value of the selector (class name or ID)')

    args = parser.parse_args()

    directory = os.path.dirname(args.file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    extract_table(args.url, args.file_path, args.selector_type, args.selector_value)

if __name__ == '__main__':
    main()
