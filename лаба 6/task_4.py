import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

def task():
    with open(INPUT_FILE, 'w', encoding = "utf8") as f:
        json_data = json.load(f)

    with open(OUTPUT_FILE) as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    return()

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end='')