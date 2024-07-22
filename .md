# Table Extractor to JSON

This Python script extracts data from an HTML table and saves it to a JSON file. It allows you to specify whether the table should be fetched by class or ID, making it flexible for different web pages.

## Requirements

Make sure you have Python installed on your system. You will also need to install the following libraries:

- `requests`
- `beautifulsoup4`

You can install these dependencies using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

### Running the Script

To run the script, use the following command:

```bash
python extract_table_to_json.py <URL> <file_path> <selector_type> <selector_value>
```

Where:
- `<URL>` is the URL of the web page containing the table.
- `<file_path>` is the full path of the JSON file where the data will be saved.
- `<selector_type>` can be `'class'` or `'id'`, depending on how the table is identified.
- `<selector_value>` is the value of the class or ID of the table.

### Usage Examples

1. **Extract table based on class:**

   ```bash
   python extract_table_to_json.py "https://example.com/page" "output/table_data.json" "class" "table-class-name"
   ```

2. **Extract table based on ID:**

   ```bash
   python extract_table_to_json.py "https://example.com/page" "output/table_data.json" "id" "table-id-name"
   ```

## Script Description

The script performs the following tasks:

1. **Makes an HTTP request to the provided URL.**
2. **Parses the HTML content of the page using BeautifulSoup.**
3. **Finds the table based on the selector type (class or ID) provided.**
4. **Extracts the headers and row data from the table.**
5. **Converts the data to JSON format.**
6. **Saves the JSON to the specified file.**

## Error Handling

- If the table is not found on the page, the script will print an error message and exit.
- If the selector type provided is not `'class'` or `'id'`, the script will print an error message and exit.

## Contributing

Feel free to contribute improvements or fixes. Create a pull request or open an issue to discuss new features.

## License

This project is licensed under the [MIT License](LICENSE).