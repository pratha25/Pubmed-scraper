import csv
from typing import List, Dict

def write_to_csv(data: List[Dict], filename: str) -> None:
    """Writes a list of dictionaries to a CSV file."""
    if not data:
        print("⚠️ No data to write.")
        return

    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"✅ Results written to {filename}")
